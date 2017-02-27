# -*- coding: utf-8 -*-


from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.utils import timezone, dateformat


from .models import Notes


# Create your views here.


@login_required
def note_add(request):
    results = request.GET
    if results.get('notes'):
        if len(results.get('notes')) > 10:
            name = results.get('notes')[0:10] + '...'
        else:
            name = results.get('notes')
        notes_add = Notes(text=results.get('notes'),
                          name=name)
        notes_add.save()
        datarequest = {'response': True,
                       'name': name,
                       'id': notes_add.id,
                       'date': dateformat.format(notes_add.date, "d E Y H:i")}
        json = JsonResponse(datarequest)
        return HttpResponse(json)
    else:
        datarequest = {'response': False}
        json = JsonResponse(datarequest)
        return HttpResponse(json)


@login_required
def note_del(request):
    result = request.GET
    if result.get('del'):
        result = result.get('del')
        result = result.split('-')[-1]
        Notes.objects.filter(id=int(result)).delete()
        # print(Notes.objects.filter(id=int(result)))
        # if Notes.objects.filter(id=int(result))==[]:
        result = {'status': 1, 'id': int(result)}
        json = JsonResponse(result)
        return HttpResponse(json)
        # else:
        #     result = {'status': 0}
        #     json = JsonResponse(result)
        #     return HttpResponse(json)
    else:
        result = {'status': 0}
        json = JsonResponse(result)
        return HttpResponse(json)


@login_required
def note_edit(request):
    result = request.GET
    if result.get('edit'):
        if len(result.get('text')) > 10:
            name = result.get('text')[0:10] + '...'
        else:
            name = result.get('text')
        id_numb = int(result.get('edit').split('-')[-1])
        text = result.get('text')
        Notes.objects.filter(id=id_numb).update(text=text,
                                                name=name,
                                                date=timezone.now())
        result = Notes.objects.filter(id=id_numb).values()[0]
        result['date'] = dateformat.format(datetime.now(), "d E Y H:i")
        json = JsonResponse(result)
        return HttpResponse(json)
