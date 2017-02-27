# -*- coding: utf-8 -*-

from buyer.models import Buyer
from single_object.models import TieBuyer


def search_automat(request, contact_owner):
    price_automat = request.get('price_automat')
    rooms_automat = request.get('rooms_automat')
    type_obj_automat = request.get('type_obj_automat')
    area_automat = request.get('area_automat')
    repairs_automat = request.get('repairs_automat')
    district_automat = request.get('district_automat')
    id_so = request.get('id_buyer')
    buyer = Buyer.objects.get(id=id_so)
    try:
        if price_automat:
            contact_owner = contact_owner.filter(price_bay__range=(buyer.price_from, buyer.price_to))
        if rooms_automat:
            contact_owner = contact_owner.filter(rooms__range=(buyer.rooms_from, buyer.rooms_to))
        if type_obj_automat:
            contact_owner = contact_owner.filter(type_facilit__in=buyer.type_building_data.all())
        if area_automat:
            contact_owner = contact_owner.filter(total_area__range=(buyer.area_from, buyer.area_to))
        if repairs_automat:
            contact_owner = contact_owner.filter(repairs__in=buyer.repairs.all())
        if district_automat:
            contact_owner = contact_owner.filter(district_obj__in=buyer.district_obj.all())
        try:
            tie_c = TieBuyer.objects.filter(tie_buye=id_so)
            for t in tie_c:
                t.tie_buye.clear()
        except TieBuyer.DoesNotExist:
            pass
        for owner in contact_owner:
            # print (0, buyers)
            # if contact_owner.tie in buyer.tie_set.all():
            #     print ('1',buyers)
            #     buyers = buyers.exclude(tie__in=buyer.tie_set.all())
            #     print ('0',buyers)
            # else:
            tie, created = TieBuyer.objects.get_or_create(tie_cont_owner=owner)
            if not TieBuyer.objects.filter(tie_buye=buyer, tie_cont_owner=owner).exists():
                tie.tie_buye.add(buyer)
    except:
        return contact_owner

    return contact_owner
