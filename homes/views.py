# -*- coding: utf-8 -*-


import uuid
import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone, dateformat
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from notes.models import Notes
from setting_street.models import Street, District, Subway
from facility.forms import AddressFacilityForm
from arendator.forms import ArendatorForm
from buyer.forms import BuyerForm
from arendator.models import Arendator, TypeState, TypeClient, TypeStage
from buyer.models import Buyer
from facility.models import AddressFacilityData, ContactOwner, ImagesFacility, TypeFacility, \
    TypeActuality, TypeCondition, TypeRepairs, TypeHeating, TypeLocations, TypeStoreys, TypeEntrance, \
    TypeDocumentation, TypeUnderThat, TypeAvailability
from setting_globall.models import NationalCarrency
from search_home import searh
from extuser.models import MyUser
from makler.models import Makler, TypeCooperations
from tasking.models import Tasking, UserFullName, TypeComplexity
from meeting.models import Meeting, TypeStatus


DAY_AGO = timezone.now() - datetime.timedelta(days=int(30))


# Create your views here.
@login_required
def homes(request):
    data = default_show_activity_index()
    list_user = UserFullName.objects.all()
    notes = Notes.objects.all()
    meeting_list = Meeting.objects.filter(meet_trash=False, meet_archiv=False).order_by('meet_date')[0:5]
    tasking = Tasking.objects.filter(task_trash=False, task_archiv=False).order_by('dead_line')[0:5]
    return render(request, 'homes/index.html', {'notes': notes, 'time': timezone.now(),
                                                'tasking': tasking,
                                                'meeting_list': meeting_list,
                                                'list_user': list_user,
                                                'arendators': data.get('arendators'),
                                                'buyers': data.get('buyers'),
                                                'facilitys': data.get('facilitys'),
                                                'maklers': data.get('maklers'),
                                                'taskings': data.get('taskings'),
                                                'meetings': data.get('meetings')})


def default_show_activity_index(dateto=DAY_AGO, datefrom=datetime.date(2100, 1, 1)):
    arendators = Arendator.objects.filter(add_date__range=(dateto, datefrom), trash=False).count()
    buyers = Buyer.objects.filter(add_date__range=(dateto, datefrom), trash=False).count()
    facilitys = ContactOwner.objects.filter(date_added__range=(dateto, datefrom), trash=False).count()
    maklers = Makler.objects.filter(add_date__range=(dateto, datefrom)).count()
    taskings = Tasking.objects.filter(add_date__range=(dateto, datefrom), task_trash=False).count()
    meetings = Meeting.objects.filter(add_date__range=(dateto, datefrom), meet_trash=False).count()
    data = {
        'arendators': arendators,
        'buyers': buyers,
        'facilitys': facilitys,
        'maklers': maklers,
        'taskings': taskings,
        'meetings': meetings,
    }
    return data


@login_required
def show_activity_index(request):
    dateto = datetime.date(2000, 1, 1)
    datefrom = datetime.date(2100, 1, 1)
    if request.GET.get('dateto'):
        dateto = request.GET.get('dateto')
    if request.GET.get('datefrom'):
        datefrom = request.GET.get('datefrom')
    if int(request.GET.get('user_id')):
        arendators = Arendator.objects.filter(rieltor=request.GET.get('user_id'), add_date__range=(dateto, datefrom),
                                              trash=False).count()
        buyers = Buyer.objects.filter(rieltor=request.GET.get('user_id'), add_date__range=(dateto, datefrom),
                                      trash=False).count()
        facilitys = ContactOwner.objects.filter(rieltor=request.GET.get('user_id'),
                                                date_added__range=(dateto, datefrom),
                                                trash=False).count()
        maklers = Makler.objects.filter(rieltor=request.GET.get('user_id'), add_date__range=(dateto, datefrom)).count()
        taskings = Tasking.objects.filter(rieltor=request.GET.get('user_id'), add_date__range=(dateto, datefrom),
                                          task_trash=False).count()
        meetings = Meeting.objects.filter(rieltor=request.GET.get('user_id'), add_date__range=(dateto, datefrom),
                                          meet_trash=False).count()
        data = {
            'arendators': arendators,
            'buyers': buyers,
            'facilitys': facilitys,
            'maklers': maklers,
            'taskings': taskings,
            'meetings': meetings,
        }
        data = JsonResponse(data, safe=True)
        return HttpResponse(data)
    else:
        data = default_show_activity_index(dateto, datefrom)
        data = JsonResponse(data, safe=True)
        return HttpResponse(data)


