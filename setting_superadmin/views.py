# -*- coding: utf-8 -*-


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from setting_superadmin.forms import AllToCallForm, AllToConnectForm
from setting_superadmin.models import AllToCall, AllToConnect
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def list_setting_superadmin(request):
    return render(request, 'setting_superadmin/list_settings.html', {'time': timezone.now()})


@login_required
def all_to_call(request, form=AllToCallForm()):
    post, create = AllToCall.objects.get_or_create(id=1)
    form = AllToCallForm(instance=post)
    return render(request, 'setting_superadmin/all_to _call.html', {'time': timezone.now(),
                                                                    'form': form,
                                                                    'post': post})


@login_required
def save_call(request):
    if request.method == 'POST':
        # try:
        post, create = AllToCall.objects.get_or_create(id=1)
        form = AllToCallForm(request.POST, request.FILES, instance=post)
        # except:
        #     form = AllToCallForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list_setting_superadmin')
        else:
            return all_to_call(request, form)
    return HttpResponseRedirect('/list_setting_superadmin')


@login_required
def all_to_connect(request, form=AllToConnectForm()):
    try:
        post = get_object_or_404(AllToConnect, id=1)
        form = AllToConnectForm(instance=post)
    except:
        pass
    return render(request, 'setting_superadmin/all_to_connect.html', {'time': timezone.now(),
                                                                      'form': form})


@login_required
def save_connect(request):
    if request.method == 'POST':
        try:
            post = get_object_or_404(AllToConnect, id=1)
            print(post)
            form = AllToConnectForm(request.POST, instance=post)
        except:
            form = AllToConnectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list_setting_superadmin')
        else:
            return all_to_connect(request, form)
    return HttpResponseRedirect('/list_setting_superadmin')
