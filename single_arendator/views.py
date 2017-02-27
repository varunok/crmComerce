# -*- coding: utf-8 -*-


# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.utils import timezone, dateformat
from django.contrib.auth.models import User
from django.views.generic import DetailView
from arendator.models import Arendator, TypeState
from facility.models import NationalCarrency
from extuser.models import MyUser
from single_arendator.models import SingleArendatorComments
from single_object.models import Tie, TypeShows, ShowsArendator
from search_automat import search_automat
from facility.models import ContactOwner, TypeOperations
from meeting.models import Meeting
from tasking.models import Tasking
from homes.views import TaskingList, MeetingList
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class SingleArendatorView(DetailView):
    """docstring for SingleObjectView"""
    model = Arendator
    slug_url_kwarg = 'aid'
    slug_field = 'id'
    template_name = 'single_arendator/single_arendator.html'
    context_object_name = 'single_arendator'

    def get_context_data(self, **kwargs):
        self.context = super(SingleArendatorView, self).get_context_data(**kwargs)
        self.context['nac_carrency'] = NationalCarrency.objects.get(id=1)
        self.context['list_state'] = TypeState.objects.all()
        self.context['single_obj_comments'] = SingleArendatorComments.objects.filter(
            obj_comments=self.context['single_arendator'].id, type_tabs='comments')
        self.context['count_meet'] = Meeting.objects.filter(meet_trash=False, meet_arendator=self.context['single_arendator'].id).count()
        self.context['count_task'] = Tasking.objects.filter(task_trash=False, task_arendator=self.context['single_arendator'].id).count()
        return self.context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(SingleArendatorView, self).dispatch(request, *args, **kwargs)


# START BLOCK COMMENTS
@login_required
def get_comment_arendator(request):
    data_comment = SingleArendatorComments.objects.filter(obj_comments=request.GET['id_arendator']).order_by('-date_comment')
    return render(request, 'single_object/comments.html', {"single_obj_comments": data_comment})


@login_required
def add_single_arendator_comment(request):
    author = User.objects.get(id=request.POST['id_user'])
    author_name = author.get_full_name()
    singl_obj = Arendator.objects.get(id=request.POST['id_single_obj'])
    image = MyUser.objects.get(user=author)
    comment = SingleArendatorComments(obj_comments=singl_obj,
                                      comment=unicode(request.POST['text_comment']),
                                      author_comment=unicode(author_name),
                                      image=unicode(image.image),
                                      type_tabs=request.POST['type_tabs'])
    comment.save()
    comments = SingleArendatorComments.objects.filter(obj_comments=singl_obj).last()
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
        SingleArendatorComments.objects.get(id=id_comment).delete()
        return HttpResponse('comment delete')
    else:
        return HttpResponse('error delete')

# END BLOCK COMMENTS


# START BLOCK PICK UP AN OBJECT
@login_required
def get_object_arendator(request):
    ties = Tie.objects.all()
    shows = TypeShows.objects.all()
    id_show = ShowsArendator.objects.all()
    single_obj_comments = SingleArendatorComments.objects.filter(obj_comments=request.GET.get('id_arendator')).order_by('-date_comment')
    return render(request, 'single_arendator/get_objects.html', {'ties': ties,
                                                                 'id_arendator': request.GET.get('id_arendator'),
                                                                 'shows': shows,
                                                                 'id_show': id_show,
                                                                 'single_obj_comments': single_obj_comments})


