# -*- coding: utf-8 -*-


from django.conf.urls import url
from single_object.views import SingleObjectView, change_call_date, change_review_date, change_actuality, \
    add_obj_comment, del_comment, get_arendator, get_comment, get_buyer, get_publication, \
    TaskingSingleList, DatabasesPrevious, AddArendatorToTie, change_shows, AutomatTie, delete_tie_arendator, clear_all_arendator,\
    AddBuyerToTie, change_shows_buyer, AutomatTieBuyer, delete_tie_buyer, clear_all_buyer, \
    repeat_obj, TaskingSingleListActive, TaskingSingleListArchive, MeetingSingleList, MeetingSingleListActive, \
    MeetingSingleListArchive

from tasking.views import get_form_task, edit_form as edit_form_task, save_form_tasking as save_form_tasking_task, \
    to_trash as to_trash_task, to_archive as to_archive_task

from meeting.views import get_form_task as get_form_meet, save_form_meeting, to_trash as to_trash_meet, \
    to_archive as to_archive_meet, edit_form as edit_form_meet


urlpatterns = [
    url(r'^(?P<oid>[0-9]+)$', SingleObjectView.as_view(), name='single_obj'),
    url(r'^change_call_date$', change_call_date, name='change_call_date'),
    url(r'^change_review_date$', change_review_date, name='change_review_date'),
    url(r'^change_actuality$', change_actuality, name='change_actuality'),
    url(r'^repeat_obj', repeat_obj, name='repeat_obj'),

    # block comment
    url(r'^get_comment$', get_comment, name='get_comment'),
    url(r'^add_obj_comment$', add_obj_comment, name='add_obj_comment'),
    url(r'^del_comment$', del_comment, name='del_comment'),
    # end block comment

    # start block arendator
    url(r'^get_arendator$', get_arendator, name='get_arendator'),
    url(r'^add_arendator_to_tie/(?P<idu>[0-9]+)$', AddArendatorToTie.as_view(), name='add_arendator_to_tie'),
    url(r'^change_shows/(?P<id_a>[0-9a-z-=]+)$', change_shows),
    url(r'^automat_tie$', AutomatTie.as_view(), name='automat_tie'),
    url(r'^delete_tie_arendator/(?P<did>[0-9]+)$', delete_tie_arendator),
    url(r'^clear_all_arendator$', clear_all_arendator),
    # end block arendator

    # start block buyer
    url(r'^get_buyer$', get_buyer, name='get_buyer'),
    url(r'^add_buyer_to_tie/(?P<idu>[0-9]+)$', AddBuyerToTie.as_view(), name='add_buyer_to_tie'),
    url(r'^change_shows_buyer/(?P<id_a>[0-9a-z-=]+)$', change_shows_buyer),
    url(r'^automat_tie_buyer$', AutomatTieBuyer.as_view(), name='automat_tie_buyer'),
    url(r'^delete_tie_buyer/(?P<did>[0-9]+)$', delete_tie_buyer),
    url(r'^clear_all_buyer$', clear_all_buyer),
    # end block buyer

    # start block task
    url(r'^get_tasks$', TaskingSingleList.as_view(), name='get_tasks'),
    url(r'^get_tasks_active$', TaskingSingleListActive.as_view(), name='get_tasks_active'),
    url(r'^get_tasks_archive$', TaskingSingleListArchive.as_view(), name='get_tasks_archive'),
    url(r'^get_form_task$', get_form_task),
    url(r'^save_form_tasking_task$', save_form_tasking_task),
    url(r'^to_trash_task$', to_trash_task),
    url(r'^to_archive_task$', to_archive_task),
    url(r'^edit_form_task$', edit_form_task),
    # end block task

    # start block meet
    url(r'^get_meetings$', MeetingSingleList.as_view(), name='get_meetings'),
    url(r'^get_meetings_active$', MeetingSingleListActive.as_view(), name='get_meetings_active'),
    url(r'^get_meetings_archive$', MeetingSingleListArchive.as_view(), name='get_meetings_archive'),
    url(r'^get_form_meet$', get_form_meet),
    url(r'^save_form_meeting$', save_form_meeting),
    url(r'^to_trash_meet$', to_trash_meet),
    url(r'^to_archive_meet$', to_archive_meet),
    url(r'^edit_form_meet$', edit_form_meet),
    # end block meet

    url(r'^get_publication$', get_publication, name='get_publication'),
    url(r'^data/(?P<poid>[0-9]+)$', DatabasesPrevious.as_view(), name='databases'),

]
