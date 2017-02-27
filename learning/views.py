# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from learning.forms import LearnForm
from learning.models import Learn
from django.contrib.auth.decorators import login_required


@login_required
def get_learn_list(request):
    learning = Learn.objects.all()
    return render(request, 'learning/learn.html', {'learning': learning})


@login_required
def add_learning(request):
    form = LearnForm()
    return render(request, 'learning/add_learning.html', {'form': form})


@login_required
def add_learn_form(request):
    if request.method == 'POST':
        form = LearnForm(request.POST)
        if form.is_valid():
            form.save()
            # return render(request, 'learning/learn.html', {'learning': learning})
            return HttpResponseRedirect('get_learn_list')
    else:
        form = LearnForm()
    return render(request, 'learning/add_learning.html', {'form': form})


@login_required
def del_learn(request):
    if request.method == 'POST':
        Learn.objects.get(id=request.POST.get('id')).delete()
        return HttpResponse(status=200)
    return HttpResponse(status=500)
