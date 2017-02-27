# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def setting_list_street(request):
    return render(request, 'setting_street/setting_list_street.html', {})
