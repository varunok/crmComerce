# -*- coding: utf-8 -*-


from django.utils import timezone, dateformat
from datetime import datetime
from facility.models import ContactOwner, DatabasePhoneOwner
from django.db.models import Q


def searh(request):
    list_req = request.GET
    if 'selling' in request.path.split('/'):
        contact_owner = ContactOwner.objects.filter(list_operations__in=[1, 4])
    elif 'arend' in request.path.split('/'):
        contact_owner = ContactOwner.objects.filter(list_operations__in=[2, 3])
    else:
        contact_owner = ContactOwner.objects.all()
    try:
        if list_req.getlist('type_facility'):
            contact_owner = contact_owner.filter(type_facilit__in=list_req.getlist('type_facility'))
        if list_req.getlist('list_operations'):
            contact_owner = contact_owner.filter(list_operations__in=list_req.getlist('list_operations'))
        if int(list_req.get('currency')) == 1:
            if list_req.get('price_on'):
                contact_owner = contact_owner.filter(price_month__gte=int(list_req.get('price_on')))
            if list_req.get('price_for'):
                contact_owner = contact_owner.filter(price_month__lte=int(list_req.get('price_for')))
        else:
            if list_req.get('price_on'):
                contact_owner = contact_owner.filter(price_bay__gte=int(list_req.get('price_on')))
            if list_req.get('price_for'):
                contact_owner = contact_owner.filter(price_bay__lte=int(list_req.get('price_for')))
        if list_req.get('actuality'):
            contact_owner = contact_owner.filter(actuality__in=list_req.getlist('actuality'))
        if list_req.getlist('district'):
            contact_owner = contact_owner.filter(district_obj__in=list_req.getlist('district'))
        if list_req.get('area_for'):
            contact_owner = contact_owner.filter(footage__gte=int(list_req.get('area_for')))
        if list_req.get('area_to'):
            contact_owner = contact_owner.filter(footage__lte=int(list_req.get('area_to')))
        if list_req.get('condition'):
            contact_owner = contact_owner.filter(condition__in=list_req.get('condition'))
        if list_req.get('id_obj'):
            contact_owner = contact_owner.filter(id=list_req.get('id_obj'))
        if list_req.get('phone_obj'):
            search_phone = list_req.get('phone_obj')
            contact_owner = contact_owner.filter(Q(phone_owner__icontains=search_phone) | Q(phone_owner_plus__icontains=search_phone))
        if list_req.get('peresmotr'):
            date_old = datetime.strptime(str(list_req.get('peresmotr')), "%m/%d/%Y")
            formatted_date = dateformat.format(datetime.now(), 'Y-m-d')
            peresmotr_reformat = dateformat.format(date_old, 'Y-m-d')
            contact_owner = contact_owner.filter(review_date__range=(formatted_date, peresmotr_reformat))
        if list_req.get('street_obj'):
            contact_owner = contact_owner.filter(street_obj__exact=list_req.get('street_obj'))
        if list_req.get('rooms'):
            contact_owner = contact_owner.filter(rooms__icontains=list_req.get('rooms'))
        # if list_req.get('rooms_ot'):
        #     contact_owner = contact_owner.filter(rooms__gte=int(list_req.get('rooms_ot')))
        # if list_req.get('rooms_do'):
        #     contact_owner = contact_owner.filter(rooms__lte=int(list_req.get('rooms_do')))
        # if list_req.get('number_home'):
        #     contact_owner = contact_owner.filter(number_home=int(list_req.get('number_home')))
        if list_req.get('name_owner'):
            contact_owner = contact_owner.filter(name_owner__icontains=list_req.get('name_owner'))
        if list_req.get('comments') != '-----':
            contact_owner = contact_owner.filter(comment__icontains=list_req.get('comments'))
        if list_req.get('vip_status') == 'on':
            contact_owner = contact_owner.filter(vip_owner=list_req.get('vip_status'))
        if list_req.get('public_status') == 'on':
            contact_owner = contact_owner.filter(public=list_req.get('public_status'))
        if list_req.getlist('rieltor'):
            contact_owner = contact_owner.filter(rieltor__in=list_req.getlist('rieltor'))
        if list_req.getlist('list_subway'):
            contact_owner = contact_owner.filter(subway_obj__in=list_req.getlist('list_subway'))
        if list_req.get('type_heating'):
            contact_owner = contact_owner.filter(heating__in=list_req.getlist('type_heating'))

        if list_req.get('landmark'):
            contact_owner = contact_owner.filter(landmark__icontains=list_req.get('landmark'))
        if list_req.get('location'):
            contact_owner = contact_owner.filter(location=list_req.get('location'))
        if list_req.get('shopping_room_for'):
            contact_owner = contact_owner.filter(shopping_room__gte=int(list_req.get('shopping_room_for')))
        if list_req.get('shopping_room_to'):
            contact_owner = contact_owner.filter(shopping_room__lte=int(list_req.get('shopping_room_to')))
        if list_req.get('repairs'):
            contact_owner = contact_owner.filter(repairs=list_req.get('repairs'))
        if list_req.get('number_of_storeys'):
            contact_owner = contact_owner.filter(number_of_storeys=list_req.get('number_of_storeys'))
        if list_req.get('entrance'):
            contact_owner = contact_owner.filter(entrance=list_req.get('entrance'))
        if list_req.get('documentation'):
            contact_owner = contact_owner.filter(documentation=list_req.get('documentation'))
        if list_req.get('payments'):
            contact_owner = contact_owner.filter(payments__icontains=list_req.get('payments'))
        if list_req.getlist('under_that'):
            contact_owner = contact_owner.filter(under_that__in=list_req.getlist('under_that')).distinct()
        if list_req.getlist('availability'):
            contact_owner = contact_owner.filter(availability__in=list_req.getlist('availability')).distinct()



    except ValueError:
        pass

    return contact_owner.filter(trash=False)
