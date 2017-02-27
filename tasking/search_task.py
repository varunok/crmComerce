# -*- coding: utf-8 -*-


from tasking.models import Tasking


def search(request):
    task = Tasking.objects.filter(task_archiv=False, task_trash=False)
    try:
        if request.get('search_task_rieltor'):
            task = task.filter(rieltor__in=request.getlist('search_task_rieltor'))
        if request.get('data_to'):
            task = task.filter(dead_line__gte=request.get('data_to'))
        if request.get('data_from'):
            task = task.filter(dead_line__lte=request.get('data_from'))
        if request.get('complexity') != '-----':
            task = task.filter(type_complex=request.get('complexity'))
        return task
    except:
        return task
