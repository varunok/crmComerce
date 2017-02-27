# -*- coding: utf-8 -*-


import os
import shutil
from facility.models import ImagesFacility, AddressFacilityData
from watermark.wm import AddWatermark
from watermark.models import Watermark
from django.core.files import File


def save_photo(request, last_id, dir_img):
    images = request.FILES.getlist('image', [])
    dir_img = ''.join(['media/tmpimg/', dir_img, '/'])
    try:
        list_tmp_img = os.listdir(dir_img)
    except:
        try:
            list_tmp_img = ImagesFacility.objects.filter(album_id=last_id, cover=True)
            if list_tmp_img:
                return False
            list_tmp_img = ImagesFacility.objects.filter(album_id=last_id)[0]
        except:
            return False
        if list_tmp_img:
            list_tmp_img.cover = True
            list_tmp_img.save()
            return True
        else:
            return False
    # cover_img = True
    for image in list_tmp_img:
        if str(image) in list_tmp_img:
            reopen = open(dir_img + image, 'rb')
            image_file = File(reopen)
            if list_tmp_img.index(image):
                if not ImagesFacility.objects.filter(album_id=last_id, cover=1).exists():
                    watermarks(image, dir_img)
                    img = ImagesFacility(album_id=last_id, image=image_file, cover=1)
                    img.save()
                else:
                    watermarks(image, dir_img)
                    img = ImagesFacility(album_id=last_id, image=image_file)
                    img.save()
            else:
                if not ImagesFacility.objects.filter(album_id=last_id, cover=1).exists():
                    watermarks(image, dir_img)
                    img = ImagesFacility(album_id=last_id, image=image_file, cover=1)
                    img.save()
                else:
                    watermarks(image, dir_img)
                    img = ImagesFacility(album_id=last_id, image=image_file)
                    img.save()

    try:
        shutil.rmtree(dir_img)
    except:
        pass
    images_count = AddressFacilityData.objects.get(id=last_id)
    count_image = ImagesFacility.objects.filter(album=images_count).count()
    images_count.images_count = count_image
    images_count.save()


def watermarks(img, dir_img):
    img_from = ''.join([os.getcwd(), '/', dir_img])
    on_off, create = Watermark.objects.get_or_create(id=1)
    if on_off.on_off:
        AddWatermark(img_from + str(img), img_from + str(img))
