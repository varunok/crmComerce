# -*- coding: utf-8 -*-


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.generic import DetailView

from facility.models import ContactOwner
from arendator.models import Arendator
from buyer.models import Buyer
from tasking.forms import TaskingForm
from tasking.models import UserFullName, Tasking
from search_task import search
from django.contrib.auth.decorators import login_required


@login_required
def get_form_task(request, form=TaskingForm()):
    form.fields['task_facility'].queryset = ContactOwner.objects.filter(trash=False)
    form.fields['task_arendator'].queryset = Arendator.objects.filter(trash=False)
    form.fields['task_buyer'].queryset = Buyer.objects.filter(trash=False)
    form.fields['rieltor'].queryset = UserFullName.objects.filter(is_active=True)
    form.fields['access'].queryset = UserFullName.objects.filter(is_active=True)
    if form.errors:
        return render(request, 'tasking/form.html', {"form": form}, status=500)

    return render(request, 'tasking/form.html', {"form": form})


@login_required
def save_form_tasking(request):
    if request.method == 'POST':
        if request.POST.get('edit'):
            return save_edit_form_tasking(request)
        form = TaskingForm(request.POST)
        if form.is_valid():
            form.save()
            task = Tasking.objects.last()
            return single_task(request, task)
    else:
        form = TaskingForm(request.POST)
    return get_form_task(request, form)


@login_required
def save_edit_form_tasking(request):
    if request.method == 'POST':
        tasking = Tasking.objects.get(id=request.POST.get('edit'))
        form = TaskingForm(request.POST, instance=tasking)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200)
    else:
        form = TaskingForm()
    return get_form_task(request, form)


@login_required
def single_task(request, task):
    return render(request, 'tasking/single_task.html', {"tasking": task})


@login_required
def search_task(request):
    if request.method == 'POST':
        tasking_list = search(request.POST)
        return render(request, 'tasking/obj_tasking.html', {"tasking_list": tasking_list})


@login_required
def edit_form(request):
    if request.method == 'POST':
        tasking = Tasking.objects.get(id=request.POST.get('id'))
        form = TaskingForm(instance=tasking)
        form.fields['rieltor'].queryset = UserFullName.objects.filter(is_active=True)
        form.fields['access'].queryset = UserFullName.objects.filter(is_active=True)
        return render(request, 'tasking/form.html', {"form": form, "edit": True, 'id_task': tasking.id})


@login_required
def to_archive(request):
    if request.method == 'POST':
        task = Tasking.objects.get(id=request.POST['id'])
        task.task_archiv = True
        task.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=500)


@login_required
def to_trash(request):
    if request.method == 'POST':
        Tasking.objects.get(id=request.POST['id']).delete()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=500)
