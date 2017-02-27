# -*- coding: utf-8 -*-


from django.conf.urls import url
from access.views import access, change_access_facility, AccessListOwnerView, AccessListUserView

urlpatterns = [
    url(r'^access$', access, name='access'),
    url(r'^change_access_facility$', change_access_facility),
    url(r'^get-access-objects$', AccessListOwnerView.as_view()),
    url(r'^get-access-users$', AccessListUserView.as_view()),
    url(r'^get-access-obj-search$', AccessListOwnerView.as_view()),
]