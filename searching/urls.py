# -*- coding: utf-8 -*-


from django.conf.urls import url
from searching.views import searching

urlpatterns = [
    url(r'searching$', searching),
]