class ObjectList(ListView):
    """docstring for ObjectList"""
    model = ContactOwner
    paginate_by = 10
    context_object_name = 'contact_owner'
    template_name = 'homes/objects.html'
    qeryset = ContactOwner.objects.all().filter(trash=False).order_by('-id')

    def get_context_data(self, **kwargs):
        self.context = super(ObjectList, self).get_context_data(**kwargs)
        self.context['time'] = timezone.now()
        self.context['images'] = ImagesFacility.objects.all()
        self.context['addres_facility_data_list'] = AddressFacilityData.objects.all()
        self.context['nac_carrency'] = NationalCarrency.objects.filter(id=1)[0]
        self.context['all_contact_owner_se'] = ContactOwner.objects.filter(list_operations__in=[1, 4], trash=False)
        self.context['all_contact_owner_ad'] = ContactOwner.objects.filter(list_operations__in=[2, 3], trash=False)
        self.context['all_contact_owner'] = ContactOwner.objects.all().filter(trash=False)
        self.context['type_facility'] = TypeFacility.objects.all()
        self.context['list_carrency'] = NationalCarrency.objects.all()
        self.context['type_actuality'] = TypeActuality.objects.all()
        self.context['list_district'] = District.objects.all()
        self.context['list_street'] = Street.objects.all()
        self.context['list_subway'] = Subway.objects.all()
        self.context['list_conditions'] = TypeCondition.objects.all()
        self.context['list_location'] = TypeLocations.objects.all()
        self.context['list_repairs'] = TypeRepairs.objects.all()
        self.context['list_storeys'] = TypeStoreys.objects.all()
        self.context['list_entrance'] = TypeEntrance.objects.all()
        self.context['list_documentation'] = TypeDocumentation.objects.all()
        self.context['list_under_that'] = TypeUnderThat.objects.all()
        self.context['list_availability'] = TypeAvailability.objects.all()
        self.context['type_heating'] = TypeHeating.objects.all()
        self.context['users'] = UserFullName.objects.filter(is_active=True)
        return self.context

    def get_queryset(self):
        order_by = self.request.GET.get('order_by', '')
        if order_by in ('id', 'price_bay', 'price_month', 'total_area', 'date_of_renovation', 'review_date'):
            self.qeryset = self.qeryset.order_by(order_by)
        if self.request.GET.get('reverse', '') == '1':
            self.qeryset = self.qeryset.reverse()
        return self.qeryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ObjectList, self).dispatch(request, *args, **kwargs)


class ObjectListSearch(ObjectList):
    """docstring for ObjectListSearch"""
    template_name = "homes/search.html"

    def get_context_data(self, **kwargs):
        self.context = super(ObjectListSearch, self).get_context_data(**kwargs)
        self.context['all_contact_owner_se'] = self.object_list.filter(list_operations__in=[1, 4], trash=False)
        self.context['all_contact_owner_ad'] = self.object_list.filter(list_operations__in=[2, 3], trash=False)
        self.context['all_contact_owner'] = self.object_list
        return self.context

    def get_queryset(self):
        return searh(self.request)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ObjectListSearch, self).dispatch(request, *args, **kwargs)


class ObjectListSelling(ObjectList):
    qeryset = ContactOwner.objects.filter(list_operations__in=[1, 4], trash=False).order_by('-id')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ObjectListSelling, self).dispatch(request, *args, **kwargs)


class ObjectListArend(ObjectList):
    qeryset = ContactOwner.objects.filter(list_operations__in=[2, 3], trash=False).order_by('-id')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ObjectListArend, self).dispatch(request, *args, **kwargs)


