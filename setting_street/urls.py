# -*- coding: utf-8 -*-


from django.conf.urls import url

from setting_street.views.setting_street_views import street_list, add_street, delete_street
from setting_street.views.setting_list_street_views import setting_list_street
from setting_street.views.setting_district_views import setting_district, add_district, delete_district
from setting_street.views.setting_subway_views import setting_subway, add_subway, delete_subway

urlpatterns = [

    url(r'^setting/setting_list_street$', setting_list_street, name='setting_list_street'),

    # start settings street objects
    url(r'^setting/setting_street$', street_list, name='setting_street'),
    url(r'^setting/add_street$', add_street),
    url(r'^setting/delete_street$', delete_street),
    # end settings street objects

    # start setting district objects
    url(r'^setting/setting_district$', setting_district, name='setting_district'),
    url(r'^setting/add_district$', add_district),
    url(r'^setting/delete_district$', delete_district),
    # end setting district objects

    # start setting subway objects
    url(r'^setting/setting_subway$', setting_subway, name='setting_subway'),
    url(r'^setting/add_subway$', add_subway),
    url(r'^setting/delete_subway$', delete_subway),
    # end setting subway objects
]


