# -*- coding: utf-8 -*-


# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.utils import timezone, dateformat
from django.contrib.auth.models import User
from django.views.generic import DetailView
from buyer.models import Buyer, TypeState
from facility.models import NationalCarrency
from extuser.models import MyUser
from single_buyer.models import SingleBuyerComments
from single_object.models import TieBuyer as Tie, TypeShows, ShowsBuyer
from search_automat import search_automat
from facility.models import ContactOwner, TypeOperations
from meeting.models import Meeting
from tasking.models import Tasking
from homes.views import TaskingList, MeetingList
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class SingleBuyerView(DetailView):
    """docstring for SingleObjectView"""
    model = Buyer
    slug_url_kwarg = 'aid'
    slug_field = 'id'
    template_name = 'single_buyer/single_buyer.html'
    context_object_name = 'single_buyer'

    def get_context_data(self, **kwargs):
        self.context = super(SingleBuyerView, self).get_context_data(**kwargs)
        self.context['nac_carrency'] = NationalCarrency.objects.get(id=1)
        self.context['list_state'] = TypeState.objects.all()
        self.context['single_obj_comments'] = SingleBuyerComments.objects.filter(
            obj_comments=self.context['single_buyer'].id, type_tabs='comments')
        self.context['count_meet'] = Meeting.objects.filter(meet_trash=False, meet_buyer=self.context['single_buyer'].id).count()
        self.context['count_task'] = Tasking.objects.filter(task_trash=False, task_buyer=self.context['single_buyer'].id).count()
        return self.context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(SingleBuyerView, self).dispatch(request, *args, **kwargs)


# START BLOCK COMMENTS
@login_required
def get_comment_buyer(request):
    data_comment = SingleBuyerComments.objects.filter(obj_comments=request.GET['id_buyer']).order_by('-date_comment')
    return render(request, 'single_object/comments.html', {"single_obj_comments": data_comment})


@login_required
def add_single_buyer_comment(request):
    author = User.objects.get(id=request.POST['id_user'])
    author_name = author.get_full_name()
    singl_obj = Buyer.objects.get(id=request.POST['id_single_obj'])
    image = MyUser.objects.get(user=author)
    comment = SingleBuyerComments(obj_comments=singl_obj,
                                  comment=unicode(request.POST['text_comment']),
                                  author_comment=unicode(author_name),
                                  image=unicode(image.image),
                                  type_tabs=request.POST['type_tabs'])
    comment.save()
    comments = SingleBuyerComments.objects.filter(obj_comments=singl_obj).last()
    date_comment = dateformat.format(comments.date_comment, 'd E Y H:i')
    comment_data = JsonResponse({
        "text": comments.comment,
        "author": comments.author_comment,
        "date": date_comment,
        "image": str(image.image),
        "id_comment": comments.id
    })
    return HttpResponse(comment_data)


@login_required
def del_comment(request):
    if request.method == 'POST':
        id_comment = request.POST.get('id_comment').split('_')[-1]
        SingleBuyerComments.objects.get(id=id_comment).delete()
        return HttpResponse('comment delete')
    else:
        return HttpResponse('error delete')

# END BLOCK COMMENTS


# START BLOCK PICK UP AN OBJECT
@login_required
def get_object_buyer(request):
    ties = Tie.objects.all()
    shows = TypeShows.objects.all()
    id_show = ShowsBuyer.objects.all()
    single_obj_comments = SingleBuyerComments.objects.filter(obj_comments=request.GET.get('id_buyer')).order_by('-date_comment')
    return render(request, 'single_buyer/get_objects.html', {'ties': ties,
                                                             'id_buyer': request.GET.get('id_buyer'),
                                                             'shows': shows,
                                                             'id_show': id_show,
                                                             'single_obj_comments': single_obj_comments})


@login_required
def automat_tie_buyer(request):
    list_operations = TypeOperations.objects.filter(type_operations__in=['Обмен', 'Продажа'])
    qeryset = ContactOwner.objects.all().filter(trash=False, list_operations__in=list_operations)
    print(search_automat(request.GET, qeryset))
    ties = Tie.objects.all()
    shows = TypeShows.objects.all()
    id_show = ShowsBuyer.objects.all()
    single_obj_comments = SingleBuyerComments.objects.filter(obj_comments=request.GET.get('id_buyer')).order_by('-date_comment')
    return render(request, 'single_buyer/get_objects.html', {'ties': ties,
                                                             'id_buyer': request.GET.get('id_buyer'),
                                                             'shows': shows,
                                                             'id_show': id_show,
                                                             'single_obj_comments': single_obj_comments})


