# -*- coding: utf-8 -*-


from django.conf.urls import url
from extuser.views import user_list, login_user, logout_user, register, add_user, delete_user, LoginFormView, \
    send_recavery_pass, edit_user, save_edit_user, edit_pass, save_edit_pass


urlpatterns = [

    url(r'^accounts/login/$', LoginFormView.as_view(), name='login'),  # redirect to login form user
    url(r'^accounts/logining/$', login_user, name='logining'),  # login user and authenticate user
    url(r'^accounts/logout/$', logout_user, name='logout'),  # logout user
    url(r'^register$', register, name='register'),  # register user
    url(r'^setting/setting_user$', user_list, name='setting_user'),  # user list in setting user
    url(r'^setting/save_edit_user$', save_edit_user, name='save_edit_user'),  # user list in setting user
    url(r'^setting/edit_user/(?P<id>[0-9]+)$', edit_user, name='edit_user'),  # user list in setting user
    url(r'^add_user$', add_user, name='add_user'),  # add user
    url(r'^setting/setting_user/delete_user$', delete_user, name='delete_user'),  # delete user
    url(r'^accounts/login/recowery_pass$', send_recavery_pass),
    url(r'^setting/edit_pass/(?P<id>[0-9]+)$', edit_pass, name="edit_pass"),
    url(r'^setting/save_edit_pass/(?P<id>[0-9]+)$', save_edit_pass, name="save_edit_pass"),
]
