# -*- coding: utf-8 -*-


from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core.mail import send_mail
from setting_superadmin.models import AllToConnect
from setting_mail_delivery.models import TemplateEmail, TemplateSms, SettingSMS, SettingEmail
from single_object.models import ContactOwner
from arendator.models import Arendator
from buyer.models import Buyer
from makler.models import Makler
from suds.client import Client
from django.conf import settings
from setting_globall.models import Subscribe
from setting_globall.models import NationalCarrency
from django.contrib.auth.decorators import login_required
# from crm.settings import EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD


EMAIL_HOST_USER = settings.EMAIL_HOST_USER
ALLOWED_HOSTS = settings.ALLOWED_HOSTS[0]


@login_required
def send_email_rieltor(request):
    if request.method == 'POST' and request.is_ajax():
        message = request.POST.get('text')
        temp_email = get_object_or_404(TemplateEmail, pk=1)
        email_to = AllToConnect.objects.filter(pk=1)
        email_from = is_sender_address_valid(temp_email.sender_address)
        subject = "Сообщение из футера"
        sending = send_mail(subject, message, email_from, [email_to[0].email], fail_silently=False)
        return HttpResponse(sending)
    else:
        return HttpResponse(status=500)


@login_required
def send_email_so(request):
    if request.method == 'POST':
        request_abs_url = request.build_absolute_uri('data')
        temp_email = get_object_or_404(TemplateEmail, pk=1)
        single_object = ContactOwner.objects.get(id=request.POST.get('id_so'))
        subs, create = Subscribe.objects.get_or_create(id=1)
        html_message = render_to_string('sender_email/mail.html', {'temp_email': temp_email,
                                                                   'request': request_abs_url,
                                                                   'single_object': single_object,
                                                                   'subs': subs})

        sending = send_mail(temp_email.title, html_message, is_sender_address_valid(temp_email.sender_address),
                            [request.POST.get('email')], [request.POST.get('email')], html_message=html_message)
        if sending:
            return HttpResponse(sending)
        return HttpResponse(status=500)


def is_sender_address_valid(sender_address):
    sender_address_valid = str(sender_address).split('@')[-1]
    validation_email = EMAIL_HOST_USER.split('@')[-1]
    if sender_address_valid != validation_email:
        return ' '
    return '%s' % sender_address


@login_required
def delivery_email_arendator(request):
    if request.method == 'POST':
        plus_email = request.POST.get('plus_email')
        request_abs_url = request.build_absolute_uri('data')
        temp_email = get_object_or_404(TemplateEmail, pk=1)
        single_object = ContactOwner.objects.get(id=request.POST.get('id_so'))
        subs, create = Subscribe.objects.get_or_create(id=1)
        html_message = render_to_string('sender_email/mail.html', {'temp_email': temp_email,
                                                                   'request': request_abs_url,
                                                                   'single_object': single_object,
                                                                   'subs': subs})
        try:
            arendator_emails = Arendator.objects.filter(id__in=request.POST.getlist('id_a')[0].split(',')).values_list('email', flat=True)
            arendator_emails = [i for i in arendator_emails if i != '']
        except:
            arendator_emails = []
        if plus_email:
            if plus_email not in arendator_emails:
                arendator_emails.append(plus_email)
        count_sending = 0
        for arendator_email in arendator_emails:
            sending = send_mail(temp_email.title, html_message, is_sender_address_valid(temp_email.sender_address),
                                [arendator_email], [arendator_email], html_message=html_message)
            if sending:
                count_sending += 1
        if count_sending:
            return HttpResponse(count_sending)
    return HttpResponse(status=500)