@login_required
def automat_tie_arendator(request):
    list_operations = TypeOperations.objects.filter(type_operations__in=['Аренда', 'Посуточна'])
    qeryset = ContactOwner.objects.all().filter(trash=False, list_operations__in=list_operations)
    search_automat(request.GET, qeryset)
    ties = Tie.objects.all()
    shows = TypeShows.objects.all()
    id_show = ShowsArendator.objects.all()
    single_obj_comments = SingleArendatorComments.objects.filter(obj_comments=request.GET.get('id_arendator')).order_by('-date_comment')
    return render(request, 'single_arendator/get_objects.html', {'ties': ties,
                                                                 'id_arendator': request.GET.get('id_arendator'),
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
    arendator = Arendator.objects.get(id=request.GET.get('id_arendator'))
    tie, created = Tie.objects.get_or_create(tie_cont_owner=cont_owner)
    if not Tie.objects.filter(tie_arenda=arendator, tie_cont_owner=cont_owner).exists():
        tie.tie_arenda.add(arendator)
    else:
        return HttpResponse(status=404, content=b'Обект уже в списке')
    ties = Tie.objects.all()
    shows = TypeShows.objects.all()
    id_show = ShowsArendator.objects.all()
    single_obj_comments = SingleArendatorComments.objects.filter(obj_comments=request.GET.get('id_arendator')).order_by('-date_comment')
    return render(request, 'single_arendator/get_objects.html', {'ties': ties,
                                                                 'id_arendator': request.GET.get('id_arendator'),
                                                                 'shows': shows,
                                                                 'id_show': id_show,
                                                                 'single_obj_comments': single_obj_comments})


@login_required
def clear_cont_owner(request):
    if request.method == 'POST':
        try:
            tie_c = Tie.objects.filter(tie_arenda=request.POST.get('id_arendator'))
            for t in tie_c:
                t.tie_arenda.clear()
        except Tie.DoesNotExist:
            pass
        ties = Tie.objects.all()
        shows = TypeShows.objects.all()
        id_show = ShowsArendator.objects.all()
        single_obj_comments = SingleArendatorComments.objects.filter(
            obj_comments=request.POST.get('id_arendator')).order_by('-date_comment')
        return render(request, 'single_arendator/get_objects.html', {'ties': ties,
                                                                     'id_arendator': request.POST.get('id_arendator'),
                                                                     'shows': shows,
                                                                     'id_show': id_show,
                                                                     'single_obj_comments': single_obj_comments})


@login_required
def del_cont_owner(request):
    if request.method == 'POST':
        tie = Tie.objects.get(tie_cont_owner=request.POST.get('id_cont_owner'))
        arend = tie.tie_arenda.get(id=request.POST.get('id_arendator'))
        tie.tie_arenda.remove(arend)
        ties = Tie.objects.all()
        shows = TypeShows.objects.all()
        id_show = ShowsArendator.objects.all()
        single_obj_comments = SingleArendatorComments.objects.filter(
            obj_comments=request.POST.get('id_arendator')).order_by('-date_comment')
        return render(request, 'single_arendator/get_objects.html', {'ties': ties,
                                                                     'id_arendator': request.POST.get('id_arendator'),
                                                                     'shows': shows,
                                                                     'id_show': id_show,
                                                                     'single_obj_comments': single_obj_comments})


@login_required
def change_show_owner(request):
    if request.method == 'POST':
        cont_owner = ContactOwner.objects.get(id=request.POST.get('id_cont_owner'))
        arendator = Arendator.objects.get(id=request.POST.get('id_arendator'))
        try:
            show = TypeShows.objects.get(id=request.POST.get('show'))
            new_show, created = ShowsArendator.objects.get_or_create(array_arendator=arendator, array_cont_ower=cont_owner)
            new_show.type_shows_arendator = show
            new_show.save()
            return HttpResponse(content=b'Изменено')
        except:
            ShowsArendator.objects.get(array_arendator=arendator, array_cont_ower=cont_owner).delete()
            return HttpResponse(status=500, content=b'Изменено')

# END BLOCK PICK UP AN OBJECT


# START BLOCK MEETING
class MeetingSingleList(MeetingList):
    model = Meeting
    template_name = 'single_arendator/meeting.html'

    def get_context_data(self, **kwargs):
        self.context = super(MeetingSingleList, self).get_context_data(**kwargs)
        self.context['tabs_active_all'] = 1
        self.context['tabs_active_active'] = 0
        self.context['tabs_active_archive'] = 0
        self.context['count_meet_active'] = Meeting.objects.filter(meet_trash=False,
                                                                   meet_archiv=False,
                                                                   meet_arendator=self.request.GET.get('id_arendator')).count()
        self.context['count_meet_all'] = Meeting.objects.filter(meet_trash=False,
                                                                meet_arendator=self.request.GET.get('id_arendator')).count()
        self.context['count_meet_archive'] = Meeting.objects.filter(meet_trash=False,
                                                                    meet_archiv=True,
                                                                    meet_arendator=self.request.GET.get('id_arendator')).count()
        return self.context

    def get_queryset(self):
        self.queryset = Meeting.objects.filter(meet_trash=False, meet_arendator=self.request.GET.get('id_arendator'))
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
        self.queryset = self.queryset.filter(meet_arendator=self.request.GET.get('id_arendator'))
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
        self.queryset = self.queryset.filter(meet_arendator=self.request.GET.get('id_arendator'))
        return self.queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(MeetingSingleListArchive, self).dispatch(request, *args, **kwargs)

# END BLOCK MEETING


# START BLOCK TASKING


class TaskingSingleList(TaskingList):
    model = Tasking
    template_name = 'single_arendator/tasking.html'

    def get_context_data(self, **kwargs):
        self.context = super(TaskingSingleList, self).get_context_data(**kwargs)
        self.context['tabs_active_all'] = 1
        self.context['tabs_active_active'] = 0
        self.context['tabs_active_archive'] = 0
        self.context['count_task_active'] = Tasking.objects.filter(task_trash=False,
                                                                   task_archiv=False,
                                                                   task_arendator=self.request.GET.get('id_arendator')).count()
        self.context['count_task_all'] = Tasking.objects.filter(task_trash=False,
                                                                task_arendator=self.request.GET.get('id_arendator')).count()
        self.context['count_task_archive'] = Tasking.objects.filter(task_trash=False,
                                                                    task_archiv=True,
                                                                    task_arendator=self.request.GET.get('id_arendator')).count()
        return self.context

    def get_queryset(self):
        self.queryset = Tasking.objects.filter(task_trash=False, task_arendator=self.request.GET.get('id_arendator'))
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
        self.queryset = self.queryset.filter(task_arendator=self.request.GET.get('id_arendator'))
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
        self.queryset = self.queryset.filter(task_arendator=self.request.GET.get('id_arendator'))
        return self.queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TaskingSingleListArchive, self).dispatch(request, *args, **kwargs)

# END BLOCK TASKING
