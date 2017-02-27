# -*- coding: utf-8 -*-


from django.conf.urls import url
from notes.views import note_add, note_del, note_edit

urlpatterns = [
    # request notes
    url(r'^note_add$', note_add),
    url(r'^note_del$', note_del),
    url(r'^note_edit$', note_edit),
    # end request notes
]
