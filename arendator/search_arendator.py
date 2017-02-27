# -*- coding: utf-8 -*-


from django.utils import timezone, dateformat
import datetime
from arendator.models import Arendator
from django.db.models import Q

def searh(request):
    data = request.GET
    arendator = Arendator.objects.all()
    try:
        if data.get('arendator'):
            arendator = arendator.filter(id=data.get('arendator'))
        if data.getlist('user'):
            arendator = arendator.filter(rieltor__in=data.getlist('user'))
        if data.get('price_from'):
            arendator = arendator.filter(price_from__gte=int(data.get('price_from')))
        if data.get('price_to'):
            arendator = arendator.filter(price_to__lte=int(data.get('price_to')))
        if data.get('terms'):
            term = str(data.get('terms')).split('/')
            term = datetime.date(int(term[2]), int(term[0]), int(term[1]))
            start_date = datetime.date(2000, 1, 1)
            arendator = arendator.filter(date_term__range=(start_date, term))
        if data.getlist('district_name'):
            arendator = arendator.filter(district_obj__in=data.getlist('district_name'))
        if data.get('area_from'):
            arendator = arendator.filter(area_from__gte=int(data.get('area_from')))
        if data.get('area_to'):
            arendator = arendator.filter(area_to__lte=int(data.get('area_to')))
        if data.getlist('state'):
            arendator = arendator.filter(type_state__in=data.getlist('state'))
        if data.get('call_date_from'):
            call_date_from = data.get('call_date_from').split('/')
            call_date_from = datetime.date(int(call_date_from[2]), int(call_date_from[0]), int(call_date_from[1]))
            if data.get('call_date_to'):
                call_date_to = data.get('call_date_to').split('/')
                call_date_to = datetime.date(int(call_date_to[2]), int(call_date_to[0]), int(call_date_to[1]))
                arendator = arendator.filter(call_date__range=(call_date_from, call_date_to))
            else:
                end_date = datetime.date(2100, 1, 1)
                arendator = arendator.filter(call_date__range=(call_date_from, end_date))
        if data.get('call_date_to'):
            call_date_to = data.get('call_date_to').split('/')
            call_date_to = datetime.date(int(call_date_to[2]), int(call_date_to[0]), int(call_date_to[1]))
            start_date = datetime.date(2000, 1, 1)
            arendator = arendator.filter(call_date__range=(start_date, call_date_to))
        if data.get('phone_n'):
            arendator = arendator.filter(Q(phone_first__iexact=data.get('phone_n')) | Q(phone_second__iexact=data.get('phone_n')))
        if data.getlist('type_facility'):
            arendator = arendator.filter(type_building_data__in=data.getlist('type_facility'))
        if data.getlist('stage_a'):
            arendator = arendator.filter(type_stage__in=data.getlist('stage_a'))
        if data.getlist('type_client'):
            arendator = arendator.filter(type_client__in=data.getlist('type_client'))
        if data.get('rooms_from'):
            arendator = arendator.filter(rooms_from__gte=int(data.get('rooms_from')))
        if data.get('rooms_to'):
            arendator = arendator.filter(rooms_to__lte=int(data.get('rooms_to')))
        if data.get('email_a'):
            arendator = arendator.filter(email__icontains=data.get('email_a'))
        if data.get('name_a'):
            arendator = arendator.filter(name__icontains=data.get('name_a'))
        if data.get('shopping_room_from'):
            arendator = arendator.filter(shopping_room_from__gte=int(data.get('shopping_room_from')))
        if data.get('shopping_room_to'):
            arendator = arendator.filter(shopping_room_to__lte=int(data.get('shopping_room_to')))
        if data.getlist('under_that'):
            arendator = arendator.filter(under_that__in=data.getlist('under_that'))
        if data.getlist('repair'):
            arendator = arendator.filter(repairs__in=data.getlist('repair'))
        if data.getlist('storeys'):
            arendator = arendator.filter(number_of_storeys__in=data.getlist('storeys'))
        if data.getlist('entrance'):
            arendator = arendator.filter(entrance__in=data.getlist('entrance'))
        if data.getlist('location'):
            arendator = arendator.filter(location__in=data.getlist('location'))
    except:
        return arendator.filter(trash=False)

    return arendator.filter(trash=False)
