# -*- coding: utf-8 -*-


def change_form_text(form):
    form._errors['phone'] = '• Обязательное поле'
    return form
