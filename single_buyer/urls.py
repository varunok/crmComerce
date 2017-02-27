# -*- coding: utf-8 -*-


from django.conf.urls import url
from single_buyer.views import SingleBuyerView, add_single_buyer_comment, get_comment_buyer, \
    del_comment, get_object_buyer, automat_tie_buyer, add_id_cont_owner, clear_cont_owner, \
    del_cont_owner, change_show_owner, MeetingSingleList, MeetingSingleListActive, \
    MeetingSingleListArchive, TaskingSingleList, TaskingSingleListActive, TaskingSingleListArchive

from meeting.views import get_form_task as get_form_meet, save_form_meeting, to_trash as to_trash_meet, \
    to_archive as to_archive_meet, edit_form as edit_form_meet

from tasking.views import get_form_task as get_form_single_task, edit_form as edit_form_task, save_form_tasking as save_form_tasking_task, \
    to_trash as to_trash_task, to_archive as to_archive_task


urlpatterns = [
    url(r'^(?P<aid>[0-9]+)$', SingleBuyerView.as_view(), name='single_buyer'),

    # block comment
    url(r'^get_comment_buyer$', get_comment_buyer, name='get_comment_buyer'),
    url(r'^add_single_buyer_comment$', add_single_buyer_comment, name='add_single_buyer_comment'),
    url(r'^del_comment$', del_comment, name='del_comment'),
    # end block comment

    # block pick up an object
    url(r'^get_object_buyer$', get_object_buyer, name='get_object_buyer'),
    url(r'^automat_tie_buyer$', automat_tie_buyer, name='automat_tie_buyer'),
    url(r'^add_id_cont_owner$', add_id_cont_owner, name='add_id_cont_owner'),
    url(r'^clear_cont_owner$', clear_cont_owner, name='clear_cont_owner'),
    url(r'^del_cont_owner$', del_cont_owner, name='del_cont_owner'),
    url(r'^change_show_owner$', change_show_owner, name='change_show_owner'),
    # end block pick up an object

    # start meeting block
    url(r'^get_meeting_buyer$', MeetingSingleList.as_view(), name='get_meetings'),
    url(r'^get_meetings_active$', MeetingSingleListActive.as_view(), name='get_meetings_active'),
    url(r'^get_meetings_archive$', MeetingSingleListArchive.as_view(), name='get_meetings_archive'),
    url(r'^get_form_meet$', get_form_meet),
    url(r'^save_form_meeting$', save_form_meeting),
    url(r'^to_trash_meet$', to_trash_meet),
    url(r'^to_archive_meet$', to_archive_meet),
    url(r'^edit_form_meet$', edit_form_meet),
    # end meeting block

    # start block task
    url(r'^get_tasking_buyer$', TaskingSingleList.as_view(), name='get_tasks'),
    url(r'^get_tasks_active$', TaskingSingleListActive.as_view(), name='get_tasks_active'),
    url(r'^get_tasks_archive$', TaskingSingleListArchive.as_view(), name='get_tasks_archive'),
    url(r'^get_form_single_task$', get_form_single_task),
    url(r'^save_form_tasking_task$', save_form_tasking_task),
    url(r'^to_trash_task$', to_trash_task),
    url(r'^to_archive_task$', to_archive_task),
    url(r'^edit_form_task$', edit_form_task),
    # end block task
]