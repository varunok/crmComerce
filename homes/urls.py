# -*- coding: utf-8 -*-


from django.conf.urls import url
from homes import views


urlpatterns = [
    # site pages menu
    url(r'^$', views.homes, name='homes'),
    url(r'^objects/$', views.ObjectList.as_view(), name='objects'),
    url(r'^[a-zA-Z]+/search_obj/$', views.ObjectListSearch.as_view(), name='objects_search'),
    url(r'^selling/$', views.ObjectListSelling.as_view(), name='selling'),
    url(r'^arend/$', views.ObjectListArend.as_view(), name='arend'),
    url(r'^buyers$', views.BuyersList.as_view(), name='buyers'),
    url(r'^maklers$', views.MaklerList.as_view(), name='maklers'),
    url(r'^arendators$', views.ArendatorsList.as_view(), name='arendators'),
    url(r'^buyers/add_buyer$', views.add_buyer, name='add_buyer'),
    url(r'^arendators/add_arendator$', views.add_arendator, name='add_arendator'),
    url(r'^objects/add_object$', views.add_object, name='add_object'),
    url(r'^tasking$', views.TaskingList.as_view(), name='tasking'),
    url(r'^archive$', views.TaskingListArchive.as_view(), name='archive'),
    url(r'^setting$', views.setting, name='setting'),
    url(r'^meeting$', views.MeetingList.as_view(), name='meeting'),
    url(r'^archive_meet$', views.MeetingListArchive.as_view(), name='archive_meet'),
    url(r'^show_activity_index$', views.show_activity_index),
    # end site
]