@login_required
def add_object(request, form=AddressFacilityForm()):
    form.fields['rieltor'].queryset = UserFullName.objects.filter(is_active=True)
    form.fields['loyality'].queryset = UserFullName.objects.filter(is_active=True)
    street_list = Street.objects.all()
    district_list = District.objects.all()
    subway_list = Subway.objects.all()
    request.session['dir_img'] = str(uuid.uuid1())
    return render(request,
                  'homes/add_object.html', {'form': form,
                                            'street_list': street_list,
                                            'district_list': district_list,
                                            'subway_list': subway_list,
                                            'time': timezone.now()})


@login_required
def buyers_list(request):
    return render(request, 'homes/buyers.html', {'time': timezone.now()})


class MaklerList(ListView):
    model = Makler
    paginate_by = 10
    context_object_name = 'maklers'
    template_name = 'homes/maklers.html'
    ordering = ['id']
    # qeryset = Makler.objects.all()

    def get_context_data(self, **kwargs):
        self.context = super(MaklerList, self).get_context_data(**kwargs)
        self.context['time'] = timezone.now()
        self.context['count_makler'] = Makler.objects.all().count()
        self.context['count_makler_white'] = Makler.objects.filter(white_black=1).count()
        self.context['count_makler_black'] = Makler.objects.filter(white_black=2).count()
        self.context['list_cooperation'] = TypeCooperations.objects.all()
        return self.context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(MaklerList, self).dispatch(request, *args, **kwargs)


class ArendatorsList(ListView):
    """docstring for ObjectList"""
    model = Arendator
    paginate_by = 10
    context_object_name = 'arendator_list'
    template_name = 'homes/arendators.html'
    queryset = Arendator.objects.all().filter(trash=False)

    def get_context_data(self, **kwargs):
        self.context = super(ArendatorsList, self).get_context_data(**kwargs)
        self.context['time'] = timezone.now()
        self.context['nac_carrency'] = NationalCarrency.objects.filter(id=1)[0]
        self.context['count_arendator'] = len(Arendator.objects.all().filter(trash=False))
        self.context['user_list'] = MyUser.objects.all()
        self.context['list_district'] = District.objects.all()
        self.context['list_state'] = TypeState.objects.all()
        self.context['type_facility'] = TypeFacility.objects.all()
        self.context['list_storeys'] = TypeStoreys.objects.all()
        self.context['list_under_that'] = TypeUnderThat.objects.all()
        self.context['list_entrance'] = TypeEntrance.objects.all()
        self.context['list_location'] = TypeLocations.objects.all()
        # self.context['list_rooms'] = TypeRooms.objects.all()
        self.context['list_client'] = TypeClient.objects.all()
        self.context['list_stage'] = TypeStage.objects.all()
        self.context['list_repair'] = TypeRepairs.objects.all()
        # self.context['list_number_of_persons'] = TypeNumberOfPerson.objects.all()

        return self.context

    def get_queryset(self):
        order_by = self.request.GET.get('order_by', '')
        if order_by in ('id', 'call_date', 'review_date'):
            self.queryset = self.queryset.order_by(order_by)
        if self.request.GET.get('reverse', '') == '1':
            self.queryset = self.queryset.reverse()
        return self.queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ArendatorsList, self).dispatch(request, *args, **kwargs)


@login_required
def add_arendator(request, form=ArendatorForm()):
    form.fields['rieltor'].queryset = UserFullName.objects.filter(is_active=True)
    form.fields['loyality'].queryset = UserFullName.objects.filter(is_active=True)
    return render(request, 'homes/add_arendator.html', {'time': timezone.now(),
                                                        'form': form})


