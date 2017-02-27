# -*- coding: utf-8 -*-


# Create your views here.
from django.shortcuts import render
from django.utils import timezone, dateformat
from datetime import datetime
from django.utils import formats
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

from facility.models import ContactOwner, ImagesFacility, NationalCarrency, TypeActuality
from single_object.models import SingleObjComments, Tie, TypeShows, ShowsArendator, TieBuyer, ShowsBuyer
from extuser.models import MyUser
from arendator.models import Arendator
from buyer.models import Buyer
from search_automat_arendator import search_automat
from search_automat_buyer import search_automat_buyer
from tasking.models import Tasking
from meeting.models import Meeting
from homes.views import TaskingList, MeetingList
from setting_globall.models import Franshise, Subscribe, FranshiseSity
from sender_email.views import link_to_single_obj


class SingleObjectView(DetailView):
    """docstring for SingleObjectView"""
    model = ContactOwner
    slug_url_kwarg = 'oid'
    slug_field = 'id'
    template_name = 'single_object/single_object.html'
    context_object_name = 'single_object'

    def get_context_data(self, **kwargs):
        self.context = super(SingleObjectView, self).get_context_data(**kwargs)
        self.context['images'] = ImagesFacility.objects.all().filter(album=self.context['single_object'].id)
        self.context['nac_carrency'] = NationalCarrency.objects.get(id=1)
        self.context['sity'] = FranshiseSity.objects.get(id=1)
        self.context['type_actuality'] = TypeActuality.objects.all()
        self.context['single_obj_comments'] = SingleObjComments.objects.filter(
            obj_comments=self.context['single_object'].id, type_tabs='comments')
        try:
            self.context['count_arendator'] = Tie.objects.get(tie_cont_owner=self.context['single_object'].id).tie_arenda.all().count()
        except:
            self.context['count_arendator'] = 0
        try:
            self.context['count_buyer'] = TieBuyer.objects.get(tie_cont_owner=self.context['single_object'].id).tie_buye.all().count()
        except:
            self.context['count_buyer'] = 0
        self.context['count_task'] = Tasking.objects.filter(task_trash=False, task_facility=self.context['single_object'].id).count()
        self.context['count_meet'] = Meeting.objects.filter(meet_trash=False, meet_facility=self.context['single_object'].id).count()
        self.context['previu_sms'] = link_to_single_obj(self.context['single_object'], 'arendator')
        self.context['subscribe'], created = Subscribe.objects.get_or_create(id=1)
        return self.context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.trash:
            return HttpResponseNotFound('<h1>Page not found</h1>')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(SingleObjectView, self).dispatch(request, *args, **kwargs)


@login_required
def change_call_date(request):
    # try:
        date_request = datetime.strptime(str(request.GET['data']), "%Y-%m-%d")
        date_change = dateformat.format(date_request, 'Y-m-d')
        con_owner = ContactOwner.objects.get(id=request.GET['id'])
        con_owner.call_date = date_change
        con_owner.save()
        formatted_datetime = formats.date_format(con_owner.date_of_renovation, "DATETIME_FORMAT")
        return HttpResponse(formatted_datetime)
    # except:
    #     return HttpResponse("error")


@login_required
def change_review_date(request):
    date_request = datetime.strptime(str(request.GET['data']), "%Y-%m-%d")
    date_change = dateformat.format(date_request, 'Y-m-d')
    con_owner = ContactOwner.objects.get(id=request.GET['id'])
    con_owner.review_date = date_change
    con_owner.save()
    formatted_datetime = formats.date_format(con_owner.date_of_renovation, "DATETIME_FORMAT")
    return HttpResponse(formatted_datetime)


@login_required
def change_actuality(request):
    con_owner = ContactOwner.objects.get(id=request.GET['id'])
    actual = TypeActuality.objects.get(id=request.GET['data'])
    con_owner.actuality = actual
    con_owner.save()
    formatted_datetime = formats.date_format(con_owner.date_of_renovation, "DATETIME_FORMAT")
    return HttpResponse(formatted_datetime)


@login_required
def repeat_obj(request):
    single_obj = ContactOwner.objects.get(id=request.GET.get('id_so'))
    single_obj.save()
    formatted_datetime = formats.date_format(single_obj.date_of_renovation, "DATETIME_FORMAT")
    return HttpResponse(formatted_datetime)


# START BLOCK COMMENTS
@login_required
def get_comment(request):
    data_comment = SingleObjComments.objects.filter(obj_comments=request.GET['id_so']).order_by('-date_comment')
    return render(request, 'single_object/comments.html', {"single_obj_comments": data_comment})


