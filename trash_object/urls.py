# -*- coding: utf-8 -*-


from django.conf.urls import url
import trash_object.views

urlpatterns = [
    url(r'^list_trash$', trash_object.views.list_trash, name='list_trash'),
    url(r'^objects_trash$', trash_object.views.ObjectListTrash.as_view(), name='objects_trash'),
    url(r'^arendator_trash$', trash_object.views.ArendatorListTrash.as_view(), name='arendator_trash'),
    url(r'^buyer_trash$', trash_object.views.BuyerListTrash.as_view(), name='buyer_trash'),
    url(r'^go_trash$', trash_object.views.go_trash),
    url(r'^del_obj$', trash_object.views.del_obj),
    url(r'^del_arendator$', trash_object.views.del_arendator),
    url(r'^del_buyer$', trash_object.views.del_buyer),
    url(r'^archiv_email$', trash_object.views.archiv_email, name='archiv_email'),
    url(r'^delete_message$', trash_object.views.delete_message),
]
