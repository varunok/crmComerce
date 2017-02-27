# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from homes.views import ObjectList, ArendatorsList, BuyersList
from facility.models import ContactOwner
from arendator.models import Arendator
from buyer.models import Buyer
from send_messege_user.models import UserMessage
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from posting.work_table import NotPost

# Create your views here.


@login_required
def list_trash(request):
    return render(request, 'trash_object/list_trash.html', {'time': timezone.now()})


class ObjectListTrash(ObjectList):
    """docstring for ClassName"""
    template_name = 'trash_object/objects_trash.html'
    qeryset = ContactOwner.objects.filter(trash=True)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ObjectListTrash, self).dispatch(request, *args, **kwargs)


class ArendatorListTrash(ArendatorsList):
    """docstring for ClassName"""
    template_name = 'trash_object/arendator_trash.html'
    queryset = Arendator.objects.all().filter(trash=True)
    context_object_name = 'arendator_list'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ArendatorListTrash, self).dispatch(request, *args, **kwargs)


class BuyerListTrash(BuyersList):
    """docstring for ClassName"""
    template_name = 'trash_object/buyer_trash.html'
    queryset = Buyer.objects.all().filter(trash=True)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BuyerListTrash, self).dispatch(request, *args, **kwargs)


@login_required
def del_obj(request):
    if request.method == 'POST':
        id_obj = request.POST.get('del')
        ContactOwner.objects.get(id=id_obj).delete()
        NotPost(id_obj)
        return HttpResponse(u"Обьект удален")
    else:
        return HttpResponse(u"Ошибка удаления")


@login_required
def del_arendator(request):
    if request.method == 'POST':
        id_obj = request.POST.get('del')
        Arendator.objects.get(id=id_obj).delete()
        return HttpResponse(u"Обьект удален")
    else:
        return HttpResponse(u"Ошибка удаления")


@login_required
def del_buyer(request):
    if request.method == 'POST':
        id_obj = request.POST.get('del')
        Buyer.objects.get(id=id_obj).delete()
        return HttpResponse(u"Обьект удален")
    else:
        return HttpResponse(u"Ошибка удаления")


@login_required
def archiv_email(request):
    messages = UserMessage.objects.filter(read=True)
    print(messages)
    return render(request, 'trash_object/archiv_email.html', {'time': timezone.now(),
                                                              'messages': messages})


@login_required
def delete_message(request):
    if request.method == 'POST':
        id_message = request.POST['id']
        # ff = UserMessage.objects.get(id=id_message)
        # print ff
        UserMessage.objects.get(id=id_message).delete()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=404)


@login_required
def go_trash(request):
    pass