@login_required
def add_obj_comment(request):
    author = User.objects.get(id=request.POST['id_user'])
    author_name = author.get_full_name()
    singl_obj = ContactOwner.objects.get(id=request.POST['id_single_obj'])
    image = MyUser.objects.get(user=author)
    comment = SingleObjComments(obj_comments=singl_obj,
                                comment=unicode(request.POST['text_comment']),
                                author_comment=unicode(author_name),
                                image=unicode(image.image),
                                type_tabs=request.POST['type_tabs'])
    comment.save()
    comments = SingleObjComments.objects.filter(obj_comments=singl_obj).last()
    date_comment = dateformat.format(comments.date_comment, 'd E Y H:i')
    comment_data = JsonResponse({
        "text": comments.comment,
        "author": comments.author_comment,
        "date": date_comment,
        "image": str(image.image),
        "id_comment": comments.id})
    return HttpResponse(comment_data)


@login_required
def del_comment(request):
    if request.method == 'POST':
        id_comment = request.POST.get('id_comment').split('_')[-1]
        SingleObjComments.objects.get(id=id_comment).delete()
        return HttpResponse('comment delete')
    else:
        return HttpResponse('error delete')
# END BLOCK COMMENTS

# START BLOCK ARENDATOR


class AddArendatorToTie(DetailView):
    model = Arendator
    slug_url_kwarg = 'idu'
    slug_field = 'id'
    template_name = 'single_object/return_table/single_table.html'
    context_object_name = 'arendator'

    def get_context_data(self, **kwargs):
        self.context = super(AddArendatorToTie, self).get_context_data(**kwargs)
        self.context['type_shows'] = TypeShows.objects.all()
        self.context['nac_carrency'] = NationalCarrency.objects.get(id=1)
        self.context['show_arendators'] = ShowsArendator.objects.all()
        self.context['error'] = True
        return self.context

    def get(self, request, *args, **kwargs):
        if Arendator.objects.filter(id=self.kwargs['idu'], trash=False).exists():
            arendator = Arendator.objects.get(id=self.kwargs['idu'], trash=False)
        else:
            return HttpResponse(status=404)
        cont_owner = ContactOwner.objects.get(id=self.request.GET.get('id'))
        # self.context['count_arendator'] = Tie.objects.get(tie_cont_owner=cont_owner).tie_arenda.all().count()
        tie, created = Tie.objects.get_or_create(tie_cont_owner=cont_owner)
        if not Tie.objects.filter(tie_arenda=arendator, tie_cont_owner=cont_owner).exists():
            tie.tie_arenda.add(arendator)
        else:
            return HttpResponse(status=404)
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AddArendatorToTie, self).dispatch(request, *args, **kwargs)


class AutomatTie(ListView):
    model = Arendator
    context_object_name = 'arendators'
    template_name = 'single_object/return_table/list_table.html'
    qeryset = Arendator.objects.all().filter(trash=False)

    def get_context_data(self, **kwargs):
        self.context = super(AutomatTie, self).get_context_data(**kwargs)
        self.context['type_shows'] = TypeShows.objects.all()
        self.context['nac_carrency'] = NationalCarrency.objects.get(id=1)
        self.context['show_arendators'] = ShowsArendator.objects.all()
        self.context['error'] = True
        return self.context

    def get_queryset(self):
        return search_automat(self.request.GET, self.qeryset)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AutomatTie, self).dispatch(request, *args, **kwargs)


@login_required
def get_arendator(request):
    ties = Tie.objects.all()
    singl_obg = ContactOwner.objects.get(id=request.GET.get('id_so'))
    try:
        count_arendator = Tie.objects.get(tie_cont_owner=singl_obg).tie_arenda.all().count()
    except:
        count_arendator = 0
    type_shows = TypeShows.objects.all()
    nac_carrency = NationalCarrency.objects.get(id=1)
    shows = ShowsArendator.objects.all()
    data_comment = SingleObjComments.objects.filter(obj_comments=request.GET['id_so']).order_by('-date_comment')
    return render(request, 'single_object/arendator.html', {"ties": ties,
                                                            "singl_obj": singl_obg,
                                                            "display": True,
                                                            "error": True,
                                                            "type_shows": type_shows,
                                                            "nac_carrency": nac_carrency,
                                                            "shows_arendator": shows,
                                                            "count_arendator": count_arendator,
                                                            "single_obj_comments": data_comment,
                                                            "id_so": request.GET.get('id_so')})


