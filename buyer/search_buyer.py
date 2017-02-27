# -*- coding: utf-8 -*-


from django.utils import timezone, dateformat
import datetime
from buyer.models import Buyer
from django.db.models import Q


def searh(request):
    data = request.GET
    buyer = Buyer.objects.all()
    try:
        if data.get('buyer'):
            buyer = buyer.filter(id=data.get('buyer'))
        if data.getlist('user'):
            buyer = buyer.filter(rieltor__in=data.getlist('user'))
        if data.get('price_from'):
            buyer = buyer.filter(price_from__gte=int(data.get('price_from')))
        if data.get('price_to'):
            buyer = buyer.filter(price_to__lte=int(data.get('price_to')))
        if data.get('terms'):
            term = str(data.get('terms')).split('/')
            term = datetime.date(int(term[2]), int(term[0]), int(term[1]))
            start_date = datetime.date(2000, 1, 1)
            buyer = buyer.filter(date_term__range=(start_date, term))
        if data.getlist('district_name'):
            buyer = buyer.filter(district_obj__in=data.getlist('district_name'))
        if data.get('area_from'):
            buyer = buyer.filter(area_from__gte=int(data.get('area_from')))
        if data.get('area_to'):
            buyer = buyer.filter(area_to__lte=int(data.get('area_to')))
        if data.getlist('state'):
            buyer = buyer.filter(type_state__in=data.getlist('state'))
        if data.get('call_date_from'):
            call_date_from = data.get('call_date_from').split('/')
            call_date_from = datetime.date(int(call_date_from[2]), int(call_date_from[0]), int(call_date_from[1]))
            if data.get('call_date_to'):
                call_date_to = data.get('call_date_to').split('/')
                call_date_to = datetime.date(int(call_date_to[2]), int(call_date_to[0]), int(call_date_to[1]))
                buyer = buyer.filter(call_date__range=(call_date_from, call_date_to))
            else:
                end_date = datetime.date(2100, 1, 1)
                buyer = buyer.filter(call_date__range=(call_date_from, end_date))
        if data.get('call_date_to'):
            call_date_to = data.get('call_date_to').split('/')
            call_date_to = datetime.date(int(call_date_to[2]), int(call_date_to[0]), int(call_date_to[1]))
            start_date = datetime.date(2000, 1, 1)
            buyer = buyer.filter(call_date__range=(start_date, call_date_to))
        if data.get('phone_n'):
            buyer = buyer.filter(Q(phone_first__iexact=data.get('phone_n')) | Q(phone_second__iexact=data.get('phone_n')))
        if data.getlist('type_facility'):
            buyer = buyer.filter(type_building_data__in=data.getlist('type_facility'))
        if data.getlist('stage_a'):
            buyer = buyer.filter(type_stage__in=data.getlist('stage_a'))
        if data.getlist('type_client'):
            buyer = buyer.filter(type_client__in=data.getlist('type_client'))
        if data.get('rooms_from'):
            buyer = buyer.filter(rooms_from__gte=int(data.get('rooms_from')))
        if data.get('rooms_to'):
            buyer = buyer.filter(rooms_to__lte=int(data.get('rooms_to')))
        if data.get('email_a'):
            buyer = buyer.filter(email__icontains=data.get('email_a'))
        if data.get('name_a'):
            buyer = buyer.filter(name__icontains=data.get('name_a'))
        if data.get('shopping_room_from'):
            buyer = buyer.filter(shopping_room_from__gte=int(data.get('shopping_room_from')))
        if data.get('shopping_room_to'):
            buyer = buyer.filter(shopping_room_to__lte=int(data.get('shopping_room_to')))
        if data.getlist('under_that'):
            buyer = buyer.filter(under_that__in=data.getlist('under_that'))
        if data.getlist('repair'):
            buyer = buyer.filter(repairs__in=data.getlist('repair'))
        if data.getlist('storeys'):
            buyer = buyer.filter(number_of_storeys__in=data.getlist('storeys'))
        if data.getlist('entrance'):
            buyer = buyer.filter(entrance__in=data.getlist('entrance'))
        if data.getlist('location'):
            buyer = buyer.filter(location__in=data.getlist('location'))
    except:
        return buyer.filter(trash=False)

    return buyer.filter(trash=False)
