# -*- coding: utf-8 -*-

from facility.models import ContactOwner
from single_object.models import TieBuyer


def search_automat_buyer(request, buyers):
    price_automat = request.get('price_automat')
    rooms_automat = request.get('rooms_automat')
    type_obj_automat = request.get('type_obj_automat')
    area_automat = request.get('area_automat')
    repairs_automat = request.get('repairs_automat')
    district_automat = request.get('district_automat')
    id_so = request.get('id_so')
    contact_owner = ContactOwner.objects.get(id=id_so)
    if not contact_owner.price_month:
        contact_owner.price_month = 0
    if not contact_owner.rooms:
        contact_owner.rooms = 0
    if not contact_owner.footage:
        contact_owner.footage = 0
    try:
        if price_automat == 'true':
            buyers = buyers.filter(price_from__lte=contact_owner.price_bay,
                                   price_to__gte=contact_owner.price_bay)
        if rooms_automat == 'true':
            buyers = buyers.filter(rooms_from__lte=int(contact_owner.rooms), rooms_to__gte=int(contact_owner.rooms))
        if type_obj_automat == 'true':
            buyers = buyers.filter(type_building_data=contact_owner.type_facilit)
        if area_automat == 'true':
            buyers = buyers.filter(area_from__lte=contact_owner.footage, area_to__gte=contact_owner.footage)
        if repairs_automat == 'true':
            buyers = buyers.filter(repairs=contact_owner.repairs)
        if district_automat == 'true':
            buyers = buyers.filter(district_obj=contact_owner.district_obj)
        try:
            TieBuyer.objects.get(tie_cont_owner=id_so).tie_buye.clear()
        except TieBuyer.DoesNotExist:
            pass
        for buyer in buyers:
            # print (0, arendators)
            # if contact_owner.tie in arendator.tie_set.all():
            #     print ('1',arendators)
            #     arendators = arendators.exclude(tie__in=arendator.tie_set.all())
            #     print ('0',arendators)
            # else:
            tie_buyers, created = TieBuyer.objects.get_or_create(tie_cont_owner=contact_owner)
            if TieBuyer.objects.filter(tie_buye=buyer, tie_cont_owner=contact_owner).exists() == False:
                tie_buyers.tie_buye.add(buyer)
    except:
        return buyers

    return buyers