@login_required
def delivery_email_arendator_single(request):
    if request.method == 'POST':
        plus_email = request.POST.get('plus_email')
        temp_email = get_object_or_404(TemplateEmail, pk=1)
        request_abs_url = request.build_absolute_uri('data')
        request_abs_url = request_abs_url.replace('arendators', 'objects')
        print(request_abs_url)
        # print(request.POST.getlist('id_obj')[0].split(','))
        subs, create = Subscribe.objects.get_or_create(id=1)
        objects = ContactOwner.objects.filter(id__in=request.POST.getlist('id_obj')[0].split(','))
        html_message = render_to_string('sender_email/list_mail.html', {'temp_email': temp_email,
                                                                        'request': request_abs_url,
                                                                        'objects': objects,
                                                                        'subs': subs})
        arendator = Arendator.objects.get(id=request.POST.get('id_a'))

        sending = send_mail(temp_email.title, html_message, is_sender_address_valid(temp_email.sender_address),
                            [arendator.email], [arendator.email], html_message=html_message)
        if sending:
            return HttpResponse(sending)
        if plus_email:
            if str(plus_email) != str(arendator.email):
                sending = send_mail(temp_email.title, html_message, is_sender_address_valid(temp_email.sender_address),
                                    [plus_email], [plus_email], html_message=html_message)
                if sending:
                    return HttpResponse(sending)
        return HttpResponse(status=500)


@login_required
def delivery_email_buyer_single(request):
    if request.method == 'POST':
        plus_email = request.POST.get('plus_email')
        temp_email = get_object_or_404(TemplateEmail, pk=1)
        request_abs_url = request.build_absolute_uri('data')
        request_abs_url = request.build_absolute_uri('data')
        request_abs_url = request_abs_url.replace('buyers', 'objects')
        # print(request.POST.getlist('id_obj')[0].split(','))
        subs, create = Subscribe.objects.get_or_create(id=1)
        objects = ContactOwner.objects.filter(id__in=request.POST.getlist('id_obj')[0].split(','))
        html_message = render_to_string('sender_email/list_mail.html', {'temp_email': temp_email,
                                                                        'request': request_abs_url,
                                                                        'objects': objects,
                                                                        'subs': subs})
        buyer = Buyer.objects.get(id=request.POST.get('id_b'))

        sending = send_mail(temp_email.title, html_message, is_sender_address_valid(temp_email.sender_address),
                            [buyer.email], [buyer.email], html_message=html_message)
        if sending:
            return HttpResponse(sending)
        if plus_email:
            if str(plus_email) != str(buyer.email):
                sending = send_mail(temp_email.title, html_message, is_sender_address_valid(temp_email.sender_address),
                                    [plus_email], [plus_email], html_message=html_message)
                if sending:
                    return HttpResponse(sending)
        return HttpResponse(status=500)


@login_required
def delivery_email_buyer(request):
    if request.method == 'POST':
        plus_email = request.POST.get('plus_email')
        request_abs_url = request.build_absolute_uri('data')
        temp_email = get_object_or_404(TemplateEmail, pk=1)
        single_object = ContactOwner.objects.get(id=request.POST.get('id_so'))
        subs, create = Subscribe.objects.get_or_create(id=1)
        html_message = render_to_string('sender_email/mail.html', {'temp_email': temp_email,
                                                                   'request': request_abs_url,
                                                                   'single_object': single_object,
                                                                   'subs': subs})
        try:
            buyer_emails = Buyer.objects.filter(id__in=request.POST.getlist('id_b')[0].split(',')).values_list('email', flat=True)
            buyer_emails = [i for i in buyer_emails if i != '']
        except:
            buyer_emails = []
        if plus_email:
            buyer_emails.append(plus_email)
        count_sending = 0
        for buyer_email in buyer_emails:
            sending = send_mail(temp_email.title, html_message, is_sender_address_valid(temp_email.sender_address),
                                [buyer_email], [buyer_email], html_message=html_message)
            if sending:
                count_sending += 1
        if count_sending:
            return HttpResponse(count_sending)
    return HttpResponse(status=500)


@login_required
def send_email_makler(request):
    if request.method == 'POST':
        emails = Makler.objects.values_list('email', flat=True)
        emails = [i for i in emails if i != '']
        count_sending_email = 0
        for email in emails:
            sending = send_mail(request.POST.get('subject'), request.POST.get('body'),
                                is_sender_address_valid(EMAIL_HOST_USER),
                                [email], [])
            if sending:
                count_sending_email += 1
        if count_sending_email:
            return HttpResponse(count_sending_email)
    return HttpResponse(status=500)


