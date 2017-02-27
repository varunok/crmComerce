# -*- coding: utf-8 -*-

from arendator.models import Arendator
from single_object.models import Tie


def search_automat(request, contact_owner):
    price_automat = request.get('price_automat')
    rooms_automat = request.get('rooms_automat')
    type_obj_automat = request.get('type_obj_automat')
    area_automat = request.get('area_automat')
    repairs_automat = request.get('repairs_automat')
    district_automat = request.get('district_automat')
    id_so = request.get('id_arendator')
    arendator = Arendator.objects.get(id=id_so)
    try:
        if price_automat:
            contact_owner = contact_owner.filter(price_month__range=(arendator.price_from, arendator.price_to))
        if rooms_automat:
            contact_owner = contact_owner.filter(rooms__range=(arendator.rooms_from, arendator.rooms_to))
        if type_obj_automat:
            contact_owner = contact_owner.filter(type_facilit__in=arendator.type_building_data.all())
        if area_automat:
            contact_owner = contact_owner.filter(footage__range=(arendator.area_from, arendator.area_to))
        if repairs_automat:
            contact_owner = contact_owner.filter(repairs__in=arendator.repairs.all())
        if district_automat:
            contact_owner = contact_owner.filter(district_obj__in=arendator.district_obj.all())
        try:
            tie_c = Tie.objects.filter(tie_arenda=id_so)
            for t in tie_c:
                t.tie_arenda.clear()
        except Tie.DoesNotExist:
            pass
        for owner in contact_owner:
            # print (0, arendators)
            # if contact_owner.tie in arendator.tie_set.all():
            #     print ('1',arendators)
            #     arendators = arendators.exclude(tie__in=arendator.tie_set.all())
            #     print ('0',arendators)
            # else:
            tie, created = Tie.objects.get_or_create(tie_cont_owner=owner)
            if not Tie.objects.filter(tie_arenda=arendator, tie_cont_owner=owner).exists():
                tie.tie_arenda.add(arendator)
    except:
        return contact_owner

    return contact_owner