@login_required
def add_id_cont_owner(request):
    if ContactOwner.objects.filter(id=request.GET.get('id_cont_owner')).exists():
        cont_owner = ContactOwner.objects.get(id=request.GET.get('id_cont_owner'))
        if cont_owner.trash:
            return HttpResponse(status=404, content=b'Обект в корзине')
    else:
        return HttpResponse(status=404, content=b'Обекта не существует')
    buyer = Buyer.objects.get(id=request.GET.get('id_buyer'))
    tie, created = Tie.objects.get_or_create(tie_cont_owner=cont_owner)
    if not Tie.objects.filter(tie_buye=buyer, tie_cont_owner=cont_owner).exists():
        tie.tie_buye.add(buyer)
    else:
        return HttpResponse(status=404, content=b'Обект уже в списке')
    ties = Tie.objects.all()
    shows = TypeShows.objects.all()
    id_show = ShowsBuyer.objects.all()
    single_obj_comments = SingleBuyerComments.objects.filter(obj_comments=request.GET.get('id_buyer')).order_by('-date_comment')
    return render(request, 'single_buyer/get_objects.html', {'ties': ties,
                                                             'id_buyer': request.GET.get('id_buyer'),
                                                             'shows': shows,
                                                             'id_show': id_show,
                                                             'single_obj_comments': single_obj_comments})


@login_required
def clear_cont_owner(request):
    if request.method == 'POST':
        try:
            tie_c = Tie.objects.filter(tie_buye=request.POST.get('id_buyer'))
            for t in tie_c:
                t.tie_buye.clear()
        except Tie.DoesNotExist:
            pass
        ties = Tie.objects.all()
        shows = TypeShows.objects.all()
        id_show = ShowsBuyer.objects.all()
        single_obj_comments = SingleBuyerComments.objects.filter(
            obj_comments=request.POST.get('id_buyer')).order_by('-date_comment')
        return render(request, 'single_buyer/get_objects.html', {'ties': ties,
                                                                 'id_buyer': request.POST.get('id_buyer'),
                                                                 'shows': shows,
                                                                 'id_show': id_show,
                                                                 'single_obj_comments': single_obj_comments})


@login_required
def del_cont_owner(request):
    if request.method == 'POST':
        tie = Tie.objects.get(tie_cont_owner=request.POST.get('id_cont_owner'))
        arend = tie.tie_buye.get(id=request.POST.get('id_buyer'))
        tie.tie_buye.remove(arend)
        ties = Tie.objects.all()
        shows = TypeShows.objects.all()
        id_show = ShowsBuyer.objects.all()
        single_obj_comments = SingleBuyerComments.objects.filter(
            obj_comments=request.POST.get('id_buyer')).order_by('-date_comment')
        return render(request, 'single_buyer/get_objects.html', {'ties': ties,
                                                                 'id_buyer': request.POST.get('id_buyer'),
                                                                 'shows': shows,
                                                                 'id_show': id_show,
                                                                 'single_obj_comments': single_obj_comments})


@login_required
def change_show_owner(request):
    if request.method == 'POST':
        cont_owner = ContactOwner.objects.get(id=request.POST.get('id_cont_owner'))
        buyer = Buyer.objects.get(id=request.POST.get('id_buyer'))
        try:
            show = TypeShows.objects.get(id=request.POST.get('show'))
            new_show, created = ShowsBuyer.objects.get_or_create(array_buyer=buyer, array_cont_ower=cont_owner)
            new_show.type_shows_buyer = show
            new_show.save()
            return HttpResponse(content=b'Изменено')
        except:
            ShowsBuyer.objects.get(array_buyer=buyer, array_cont_ower=cont_owner).delete()
            return HttpResponse(status=500, content=b'Изменено')

# END BLOCK PICK UP AN OBJECT


