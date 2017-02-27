# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from send_messege_user.models import UserMessage
from django.contrib.auth.models import User
from extuser.models import MyUser
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def send_messege_user(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.POST['id_user'])
        send_user = MyUser.objects.get(user=request.user.id)
        UserMessage(user_message=user, message=request.POST['text_messege'], from_user=send_user).save()
        return HttpResponse('message send')
    else:
        return HttpResponse('error')


@login_required
def get_messege(request):
    messages = UserMessage.objects.filter(user_message=request.user.id, read=False)
    return HttpResponse(JsonResponse({"new_message": len(messages)}))


@login_required
def get_new_message_html(request):
    messages = UserMessage.objects.filter(user_message=request.user.id, read=False)
    return render(request, 'send_messege_user/message_user.html', {"messages": messages})


@login_required
def get_text_message(request):
    id_mes = request.GET['id_mes'].split('-')[-1]
    message = UserMessage.objects.get(id=id_mes)
    message = JsonResponse({
        "id_message": message.id,
        "from_fn": message.from_user.user.first_name,
        "from_ln": message.from_user.user.last_name,
        "time": message.time_message,
        "text_message": message.message})
    return HttpResponse(message)


@login_required
def reading_message(request):
    if request.method == 'POST':
        id_mes = request.POST['id']
        message = UserMessage.objects.get(id=id_mes)
        message.read = True
        message.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=404)
