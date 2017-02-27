# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from setting_street.models import TypesStreet, Street


# Create your views here.
@login_required
def street_list(request):
    type_street = TypesStreet.objects.all()
    list_street = Street.objects.all()
    return render(request,
                  'setting_street/setting_street.html',
                  {'type_street': type_street, 'list_street': list_street})


@login_required
def add_street(request):
    results = request.GET
    add_type_street = TypesStreet.objects.filter(id=results.get("id_short"))
    # try:
    if Street.objects.filter(full_street=''.join((unicode(add_type_street[0]), results.get('name_street')))):
        json = JsonResponse({'error': 'Значение присутствует'})
        return HttpResponse(json, status=500)
    # except:
    add_street = Street(street=results.get('name_street'),
                        type_street_group=add_type_street[0],
                        full_street=''.join((unicode(add_type_street[0]), results.get('name_street'))))
    add_street.save()
    response_street = {"type_street": add_type_street[0].short_name,
                       "name_street": add_street.street}
    json = JsonResponse(response_street)
    return HttpResponse(json)


@login_required
def delete_street(request):
    results = request.GET
    result = results.get('id_street')
    Street.objects.filter(id=int(result)).delete()
    return HttpResponse("object delete")
