# -*- coding: utf-8 -*-


from django.conf.urls import url
from facility.views import add_facility, check_phone, add_img, del_img, trash_obj, edit_facility, save_edit_facility, \
    restore_obj

urlpatterns = [
    url(r'^add_facility$', add_facility, name='add_facility'),
    url(r'^edit_facility/add_facility$', save_edit_facility),
    url(r'^check_phone$', check_phone),
    url(r'^add_img$', add_img),
    url(r'^edit_facility/add_img$', add_img),
    url(r'^del_img$', del_img),
    url(r'^edit_facility/del_img$', del_img),
    url(r'^restore_obj$', restore_obj),
    url(r'^trash_obj$', trash_obj),
    url(r'^edit_facility/(?P<id_obj>[0-9]+)$', edit_facility, name='edit_facility'),
]
