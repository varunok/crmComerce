# -*- coding: utf-8 -*-


from django.conf.urls import url
from learning.views import get_learn_list, add_learning, add_learn_form, del_learn

urlpatterns = [
    url(r'^get_learn_list$', get_learn_list, name='get_learn_list'),
    url(r'^add_learning$', add_learning, name='add_learning'),
    url(r'^add_learn_form$', add_learn_form, name='add_learn_form'),
    url(r'^del_learn$', del_learn, name='del_learn'),
]
