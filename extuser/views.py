# -*- coding: utf-8 -*-


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils import timezone, dateformat
from django.contrib.auth.models import User
from extuser.models import UsersGroupExtUser, MyUser, RecoveryPass
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from setting_mail_delivery.models import TemplateEmail, TemplateSms, SettingSMS, SettingEmail
from active_franshise import Active
from setting_globall.models import Franshise
from django.core.files import File
from django.db import IntegrityError

EMAIL_HOST_USER = settings.EMAIL_HOST_USER

# Create your views here.


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "extuser/log_in.html"
    success_url = "/"


def login_user(request):
    if request.method == 'POST':
        if request.POST.get('login') is not None:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                if not user.is_superuser:
                    try:
                        if not Active().franshises():
                            franshise = Franshise.objects.get(id=1)
                            franshise_site = ''.join(['http://', 'admin.', str(franshise.franshise), '/?page=franchise&franchise_action=list'])
                            return HttpResponseRedirect(franshise_site)
                    except:
                        return HttpResponse(content=b'ERROR. Обратитесь к администратору.')
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/')


@login_required
def logout_user(request):
    if request.method == 'GET':
        logout(request)
        return HttpResponseRedirect("accounts/login/")


@login_required
class RegisterFormView(FormView):
    form_class = UserCreationForm
    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/"
    # Шаблон, который будет использоваться при отображении представления.
    template_name = "extuser/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()
        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


@login_required
def register(request):
    type_user = UsersGroupExtUser.objects.all()
    return render(request, 'extuser/register.html', {'type_user': type_user})


@login_required
def add_user(request):
    if request.method == 'POST':
        if request.POST.get('add_user') is not None:
            if request.user.is_superuser or request.user.myuser.type_user.id == 1:
                try:
                    result = request.POST
                    new_user = User.objects.create_user(last_login=timezone.now(), username=result.get('email'), first_name=result.get('first_name'), last_name=result.get('last_name'), email=result.get('email'), password=result.get('password'))
                    new_user.save()
                    if not request.FILES.get('photo'):
                        reopen = open('media/avatar/avatar_zaglushka.jpg', 'rb')
                        image_file = File(reopen)
                    else:
                        image_file = request.FILES.get('photo')
                    add_img = MyUser(id=new_user.id, image=image_file, user_id=new_user.id, type_user_id=result.get('type_user'))
                    add_img.save()
                    recovery = RecoveryPass(email=result.get('email'), password=result.get('password'))
                    recovery.save()
                except IntegrityError:
                    type_user = UsersGroupExtUser.objects.all()
                    return render(request, 'extuser/register.html', {'type_user': type_user,
                                                                     'user_is': True})
            return user_list(request)


@login_required
def edit_user(request, id):
    user_edit = MyUser.objects.get(pk=id)
    return render(request, 'extuser/edit_user.html', {'user_edit': user_edit})


@login_required
def save_edit_user(request):
    if request.method == 'POST':
        User.objects.filter(id=request.POST.get('id_user')).update(first_name=request.POST.get('first_name'),
                                                                   last_name=request.POST.get('last_name'),
                                                                   email=request.POST.get('email'),
                                                                   username=request.POST.get('email'))
        if request.FILES.get('photo'):
            path_to_file = ''.join(['media/avatar/'])
            f = request.FILES
            for ele in f:
                with open(path_to_file + f[ele].name, 'wb+') as destination:
                    for chunk in f[ele].chunks():
                        destination.write(chunk)
            reopen = open(path_to_file + f[ele].name, 'rb')
            image_file = File(reopen)
            image_file.name = image_file.name[6:]
            MyUser.objects.filter(id=request.POST.get('id_user')).update(image=image_file)
        return HttpResponseRedirect('setting_user')


@login_required
def edit_pass(request, id, error=None):
    user_edit = MyUser.objects.get(id=id)
    return render(request, 'extuser/reset_pass.html', {'user_edit': user_edit, 'error': error})


@login_required
def save_edit_pass(request, id):
    if request.method == 'POST':
        if request.POST.get('new_password1') == request.POST.get('new_password2'):
            user = User.objects.get(id=id)
            user.set_password(request.POST.get('new_password1'))
            user.save()
            RecoveryPass.objects.filter(email=user.email).update(password=request.POST.get('new_password1'))
            return edit_user(request, id)
        return edit_pass(request, id, error=True)


@login_required
def user_list(request):
    exuser = User.objects.filter(is_active=True)
    return render(request, 'extuser/setting_user.html', { 'time': timezone.now(), "exuser": exuser})


@login_required
def delete_user(request):
    if request.user.is_superuser:
        results = request.GET
        result = results.get('id_user')
        inactive_user = User.objects.get(id=int(result))
        inactive_user.is_active = 0
        inactive_user.save() 
        exuser = User.objects.all().filter(is_active=1)
        json = JsonResponse({"del":True, "count_user":len(exuser)})
        return HttpResponse(json)
    else:
        return HttpResponse(JsonResponse({"del":False}))


def send_recavery_pass(request):
    if request.method == 'POST':
        temp_email = get_object_or_404(TemplateEmail, pk=1)
        email_from = is_sender_address_valid(temp_email.sender_address)
        # if request.POST.get('restore_btn') is not None:
        if True:
            emails = RecoveryPass.objects.filter(email=request.POST.get('restore_pass'))
            if emails:
                for email in emails:
                    sending = send_mail("Востановление пароля", email.password, email_from, [email.email], fail_silently=False)
                    if sending:
                        return HttpResponse(content=b'Пароль вислан на Вашу почту')
    return HttpResponse(content=b'Ошибка отсилки')


def is_sender_address_valid(sender_address):
    rieltor_email_setting = get_object_or_404(SettingEmail, id=1)
    EMAIL_HOST_USER = str(rieltor_email_setting.host_user)
    sender_address_is_valid = sender_address.split('@')[-1]
    email_host_is_valid = EMAIL_HOST_USER.split('@')[-1]
    if sender_address_is_valid != email_host_is_valid:
        return EMAIL_HOST_USER
    return sender_address
