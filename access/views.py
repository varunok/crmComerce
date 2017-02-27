# -*- coding: utf-8 -*-


import json
import re

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from facility.models import ContactOwner, UserFullName
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.core import serializers


# Create your views here.
@login_required
def access(request):
    users = User.objects.filter(is_active=True).order_by('id')
    facilitys = ContactOwner.objects.all().filter(trash=False).order_by('id')
    return render(request, 'access/access.html', {"users": users,
                                           "facilitys": facilitys})


@login_required
def change_access_facility(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = UserFullName.objects.get(id=data.get(u'user_pk'))
            if user.is_superuser:
                return HttpResponse(status=300, content='Пользователь superuser')
            facility_id = None
            if data.get('all'):
                facilitys = ContactOwner.objects.all()
                if data.get('selected'):
                    for facility in facilitys:
                        facility.loyality.add(user)
                else:
                    for facility in facilitys:
                        facility.loyality.remove(user)
                facility_id = 'ALL'
            else:
                facility = ContactOwner.objects.get(id=data.get(u'obj_pk'))
                if data.get(u'selected'):
                    facility.loyality.add(user)
                else:
                    facility.loyality.remove(user)
                facility_id = facility.id
            data = JsonResponse({
                'message': u'Доступ изменен',
                'user': str(user),
                'id_facility': facility_id
            })
            return HttpResponse(data)
        except:
            return HttpResponse(status=501)


class AccessMixin(object):
    def serialize_response(self, data, fields=None, *args, **kwargs):
        paginator = ''.join(('{"paginator": "', render_to_string('paginator.html', {'data': data}), '"}'))
        paginator = paginator.replace('\n', '')
        object = serializers.serialize("json", data, fields=fields)
        object = ''.join((object[:-1], ', ', paginator, ']'))
        return object


class AccessListOwnerView(AccessMixin, View):

    def post(self, request, *args, **kwargs):
        facilitys = self.get_queryset()
        return HttpResponse(self.serialize_response(facilitys, fields='id, loyality'))

    def get_queryset(self, **kwargs):
        data = json.loads(self.request.body)
        if data.has_key('id'):
            items = data.get('id')
        else:
            items = 10
        obj = data.get('search')
        if obj:
            owner = self.get_list_obj(obj)
        else:
            owner = ContactOwner.objects.all().filter(trash=False).order_by('id')
        paginator = Paginator(owner, items)
        page = data.get('page')
        try:
            owner = paginator.page(page)
        except PageNotAnInteger:
            owner = paginator.page(1)
        except EmptyPage:
            owner = paginator.page(paginator.num_pages)
        return owner

    def get_list_obj(self, obj):
        print(obj)
        del_null = lambda obj: [x for x in obj if x]
        if ',' in obj:
            obj = del_null(obj.split(','))
            if len(obj) == 1: return self.get_single_obj(obj)
            return ContactOwner.objects.filter(id__in=obj, trash=False).order_by('id')
        elif '-' in obj:
            obj = del_null(obj.split('-'))
            if len(obj) == 1: return self.get_single_obj(obj)
            if len(obj) == 2: obj = range(int(obj[0]), int(obj[1]))
            return ContactOwner.objects.filter(id__in=obj, trash=False).order_by('id')
        elif ':' in obj:
            return self.get_slice(obj)
        else:
            if len([obj]) == 1: return self.get_single_obj(obj)

    def get_single_obj(self, obj):
        if not isinstance(obj, list):
            obj = [obj]
        return [get_object_or_404(ContactOwner, id=obj[0])]

    def get_slice(self, obj):
        del_null = lambda obj: [x for x in obj if x]
        regex = r"(?P<fir>\d*)(?P<gu>[:])(?P<las>\d*)"
        matches = re.finditer(regex, obj)
        for matchNum, match in enumerate(matches):
            obj = match.groups()
        obj = del_null(list(obj))
        if len(obj) == 3:
            return ContactOwner.objects.filter(trash=False).order_by('id')[int(obj[0])-1:int(obj[-1])]
        if obj[0] == ':':
            return ContactOwner.objects.filter(trash=False).order_by('id')[:int(obj[1])+1]
        if obj[-1] == ':':
            return ContactOwner.objects.filter(trash=False).order_by('id')[int(obj[0])-1:]
        else:
            return ContactOwner.objects.filter(id__in=obj, trash=False).order_by('id')



class AccessListUserView(AccessMixin, View):

    def get(self, request, *args, **kwargs):
        users = User.objects.filter(is_active=True).order_by('id')
        return HttpResponse(self.serialize_response(users,
                                                    fields='id, last_name, first_name, is_superuser'))






        # if isinstance(obj, list) and len(obj) == 1:
        #     obj = obj[0]
        # if semi in obj:
        #     obj = obj.split(semi)
        #     obj = [x for x in obj if x]
        #     if len(obj) == 2:
        #         obj = range(int(obj[0]), int(obj[1]) + 1)
        # else:
        #     obj = [obj]
        # return(obj)