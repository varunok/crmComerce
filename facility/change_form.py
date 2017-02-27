# -*- coding: utf-8 -*-


def change_form_text(form):
    form._errors['street_obj'] = 'Обязательное поле'
    form._errors['type_facilit'] = 'Обязательное поле'
    form._errors['email_owner'] = '• Введите корректный емейл адрес'
    form._errors['list_operations'] = '• Обязательное поле'
    form._errors['phone_owner'] = 'Обязательное поле'
    form._errors['comment'] = 'Обязательное поле'
    return form