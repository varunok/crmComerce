# -*- coding: utf-8 -*-


from django.http import HttpResponse, JsonResponse
from work_table import InsertData, SetShows, SearchData, NotPost
from facility.models import ContactOwner
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def posting_true(request):
    if request.method == 'POST':
        single_object = ContactOwner.objects.get(id=request.POST['id_so'])
        if SearchData(single_object).isFind:
            SetShows(request.POST['id_so'], 'true')
            single_object.public = True
            single_object.save()
            return HttpResponse(JsonResponse({'data': 'true'}), status=200)
        else:
            if InsertData(single_object).isPost:
                single_object.public = True
                single_object.save()
                return HttpResponse(JsonResponse({'data': 'true'}), status=200)
            else:
                return HttpResponse(status=500)
    else:
        return HttpResponse(status=500)


@login_required
def posting_false(request):
    if request.method == 'POST':
        single_object = ContactOwner.objects.get(id=request.POST['id_so'])
        single_object.public = False
        single_object.save()
        SetShows(request.POST['id_so'], 'false')
        NotPost(request.POST['id_so'])
        return HttpResponse(JsonResponse({'data': 'false'}), status=200)
    else:
        return HttpResponse(status=500)
