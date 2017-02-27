# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.utils import timezone, dateformat
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from setting_street.models import Subway


@login_required
def setting_subway(request):
    list_subway = Subway.objects.all()
    return render(request, 'setting_street/setting_subway.html', {'time': timezone.now(), 'list_subway': list_subway})


@login_required
def add_subway(request):
    results = request.GET
    try:
        add_subway = Subway(subway=results.get('name_subway'))
        add_subway.save()
        response_subway = {"name_subway": add_subway.subway}
        json = JsonResponse(response_subway)
        return HttpResponse(json)
    except:
        return HttpResponse("Значение присутствует")


@login_required
def delete_subway(request):
    results = request.GET
    Subway.objects.filter(id=int(results.get('id_subway'))).delete()
    return HttpResponse("object delete")