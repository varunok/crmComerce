# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from extuser.models import MyUser
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone, dateformat
from datetime import datetime
# Create your views here.


@login_required
def who_online(request):
    try:
        users = User.objects.all()
        dict_users = {}
        for user_r in users:
            if user_r.id == request.user.id:
                user_r.last_login = request.GET['date']
                user_r.save()
            dict_users[user_r.id] = {}
            user_r.last_login = str(user_r.last_login).split('.')[0]
            date_old = datetime.strptime(str(user_r.last_login), "%Y-%m-%d %H:%M:%S")
            dt = str(timezone.now() - date_old).split(',')
            if len(dt) > 1:
                dict_users[user_r.id]["login"] = user_r.last_login
            else:
                dt = dt[0].split(':')
                if int(dt[1]) < 15 and int(dt[0]) == 0:
                    dict_users[user_r.id]["login"] = 'online'
                elif int(dt[1]) >= 15:
                    dict_users[user_r.id]["login"] = str(timezone.now() - date_old).split('.')[0]
                elif int(dt[0]):
                    dict_users[user_r.id]["login"] = str(timezone.now() - date_old).split('.')[0]
        return HttpResponse(JsonResponse(dict_users))
    except:
        return HttpResponse('error')


@login_required
def who_online_html(request):
    list_user = MyUser.objects.all()
    return render(request, 'who_online/who_online.html', {"list_user": list_user})
