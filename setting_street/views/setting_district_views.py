# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.utils import timezone, dateformat
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from setting_street.models import District


@login_required
def setting_district(request):
    list_district = District.objects.all()
    return render(request, 'setting_street/setting_district.html', {'time': timezone.now(), 'list_district': list_district})


@login_required
def add_district(request):
    results = request.GET
    try:
        add_district = District(district=results.get('name_district'))
        add_district.save()
        response_district = {"name_district": add_district.district}
        json = JsonResponse(response_district)
        return HttpResponse(json)
    except:
        return HttpResponse("Значение присутствует")


@login_required
def delete_district(request):
    results = request.GET
    District.objects.filter(id=int(results.get('id_district'))).delete()
    return HttpResponse("object delete")