@login_required
def delivery_sms_arendator(request):
    """# Auth(xs:string login, xs:string password, )
       # GetCreditBalance()
       # GetMessageStatus(xs:string MessageId, )
       # GetNewMessages()
       # SendSMS(xs:string sender, xs:string destination, xs:string text, xs:string wappush, )
    """
    if request.method == 'POST':
        plus_phone = request.POST.get('plus_phone')
        single_object = ContactOwner.objects.get(id=request.POST.get('id_so'))
        setting_sms = get_object_or_404(SettingSMS, id=1)
        try:
            arendator_phone = Arendator.objects.filter(id__in=request.POST.getlist('id_a')[0].split(',')).values_list('phone_first', flat=True)
        except:
            arendator_phone = []
        if plus_phone:
            arendator_phone.append(plus_phone)
        client = Client('http://turbosms.in.ua/api/wsdl.html')
        # auth = client.service.Auth(login='crm', password='sin1984')
        auth = client.service.Auth(login=setting_sms.login, password=setting_sms.password)
        count_message = 0
        if auth == u'Вы успешно авторизировались':
            balance = client.service.GetCreditBalance()
            if float(balance):
                result = client.service.SendSMS(sender=setting_sms.sender,
                                                destination=list_phone_validate(arendator_phone),
                                                text=link_to_single_obj(single_object, 'arendator'))
                for i in result['ResultArray'][1:]:
                    status = client.service.GetMessageStatus(MessageId=i)
                    if status == u'Отправлено':
                        count_message += 1
                return HttpResponse(count_message)
            else:
                balance = u'Ваш баланс ' + balance
                return HttpResponse(balance, status=500)
        else:
            return HttpResponse(auth, status=500)
    else:
        return HttpResponse(status=500)


@login_required
def delivery_sms_arendator_single(request):
    if request.method == 'POST':
        plus_phone = request.POST.get('plus_phone')
        try:
            objects = ContactOwner.objects.filter(id__in=request.POST.getlist('id_obj')[0].split(','))
        except:
            return HttpResponse('Не вибрано обектов для рассилки', status=500)
        setting_sms = get_object_or_404(SettingSMS, id=1)
        try:
            arendator = Arendator.objects.get(id=request.POST.get('id_a'))
            phone_list = [str(arendator.phone_first)]
        except:
            phone_list = []
        if plus_phone:
            if not str(plus_phone) in phone_list:
                phone_list.append(plus_phone)
        client = Client('http://turbosms.in.ua/api/wsdl.html')
        auth = client.service.Auth(login=setting_sms.login, password=setting_sms.password)
        count_message = 0
        if auth == u'Вы успешно авторизировались':
            balance = client.service.GetCreditBalance()
            if float(balance):
                result = client.service.SendSMS(sender=setting_sms.sender,
                                                destination=list_phone_validate(phone_list),
                                                text=link_to_obj(objects, 'arendator'))
                for i in result['ResultArray'][1:]:
                    status = client.service.GetMessageStatus(MessageId=i)
                    if status == u'Отправлено':
                        count_message += 1
                return HttpResponse(count_message)
            else:
                balance = u'Ваш баланс ' + balance
                return HttpResponse(balance, status=500)
        else:
            return HttpResponse(auth, status=500)
    else:
        return HttpResponse(status=500)


@login_required
def delivery_sms_buyer_single(request):
    if request.method == 'POST':
        plus_phone = request.POST.get('plus_phone')
        try:
            objects = ContactOwner.objects.filter(id__in=request.POST.getlist('id_obj')[0].split(','))
        except:
            return HttpResponse('Не вибрано обектов для рассилки', status=500)
        setting_sms = get_object_or_404(SettingSMS, id=1)
        try:
            buyer = Buyer.objects.get(id=request.POST.get('id_b'))
            phone_list = [str(buyer.phone_first)]
        except:
            phone_list = []
        if plus_phone:
            if not str(plus_phone) in phone_list:
                phone_list.append(plus_phone)
        client = Client('http://turbosms.in.ua/api/wsdl.html')
        auth = client.service.Auth(login=setting_sms.login, password=setting_sms.password)
        count_message = 0
        if auth == u'Вы успешно авторизировались':
            balance = client.service.GetCreditBalance()
            if float(balance):
                result = client.service.SendSMS(sender=setting_sms.sender,
                                                destination=list_phone_validate(phone_list),
                                                text=link_to_obj(objects, 'buyer'))
                for i in result['ResultArray'][1:]:
                    status = client.service.GetMessageStatus(MessageId=i)
                    if status == u'Отправлено':
                        count_message += 1
                return HttpResponse(count_message)
            else:
                balance = u'Ваш баланс ' + balance
                return HttpResponse(balance, status=500)
        else:
            return HttpResponse(auth, status=500)
    else:
        return HttpResponse(status=500)


