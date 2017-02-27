# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse
from watermark.models import Watermark
from wm import CreateWatermark
from django.contrib.auth.decorators import login_required


@login_required
def setting_watermark(request):
    try:
        wm = Watermark.objects.filter(id=1).get()
    except:
        class Fake():
            text = ''
            watermark_img = ''
        wm = Fake()
    return render(request, 'watermark/setting_watermark.html', {'wm': wm})


@login_required
def create_watermark(request):
    if request.method == 'POST':
        if CreateWatermark(request.POST['wm']).isCreated:
            wm, created = Watermark.objects.update_or_create(id=1, watermark_img='watermark/watermark.png')
            wm.text = request.POST['wm']
            wm.save()
            return HttpResponse(wm.watermark_img.url)
    else:
        return HttpResponse(status=500)


@login_required
def on_off_watermark(request):
    val = request.GET.get('val').strip()
    if val == '1':
        Watermark.objects.filter(id=1).update(on_off=True)
    else:
        Watermark.objects.filter(id=1).update(on_off=False)

    o = Watermark.objects.get(id=1)
    o = o.on_off
    return HttpResponse(o)
