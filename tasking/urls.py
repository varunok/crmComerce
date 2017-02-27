# -*- coding: utf-8 -*-


from django.conf.urls import url
from tasking.views import get_form_task, save_form_tasking, to_archive, search_task, to_trash, edit_form


urlpatterns = [
    url(r'get_form_task$', get_form_task),
    url(r'save_form_tasking$', save_form_tasking),
    url(r'to_archive$', to_archive),
    url(r'search_task$', search_task),
    url(r'to_trash$', to_trash),
    url(r'edit_form$', edit_form),
]