@login_required
def delivery_sms_buyer(request):
    """# Auth(xs:string login, xs:string password, )
       # GetCreditBalance()
       # GetMessageStatus(xs:string MessageId, )
       # GetNewMessages()
       # SendSMS(xs:string sender, xs:string destination, xs:string text, xs:string wappush, )
    """
    if request.method == 'POST':
        plus_phone = request.POST.get('plus_phone')
        single_object = ContactOwner.objects.get(id=request.POST.get('id_so'))
        setting_sms = get_object_or_404(SettingSMS, id=1)
        try:
            buyer_phone = Buyer.objects.filter(id__in=request.POST.getlist('id_b')[0].split(',')).values_list('phone_first', flat=True)
        except:
            buyer_phone = []
        if plus_phone:
            buyer_phone.append(plus_phone)
        client = Client('http://turbosms.in.ua/api/wsdl.html')
        # auth = client.service.Auth(login='crm', password='sin1984')
        auth = client.service.Auth(login=setting_sms.login, password=setting_sms.password)
        count_message = 0
        if auth == u'Вы успешно авторизировались':
            balance = client.service.GetCreditBalance()
            if float(balance):
                result = client.service.SendSMS(sender=setting_sms.sender,
                                                destination=list_phone_validate(buyer_phone),
                                                text=link_to_single_obj(single_object, 'buyer'))
                for i in result['ResultArray'][1:]:
                    status = client.service.GetMessageStatus(MessageId=i)
                    if status == u'Отправлено':
                        count_message += 1
                return HttpResponse(count_message)
            else:
                balance = u'Ваш баланс ' + balance
                return HttpResponse(balance, status=500)
        else:
            return HttpResponse(auth, status=500)
    else:
        return HttpResponse(status=500)


def list_phone_validate(list_phone):
    list_phone = [str(i) for i in list(list_phone)]
    new_list_phone = []
    for phone in list_phone:
        if len(phone) == 12 and int(phone[0]) == 3:
            new_list_phone.append(''.join(['+', phone]))
        elif len(phone) == 11 and int(phone[0]) == 8:
            new_list_phone.append(''.join(['+3', phone]))
        elif len(phone) == 10 and int(phone[0]) == 0:
            new_list_phone.append(''.join(['+38', phone]))
        elif len(phone) == 9:
            new_list_phone.append(''.join(['+380', phone]))
    del list_phone
    return ','.join(new_list_phone)


def link_to_single_obj(single_object, type_kontragent):
    templ_sms = get_object_or_404(TemplateSms, id=1)
    address = single_object.street_obj
    if type_kontragent == 'arendator':
        try:
            nat_curr = NationalCarrency.objects.get(id=1)
        except:
            nat_curr = ''
        price = str(single_object.price_month) + nat_curr.currency
    elif type_kontragent == 'buyer':
        price = str(single_object.price_bay)+'$'
    link = ''.join([ALLOWED_HOSTS, '/objects/data/', str(single_object.id)])
    landmark = single_object.landmark
    link = ', '.join([templ_sms.title, templ_sms.text, landmark, unicode(address),
                     price, link, templ_sms.signature])
    return link


def link_to_obj(objects, type_kontragent):
    templ_sms = get_object_or_404(TemplateSms, id=1)
    list_obj = []
    for single_object in objects:
        address = single_object.street_obj
        if type_kontragent == 'arendator':
            try:
                nat_curr = NationalCarrency.objects.get(id=1)
            except:
                nat_curr = ''
            price = str(single_object.price_month) + nat_curr.currency
        elif type_kontragent == 'buyer':
            price = str(single_object.price_bay)+'$'
        link = ''.join([ALLOWED_HOSTS, '/objects/data/', str(single_object.id)])
        landmark = single_object.landmark
        link = ', '.join([templ_sms.title, templ_sms.text, landmark, unicode(address),
                          price, link, templ_sms.signature])
        list_obj.append(link)
    return ', '.join(list_obj)