@login_required
def change_shows(request, id_a):
    id_a, id_o, id_show = id_a.split('=')
    id_a = id_a.split('-')[-1]
    id_o = id_o.split('-')[-1]
    id_show = id_show.split('-')[-1]
    arendator = Arendator.objects.get(id=id_a)
    cont_owner = ContactOwner.objects.get(id=id_o)
    try:
        type_shows = TypeShows.objects.get(id=id_show)
        show_ar, created = ShowsArendator.objects.get_or_create(array_arendator=arendator, array_cont_ower=cont_owner)
        show_ar.type_shows_arendator = type_shows
        show_ar.save()
        return HttpResponse('ok')
    except:
        ShowsArendator.objects.get(array_arendator=arendator, array_cont_ower=cont_owner).delete()
        return HttpResponse(status=500, content=b'Изменено')


@login_required
def delete_tie_arendator(request, did):
    try:
        tie = Tie.objects.get(tie_cont_owner=request.POST.get('id'))
        arend = tie.tie_arenda.get(id=did)
        tie.tie_arenda.remove(arend)
        if tie.tie_arenda.filter(id=did):
            return HttpResponse(status=404)
        return HttpResponse(status=200)
    except:
        return HttpResponse(status=404)


@login_required
def clear_all_arendator(request):
    try:
        tie = Tie.objects.get(tie_cont_owner=request.POST.get('id'))
        tie.tie_arenda.clear()
        return HttpResponse(status=200)
    except:
        return HttpResponse(status=404)
# END BLOCK ARENDATOR

# START BLOCK BUYER


class AddBuyerToTie(DetailView):
    model = Buyer
    slug_url_kwarg = 'idu'
    slug_field = 'id'
    template_name = 'single_object/return_table/single_table_buyer.html'
    context_object_name = 'buyer'

    def get_context_data(self, **kwargs):
        self.context = super(AddBuyerToTie, self).get_context_data(**kwargs)
        self.context['type_shows'] = TypeShows.objects.all()
        self.context['nac_carrency'] = NationalCarrency.objects.get(id=1)
        self.context['show_arendators'] = ShowsBuyer.objects.all()
        self.context['error'] = True
        return self.context

    def get(self, request, *args, **kwargs):
        if Buyer.objects.filter(id=self.kwargs['idu'], trash=False).exists():
            buyer = Buyer.objects.get(id=self.kwargs['idu'], trash=False)
        else:
            return HttpResponse(status=404)
        cont_owner = ContactOwner.objects.get(id=self.request.GET.get('id'))
        # self.context['count_arendator'] = Tie.objects.get(tie_cont_owner=cont_owner).tie_arenda.all().count()
        tie_buyer, created = TieBuyer.objects.get_or_create(tie_cont_owner=cont_owner)
        if not TieBuyer.objects.filter(tie_buye=buyer, tie_cont_owner=cont_owner).exists():
            tie_buyer.tie_buye.add(buyer)
        else:
            return HttpResponse(status=404)
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AddBuyerToTie, self).dispatch(request, *args, **kwargs)


class AutomatTieBuyer(ListView):
    model = Buyer
    context_object_name = 'buyers'
    template_name = 'single_object/return_table/list_table_buyer.html'
    qeryset = Buyer.objects.all().filter(trash=False)

    def get_context_data(self, **kwargs):
        self.context = super(AutomatTieBuyer, self).get_context_data(**kwargs)
        self.context['type_shows'] = TypeShows.objects.all()
        self.context['nac_carrency'] = NationalCarrency.objects.get(id=1)
        self.context['show_arendators'] = ShowsBuyer.objects.all()
        self.context['error'] = True
        return self.context

    def get_queryset(self):
        return search_automat_buyer(self.request.GET, self.qeryset)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AutomatTieBuyer, self).dispatch(request, *args, **kwargs)


@login_required
def get_buyer(request):
    ties = TieBuyer.objects.all()
    singl_obg = ContactOwner.objects.get(id=request.GET.get('id_so'))
    try:
        count_buyers = TieBuyer.objects.get(tie_cont_owner=singl_obg).tie_buye.all().count()
    except:
        count_buyers = 0
    type_shows = TypeShows.objects.all()
    nac_carrency = NationalCarrency.objects.get(id=1)
    shows = ShowsBuyer.objects.all()
    data_comment = SingleObjComments.objects.filter(obj_comments=request.GET['id_so']).order_by('-date_comment')
    return render(request, 'single_object/buyers.html', {"ties": ties,
                                                         "singl_obj": singl_obg,
                                                         "display": True,
                                                         "error": True,
                                                         "type_shows": type_shows,
                                                         "nac_carrency": nac_carrency,
                                                         "shows_buyer": shows,
                                                         "count_buyer": count_buyers,
                                                         "single_obj_comments": data_comment})


