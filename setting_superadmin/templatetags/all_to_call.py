# -*- coding: utf-8 -*-


from django import template
from setting_superadmin.models import AllToCall


register = template.Library()


@register.simple_tag(name='all_to_call')
def all_to_call(arg=''):
    if arg == 'phone':
        try:
            phone = AllToCall.objects.get(id=1)
        except:
            return '00-00-00-00'
        return phone.phone
    elif arg == 'email':
        try:
            email = AllToCall.objects.get(id=1)
        except:
            return 'abc@abc.com'
        return email.email
    elif arg == 'skype':
        try:
            skype = AllToCall.objects.get(id=1)
        except:
            return 'abc'
        return skype.skype
    elif arg == 'group_vk':
        try:
            group_vk = AllToCall.objects.get(id=1)
        except:
            return 'abc_vk'
        return group_vk.group_vk
    else:
        return ''


@register.simple_tag(name='photo_futer')
def photo_futer(arg=''):
    try:
        image = AllToCall.objects.get(id=1)
        return image.image
    except:
        return 'Bad Robot'
