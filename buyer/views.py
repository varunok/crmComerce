# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from buyer.forms import BuyerForm
from homes.views import add_buyer, BuyersList

from buyer.models import Buyer, TypeState, UserFullName
from datetime import datetime
from django.utils import timezone, dateformat
from search_buyer import searh
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@login_required
def add_buyer_obj(request):
    if request.method == 'POST':
        form = BuyerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/buyers')
    else:
        form = BuyerForm()
    return add_buyer(request, form)


@login_required
def save_edit_buyer(request):
    if request.method == 'POST':
        buyer = Buyer.objects.get(id=request.POST.get('edit'))
        form = BuyerForm(request.POST, instance=buyer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/buyers')
    else:
        form = BuyerForm()
    return edit_buyer(request, request.POST.get('edit'))


@login_required
def change_call_date(request):
    id_ar = request.GET['id'].split('-')[-1]
    buyer = Buyer.objects.get(id=id_ar)
    date_request = datetime.strptime(str(request.GET['date']), "%Y-%m-%d")
    date_change = dateformat.format(date_request, 'Y-m-d')
    buyer.call_date = date_change
    buyer.save()
    return HttpResponse("ok")


@login_required
def change_term_date(request):
    id_ar = request.GET['id']
    arendator = Buyer.objects.get(id=id_ar)
    date_request = datetime.strptime(str(request.GET['date']), "%Y-%m-%d")
    date_change = dateformat.format(date_request, 'Y-m-d')
    arendator.date_term = date_change
    arendator.save()
    return HttpResponse(status=200)


@login_required
def change_type_state(request):
    id_ar = request.GET['id']
    type_state = TypeState.objects.get(id=request.GET.get('type_state'))
    Buyer.objects.update(id=id_ar, type_state=type_state)
    return HttpResponse(content=b'Ok')


class BuyerListSearch(BuyersList):
    """docstring for ObjectListSearch"""
    template_name = "buyer/search.html"

    def get_queryset(self):
        return searh(self.request)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BuyerListSearch, self).dispatch(request, *args, **kwargs)


@login_required
def trash_buyer(request):
    if request.method == 'POST':
        id_obj = request.POST.get('trash')
        trash_obj = Buyer.objects.get(id=id_obj)
        user = User.objects.get(id=request.POST.get('iduser'))
        trash_obj.trash = True
        trash_obj.time_trash = timezone.now()
        trash_obj.name_user_trash = user.get_full_name()
        trash_obj.save()
        return HttpResponse("Обьект 'Покупатель' перемещен в корзину")
    else:
        return HttpResponse("Ошибка")


@login_required
def restore_buyers(request):
    if request.method == 'POST':
        restore_obj = Buyer.objects.get(id=request.POST.get('id_obj'))
        restore_obj.trash = False
        restore_obj.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=500)


@login_required
def edit_buyer(request, id_buyer):
    buyer = Buyer.objects.get(id=id_buyer)
    form = BuyerForm(instance=buyer)
    form.fields['rieltor'].queryset = UserFullName.objects.filter(is_active=True)
    form.fields['loyality'].queryset = UserFullName.objects.filter(is_active=True)
    return render(request, 'homes/add_buyer.html', {'form': form, 'edit': True, 'id_buyer': id_buyer})