@login_required
def change_shows_buyer(request, id_a):
    try:
        id_a, id_o, id_show = id_a.split('=')
        id_a = id_a.split('-')[-1]
        id_o = id_o.split('-')[-1]
        id_show = id_show.split('-')[-1]
        type_shows = TypeShows.objects.get(id=id_show)
        buyer = Buyer.objects.get(id=id_a)
        cont_owner = ContactOwner.objects.get(id=id_o)
        show_ar, created = ShowsBuyer.objects.get_or_create(array_buyer=buyer, array_cont_ower=cont_owner)
        show_ar.type_shows_buyer = type_shows
        show_ar.save()
        return HttpResponse('ok')
    except:
        return HttpResponse('error')


@login_required
def delete_tie_buyer(request, did):
    try:
        tie = TieBuyer.objects.get(tie_cont_owner=request.POST.get('id'))
        buyers = tie.tie_buye.get(id=did)
        tie.tie_buye.remove(buyers)
        if tie.tie_buye.filter(id=did):
            return HttpResponse(status=404)
        return HttpResponse(status=200)
    except:
        return HttpResponse(status=404)


@login_required
def clear_all_buyer(request):
    try:
        tie = TieBuyer.objects.get(tie_cont_owner=request.POST.get('id'))
        tie.tie_buye.clear()
        return HttpResponse(status=200)
    except:
        return HttpResponse(status=404)
# END BLOCK BUYER

# START BLOCK TASKING


class TaskingSingleList(TaskingList):
    model = Tasking
    template_name = 'single_object/tasks.html'

    def get_context_data(self, **kwargs):
        self.context = super(TaskingSingleList, self).get_context_data(**kwargs)
        self.context['tabs_active_all'] = 1
        self.context['tabs_active_active'] = 0
        self.context['tabs_active_archive'] = 0
        self.context['count_task_active'] = Tasking.objects.filter(task_trash=False,
                                                                   task_archiv=False, task_facility=self.request.GET.get('id_so')).count()
        self.context['count_task_all'] = Tasking.objects.filter(task_trash=False, task_facility=self.request.GET.get('id_so')).count()
        self.context['count_task_archive'] = Tasking.objects.filter(task_trash=False,
                                                                    task_archiv=True, task_facility=self.request.GET.get('id_so')).count()
        return self.context

    def get_queryset(self):
        self.queryset = Tasking.objects.filter(task_trash=False, task_facility=self.request.GET.get('id_so'))
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
        self.queryset = self.queryset.filter(task_facility=self.request.GET.get('id_so'))
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
        self.queryset = self.queryset.filter(task_facility=self.request.GET.get('id_so'))
        return self.queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TaskingSingleListArchive, self).dispatch(request, *args, **kwargs)

# END BLOCK TASKING


# START BLOCK PUBLICATIONS
@login_required
def get_publication(request):
    from posting.work_table import GetShows
    len_shows = GetShows(request.GET['id_so']).data_return()
    franshise = Franshise.objects.values()[0]['franshise']
    single_object = ContactOwner.objects.get(id=request.GET['id_so'])
    return render(request, 'single_object/publication.html', {"franshise": franshise,
                                                              "status": single_object,
                                                              "len_shows": len_shows})

# END BLOCK PUBLICATIONS


# START BLOCK MEETING
class MeetingSingleList(MeetingList):
    model = Meeting
    template_name = 'single_object/meetings.html'

    def get_context_data(self, **kwargs):
        self.context = super(MeetingSingleList, self).get_context_data(**kwargs)
        self.context['tabs_active_all'] = 1
        self.context['tabs_active_active'] = 0
        self.context['tabs_active_archive'] = 0
        self.context['count_meet_active'] = Meeting.objects.filter(meet_trash=False,
                                                                   meet_archiv=False, meet_facility=self.request.GET.get('id_so')).count()
        self.context['count_meet_all'] = Meeting.objects.filter(meet_trash=False, meet_facility=self.request.GET.get('id_so')).count()
        self.context['count_meet_archive'] = Meeting.objects.filter(meet_trash=False,
                                                                    meet_archiv=True, meet_facility=self.request.GET.get('id_so')).count()
        return self.context

    def get_queryset(self):
        self.queryset = Meeting.objects.filter(meet_trash=False, meet_facility=self.request.GET.get('id_so'))
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
        self.queryset = self.queryset.filter(meet_facility=self.request.GET.get('id_so'))
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
        self.queryset = self.queryset.filter(meet_facility=self.request.GET.get('id_so'))
        return self.queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(MeetingSingleListArchive, self).dispatch(request, *args, **kwargs)

# END BLOCK MEETING


class DatabasesPrevious(SingleObjectView):
    slug_url_kwarg = 'poid'
    slug_field = 'id'
    template_name = 'single_object/previews.html'

    def dispatch(self, request, *args, **kwargs):
        return super(SingleObjectView, self).dispatch(request, *args, **kwargs)
