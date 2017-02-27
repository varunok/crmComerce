# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse
from facility.models import ContactOwner
from arendator.models import Arendator
from buyer.models import Buyer
from meeting.models import Meeting, UserFullName, TypeStatus
from meeting.forms import MeetingForm
from search_meet import search
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def get_form_task(request, form=MeetingForm()):
    form.fields['meet_facility'].queryset = ContactOwner.objects.filter(trash=False)
    form.fields['meet_arendator'].queryset = Arendator.objects.filter(trash=False)
    form.fields['meet_buyer'].queryset = Buyer.objects.filter(trash=False)
    form.fields['rieltor'].queryset = UserFullName.objects.filter(is_active=True)
    form.fields['access'].queryset = UserFullName.objects.filter(is_active=True)
    if form.errors:
        return render(request, 'meeting/form.html', {"form": form}, status=500)
    return render(request, 'meeting/form.html', {"form": form})


@login_required
def save_form_meeting(request):
    if request.method == 'POST':
        if request.POST.get('edit'):
            return save_edit_form_meeting(request)
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            meet = Meeting.objects.filter().order_by('id').last()
            return single_meet(request, meet)
    else:
        form = MeetingForm()
    return get_form_task(request, form)


@login_required
def save_edit_form_meeting(request):
    if request.method == 'POST':
        meeting = Meeting.objects.get(id=request.POST.get('edit'))
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200)
    else:
        form = MeetingForm()
    return get_form_task(request, form)


# def edit_single_meet(request, meet):
#     data_meet = serializers.serialize("json", [meet], indent=2,
#                                       use_natural_foreign_keys=True, use_natural_primary_keys=True)
#     return HttpResponse(data_meet)
#     return HttpResponseRedirect('/meeting')


@login_required
def single_meet(request, meet):
    status_list = TypeStatus.objects.all()
    return render(request, 'meeting/single_meet.html', {"meeting": meet, "status_list": status_list})


@login_required
def to_archive(request):
    if request.method == 'POST':
        task = Meeting.objects.get(id=request.POST['id'])
        task.meet_archiv = True
        task.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=500)


@login_required
def edit_form(request):
    if request.method == 'POST':
        meeting = Meeting.objects.get(id=request.POST.get('id'))
        form = MeetingForm(instance=meeting)
        return render(request, 'meeting/form.html', {"form": form, "edit": True, 'id_meet': meeting.id})


@login_required
def to_trash(request):
    if request.method == 'POST':
        Meeting.objects.get(id=request.POST['id']).delete()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=500)


@login_required
def search_meet(request):
    if request.method == 'POST':
        meeting_list = search(request.POST)
        status_list = TypeStatus.objects.all()
        return render(request, 'meeting/obj_meeting.html', {"meeting_list": meeting_list,
                                                            "status_list": status_list})
