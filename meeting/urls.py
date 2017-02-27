# -*- coding: utf-8 -*-


from django.conf.urls import url
from meeting.views import get_form_task, save_form_meeting, to_archive, edit_form, to_trash, search_meet

urlpatterns = [
    url(r'get_form_task$', get_form_task),
    url(r'save_form_meeting$', save_form_meeting),
    url(r'to_archive$', to_archive),
    url(r'edit_form$', edit_form),
    url(r'to_trash$', to_trash),
    url(r'search_meet$', search_meet),
]