# START BLOCK MEETING
class MeetingSingleList(MeetingList):
    model = Meeting
    template_name = 'single_buyer/meeting.html'

    def get_context_data(self, **kwargs):
        self.context = super(MeetingSingleList, self).get_context_data(**kwargs)
        self.context['tabs_active_all'] = 1
        self.context['tabs_active_active'] = 0
        self.context['tabs_active_archive'] = 0
        self.context['count_meet_active'] = Meeting.objects.filter(meet_trash=False,
                                                                   meet_archiv=False,
                                                                   meet_buyer=self.request.GET.get('id_buyer')).count()
        self.context['count_meet_all'] = Meeting.objects.filter(meet_trash=False,
                                                                meet_buyer=self.request.GET.get('id_buyer')).count()
        self.context['count_meet_archive'] = Meeting.objects.filter(meet_trash=False,
                                                                    meet_archiv=True,
                                                                    meet_buyer=self.request.GET.get('id_buyer')).count()
        return self.context

    def get_queryset(self):
        self.queryset = Meeting.objects.filter(meet_trash=False, meet_buyer=self.request.GET.get('id_buyer'))
        return self.queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(MeetingSingleList, self).dispatch(request, *args, **kwargs)


class MeetingSingleListActive(MeetingSingleList):
    queryset = Meeting.objects.filter(meet_trash=False, meet_archiv=False)

    def get_context_data(self, **kwargs):
        self.context = super(MeetingSingleListActive, self).get_context_data(**kwargs)
        self.context['tabs_active_active'] = 1
        self.context['tabs_active_all'] = 0
        self.context['tabs_active_archive'] = 0
        return self.context

    def get_queryset(self):
        self.queryset = self.queryset.filter(meet_buyer=self.request.GET.get('id_buyer'))
        return self.queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(MeetingSingleListActive, self).dispatch(request, *args, **kwargs)


class MeetingSingleListArchive(MeetingSingleList):
    queryset = Meeting.objects.filter(meet_trash=False, meet_archiv=True)

    def get_context_data(self, **kwargs):
        self.context = super(MeetingSingleListArchive, self).get_context_data(**kwargs)
        self.context['tabs_active_active'] = 0
        self.context['tabs_active_all'] = 0
        self.context['tabs_active_archive'] = 1
        return self.context

    def get_queryset(self):
        self.queryset = self.queryset.filter(meet_buyer=self.request.GET.get('id_buyer'))
        return self.queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(MeetingSingleListArchive, self).dispatch(request, *args, **kwargs)

# END BLOCK MEETING


# START BLOCK TASKING


class TaskingSingleList(TaskingList):
    model = Tasking
    template_name = 'single_buyer/tasking.html'

    def get_context_data(self, **kwargs):
        self.context = super(TaskingSingleList, self).get_context_data(**kwargs)
        self.context['tabs_active_all'] = 1
        self.context['tabs_active_active'] = 0
        self.context['tabs_active_archive'] = 0
        self.context['count_task_active'] = Tasking.objects.filter(task_trash=False,
                                                                   task_archiv=False,
                                                                   task_buyer=self.request.GET.get('id_buyer')).count()
        self.context['count_task_all'] = Tasking.objects.filter(task_trash=False,
                                                                task_buyer=self.request.GET.get('id_buyer')).count()
        self.context['count_task_archive'] = Tasking.objects.filter(task_trash=False,
                                                                    task_archiv=True,
                                                                    task_buyer=self.request.GET.get('id_buyer')).count()
        return self.context

    def get_queryset(self):
        self.queryset = Tasking.objects.filter(task_trash=False, task_buyer=self.request.GET.get('id_buyer'))
        return self.queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TaskingSingleList, self).dispatch(request, *args, **kwargs)


class TaskingSingleListActive(TaskingSingleList):
    queryset = Tasking.objects.filter(task_trash=False, task_archiv=False)

    def get_context_data(self, **kwargs):
        self.context = super(TaskingSingleListActive, self).get_context_data(**kwargs)
        self.context['tabs_active_active'] = 1
        self.context['tabs_active_all'] = 0
        self.context['tabs_active_archive'] = 0
        return self.context

    def get_queryset(self):
        self.queryset = self.queryset.filter(task_buyer=self.request.GET.get('id_buyer'))
        return self.queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TaskingSingleListActive, self).dispatch(request, *args, **kwargs)


class TaskingSingleListArchive(TaskingSingleList):
    queryset = Tasking.objects.filter(task_trash=False, task_archiv=True)

    def get_context_data(self, **kwargs):
        self.context = super(TaskingSingleListArchive, self).get_context_data(**kwargs)
        self.context['tabs_active_active'] = 0
        self.context['tabs_active_all'] = 0
        self.context['tabs_active_archive'] = 1
        return self.context

    def get_queryset(self):
        self.queryset = self.queryset.filter(task_buyer=self.request.GET.get('id_buyer'))
        return self.queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TaskingSingleListArchive, self).dispatch(request, *args, **kwargs)

# END BLOCK TASKING
