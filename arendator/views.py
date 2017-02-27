# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from arendator.forms import ArendatorForm
from homes.views import add_arendator, ArendatorsList
from arendator.models import Arendator, TypeState, UserFullName
from datetime import datetime
from django.utils import timezone, dateformat
from search_arendator import searh
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@login_required
def add_arendator_obj(request):
    if request.method == 'POST':
        form = ArendatorForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/arendators')
    else:
        form = ArendatorForm()
    return add_arendator(request, form)


@login_required
def save_edit_arendator(request):
    if request.method == 'POST':
        arendator = Arendator.objects.get(id=request.POST.get('edit'))
        form = ArendatorForm(request.POST, instance=arendator)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/arendators')
    else:
        form = ArendatorForm()
    return edit_arendator(request, request.POST.get('edit'))


@login_required
def change_call_date(request):
    id_ar = request.GET['id'].split('-')[-1]
    arendator = Arendator.objects.get(id=id_ar)
    date_request = datetime.strptime(str(request.GET['date']), "%m/%d/%Y")
    date_change = dateformat.format(date_request, 'Y-m-d')
    arendator.call_date = date_change
    arendator.save()
    return HttpResponse(arendator.call_date)


@login_required
def change_term_date(request):
    id_ar = request.GET['id']
    arendator = Arendator.objects.get(id=id_ar)
    date_request = datetime.strptime(str(request.GET['date']), "%Y-%m-%d")
    date_change = dateformat.format(date_request, 'Y-m-d')
    arendator.date_term = date_change
    arendator.save()
    return HttpResponse(status=200)


@login_required
def change_type_state(request):
    id_ar = request.GET['id']
    type_state = TypeState.objects.get(id=request.GET.get('type_state'))
    Arendator.objects.update(id=id_ar, type_state=type_state)
    return HttpResponse(content=b'Ok')


class ArendatorListSearch(ArendatorsList):
    """docstring for ObjectListSearch"""
    template_name = "arendator/search.html"

    def get_queryset(self):
        return searh(self.request)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ArendatorListSearch, self).dispatch(request, *args, **kwargs)


@login_required
def trash_arendator(request):
    if request.method == 'POST':
        id_obj = request.POST.get('trash')
        trash_obj = Arendator.objects.get(id=id_obj)
        user = User.objects.get(id=request.POST.get('iduser'))
        trash_obj.trash = True
        trash_obj.time_trash = timezone.now()
        trash_obj.name_user_trash = user.get_full_name()
        trash_obj.save()
        return HttpResponse("Обьект 'Арендатор' перемещен в корзину")
    else:
        return HttpResponse("Ошибка")


@login_required
def restore_arendator(request):
    if request.method == 'POST':
        restore_obj = Arendator.objects.get(id=request.POST.get('id_obj'))
        restore_obj.trash = False
        restore_obj.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=500)


@login_required
def edit_arendator(request, id_arendator):
    arendator = Arendator.objects.get(id=id_arendator)
    form = ArendatorForm(instance=arendator)
    form.fields['rieltor'].queryset = UserFullName.objects.filter(is_active=True)
    form.fields['loyality'].queryset = UserFullName.objects.filter(is_active=True)
    return render(request, 'homes/add_arendator.html', {'form': form, 'edit': True, 'id_arendator': id_arendator})