class BuyersList(ListView):
    """docstring for ObjectList"""
    model = Buyer
    paginate_by = 10
    context_object_name = 'buyer_list'
    template_name = 'homes/buyers.html'
    queryset = Buyer.objects.all().filter(trash=False)

    def get_context_data(self, **kwargs):
        self.context = super(BuyersList, self).get_context_data(**kwargs)
        self.context['time'] = timezone.now()
        self.context['nac_carrency'] = NationalCarrency.objects.filter(id=1)[0]
        self.context['count_buyer'] = Buyer.objects.all().filter(trash=False).count()
        self.context['user_list'] = MyUser.objects.all()
        self.context['list_district'] = District.objects.all()
        self.context['list_state'] = TypeState.objects.all()
        self.context['type_facility'] = TypeFacility.objects.all()
        self.context['list_storeys'] = TypeStoreys.objects.all()
        self.context['list_under_that'] = TypeUnderThat.objects.all()
        self.context['list_entrance'] = TypeEntrance.objects.all()
        self.context['list_location'] = TypeLocations.objects.all()
        # self.context['list_rooms'] = TypeRooms.objects.all()
        self.context['list_client'] = TypeClient.objects.all()
        self.context['list_stage'] = TypeStage.objects.all()
        self.context['list_repair'] = TypeRepairs.objects.all()
        # self.context['list_number_of_persons'] = TypeNumberOfPerson.objects.all()
        return self.context

    def get_queryset(self):
        order_by = self.request.GET.get('order_by', '')
        if order_by in ('id', 'call_date', 'review_date'):
            self.queryset = self.queryset.order_by(order_by)
        if self.request.GET.get('reverse', '') == '1':
            self.queryset = self.queryset.reverse()
        return self.queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BuyersList, self).dispatch(request, *args, **kwargs)


@login_required
def add_buyer(request, form=BuyerForm()):
    form.fields['rieltor'].queryset = UserFullName.objects.filter(is_active=True)
    form.fields['loyality'].queryset = UserFullName.objects.filter(is_active=True)
    return render(request, 'homes/add_buyer.html', {'time': timezone.now(),
                                                    'form': form})


class TaskingList(ListView):
    model = Tasking
    paginate_by = 10
    context_object_name = 'tasking_list'
    template_name = 'homes/tasking.html'
    queryset = Tasking.objects.filter(task_trash=False, task_archiv=False)

    def get_context_data(self, **kwargs):
        self.context = super(TaskingList, self).get_context_data(**kwargs)
        self.context['time'] = timezone.now()
        self.context['count_active_task'] = Tasking.objects.filter(task_trash=False, task_archiv=False).count()
        self.context['count_archive_task'] = Tasking.objects.filter(task_trash=False, task_archiv=True).count()
        self.context['rieltor_list'] = UserFullName.objects.filter(is_active=True)
        self.context['complexity_list'] = TypeComplexity.objects.all()
        return self.context

    # def get_queryset(self):
    #     self.queryset = Tasking.objects.filter(task_trash=False, task_archiv=False, access=self.request.user.id)
    #     return self.queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TaskingList, self).dispatch(request, *args, **kwargs)


class TaskingListArchive(TaskingList):
    queryset = Tasking.objects.filter(task_trash=False, task_archiv=True)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TaskingListArchive, self).dispatch(request, *args, **kwargs)


@login_required
def setting(request):
    return render(request, 'homes/setting.html', {'time': timezone.now()})


class MeetingList(ListView):
    model = Meeting
    paginate_by = 10
    context_object_name = 'meeting_list'
    template_name = 'homes/meeting.html'
    queryset = Meeting.objects.filter(meet_trash=False, meet_archiv=False)

    def get_context_data(self, **kwargs):
        self.context = super(MeetingList, self).get_context_data(**kwargs)
        self.context['time'] = timezone.now()
        self.context['count_active_meet'] = Meeting.objects.filter(meet_trash=False, meet_archiv=False).count()
        self.context['count_archive_meet'] = Meeting.objects.filter(meet_trash=False, meet_archiv=True).count()
        self.context['rieltor_list'] = UserFullName.objects.filter(is_active=True)
        self.context['status_list'] = TypeStatus.objects.all()
        return self.context

    # def get_queryset(self):
    #     self.queryset = Meeting.objects.filter(task_trash=False, task_archiv=False, access=self.request.user.id)
    #     return self.queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(MeetingList, self).dispatch(request, *args, **kwargs)


class MeetingListArchive(MeetingList):
    queryset = Meeting.objects.filter(meet_trash=False, meet_archiv=True)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(MeetingListArchive, self).dispatch(request, *args, **kwargs)


# @login_required
# def meeting(request):
#     return render(request, 'homes/meeting.html', {'time': timezone.now()})
