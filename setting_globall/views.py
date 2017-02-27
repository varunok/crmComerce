# -*- coding: utf-8 -*-


# Create your views here.
from django.db import DataError
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from setting_globall.models import NationalCarrency, ListNationalCarrency, FranshiseSity, Franshise, Subscribe
from setting_globall.forms import SubscribeForm
from django.contrib.auth.decorators import login_required


@login_required
def setting_globall(request):
    class FakeClass(object):
        pass
    list_currency = ListNationalCarrency.objects.all()
    try:
        nat_curr = NationalCarrency.objects.get(id=1)
    except:
        nat_curr = ''
    try:
        sity = FranshiseSity.objects.get(id=1)
    except:
        sity = FakeClass()
        sity.sity = ''
    try:
        franshise = Franshise.objects.get(id=1)
    except:
        franshise = FakeClass()
        franshise.franshise = ''
    return render(request, 'setting_globall/setting_globall.html', {'time': timezone.now(),
                                                                    'list_currency': list_currency,
                                                                    'nat_curr': nat_curr,
                                                                    'sity': sity.sity,
                                                                    'franshise': franshise.franshise})


@login_required
def nat_currency(request):
    if request.method == 'POST':
        try:
            if NationalCarrency.objects.filter(id=1):
                add_currency = NationalCarrency.objects.get(id=1)
                add_currency.currency = request.POST['carrency']
                add_currency.save()
                return HttpResponse(u'Значение изменено')
            else:
                add_currency = NationalCarrency(currency=request.POST['carrency'])
                add_currency.save()
                add_currency = NationalCarrency(currency='$')
                add_currency.save()
                return HttpResponse(u'Значение сохранено')
        except DataError:
            return HttpResponse(u'Ошибка', status=404)
    return HttpResponse(u'Ошибка', status=404)


@login_required
def sity_franshise(request):
    if request.method == 'POST':
        sity, create = FranshiseSity.objects.get_or_create(id=1)
        sity.sity = request.POST.get('sity')
        sity.save()
        return HttpResponse(u'Значение сохранено')
    else:
        return HttpResponse(u'Ошибка', status=404)


@login_required
def franshise(request):
    if request.method == 'POST':
        franshise, create = Franshise.objects.get_or_create(id=1)
        franshise.franshise = request.POST.get('franshise')
        franshise.save()
        return HttpResponse(u'Значение сохранено')
    else:
        return HttpResponse(u'Ошибка', status=404)


@login_required
def get_subscribe(request):
    subs, create = Subscribe.objects.get_or_create(id=1)
    form = SubscribeForm(instance=subs)
    return render(request, 'setting_globall/subscribe.html', {'form': form})


@login_required
def save_subscribe_form(request):
    subs, create = Subscribe.objects.get_or_create(id=1)
    if request.method == 'POST':
        form = SubscribeForm(request.POST, instance=subs)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('setting')
    else:
        form = SubscribeForm(instance=subs)
    return render(request, 'setting_globall/subscribe.html', {'form': form})
