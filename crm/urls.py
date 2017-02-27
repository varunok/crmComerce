# -*- coding: utf-8 -*-


"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import setting_street.urls
import extuser.urls
import homes.urls
import notes.urls
import facility.urls
import setting_globall.urls
import trash_object.urls
import single_object.urls
import who_online.urls
import send_messege_user.urls
import arendator.urls
import buyer.urls
import makler.urls
import setting_superadmin.urls
import tasking.urls
import parsings.urls
import posting.urls
import watermark.urls
import sender_email.urls
import setting_mail_delivery.urls
import meeting.urls
import searching.urls
import single_arendator.urls
import single_buyer.urls
import backupbd_crm.urls
import learning.urls
import access.urls

urlpatterns = [
    url(r'^', include(setting_street.urls)),
    url(r'^', include(extuser.urls)),
    url(r'^', include(homes.urls)),
    url(r'^', include(notes.urls)),
    url(r'^objects/', include(facility.urls)),
    url(r'^', include(setting_globall.urls)),
    url(r'^', include(trash_object.urls)),
    url(r'^objects/', include(single_object.urls)),
    url(r'^', include(who_online.urls)),
    url(r'^', include(send_messege_user.urls)),
    url(r'^arendators/', include(arendator.urls)),
    url(r'^buyers/', include(buyer.urls)),
    url(r'^', include(makler.urls)),
    url(r'^', include(setting_superadmin.urls)),
    url(r'^tasking/', include(tasking.urls)),
    url(r'^', include(parsings.urls)),
    url(r'^', include(posting.urls)),
    url(r'^', include(watermark.urls)),
    url(r'^', include(sender_email.urls)),
    url(r'^', include(setting_mail_delivery.urls)),
    url(r'^', include(meeting.urls)),
    url(r'^', include(searching.urls)),
    url(r'^arendators/', include(single_arendator.urls)),
    url(r'^buyers/', include(single_buyer.urls)),
    url(r'^', include(backupbd_crm.urls)),
    url(r'^', include(learning.urls)),
    url(r'^', include(access.urls)),
    # admin
    url(r'^admin/', admin.site.urls),
    # end admin
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
