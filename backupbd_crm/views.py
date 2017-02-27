# -*- coding: utf-8 -*-


import os
import subprocess
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .writeXLS import WriteXLS
from .backup_objects import title, SaveConOwn
from setting_globall.models import Franshise
from django.contrib.auth.decorators import login_required


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@login_required
def list_backup(request):
    return render(request, 'backupbd_crm/list_backup.html', {})


@login_required
def backup_xls(request):
    # if request.method == 'POST':
    return render(request, 'backupbd_crm/backup_xls.html', {})


@login_required
def create_object_xls(request):
    facilitis = SaveConOwn.objects.all()
    path_to_file = WriteXLS('objects', facilitis, title).write_table()
    return HttpResponse(path_to_file)


@login_required
def backup_global(request):
    return render(request, 'backupbd_crm/backup_global.html', {})


@login_required
def get_backup_global(request):
    # path_to_python = ''
    franshise, created = Franshise.objects.get_or_create(id=1)
    file_name = '-'.join([str(franshise), str(timezone.now()), 'backup.psql'])
    path = ''.join([BASE_DIR, '/media/backup_global/', file_name])
    cmd = ''.join([BASE_DIR, '/../data/bin/python', ' manage.py dbbackup --output-path ', path])
    # cmd = ''.join(['./manage.py dbbackup --output-path ', path])
    # cmd = ''.join([BASE_DIR, '/../data/bin/python', ' manage.py dbbackup'])
    PIPE = subprocess.PIPE
    p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,
                         stderr=subprocess.STDOUT, close_fds=True, cwd=BASE_DIR)
    p = p.stdout.read()
    p = p.split(' ')[-1].strip()
    path_to_file = ''.join([settings.MEDIA_URL, 'backup_global/', file_name])
    return HttpResponse(path_to_file)


@login_required
def restore_file_save(request):
    if request.method == 'POST':
        path = ''.join([BASE_DIR, '/media/restore'])
        try:
            list_file = os.listdir('media/restore/')
            for ele in list_file:
                os.remove(''.join(('media/restore/', ele)))
        except:
            pass
        try:
            os.mkdir(path)
        except:
            pass
        file = request.FILES
        valid = file['0'].name
        valid = valid.split('.')[-1]
        if valid == 'psql':
            with open(path + '/' + file['0'].name, 'wb+') as destination:
                for chunk in file['0'].chunks():
                    destination.write(chunk)
            return HttpResponse(content=b'ok')
        else:
            return HttpResponse(status=500, content=b'bad file')


@login_required
def restore_databases(request):
    list_file = os.listdir('media/restore/')
    # cmd = ''.join(['./manage.py dbrestore --noinput --input-path ', BASE_DIR, '/media/restore/', list_file[0]])
    cmd = ''.join([BASE_DIR, '/../data/bin/python',
                  ' manage.py dbrestore --noinput --input-path ', BASE_DIR, '/media/restore/', list_file[0]])
    PIPE = subprocess.PIPE
    p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,
                         stderr=subprocess.STDOUT, close_fds=True, cwd=BASE_DIR)
    p = p.stdout.read()
    return HttpResponse(p)


@login_required
def backup_dropbox(request):
    cmd = ''.join(['./manage.py dbbackup'])
    PIPE = subprocess.PIPE
    p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,
                         stderr=subprocess.STDOUT, close_fds=True, cwd=BASE_DIR)
    p = p.stdout.read()
    # p = p.split(' ')[-1].strip()
    # path_to_file = ''.join([settings.MEDIA_URL, 'backup_global/', p])
    return HttpResponse(p)
