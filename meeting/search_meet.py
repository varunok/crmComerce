# -*- coding: utf-8 -*-


from meeting.models import Meeting


def search(request):
    meet = Meeting.objects.filter(meet_archiv=False, meet_trash=False)
    try:
        if request.get('search_meet_rieltor'):
            meet = meet.filter(rieltor__in=request.getlist('search_meet_rieltor'))
        if request.get('data_to'):
            meet = meet.filter(meet_date__gte=request.get('data_to'))
        if request.get('data_from'):
            meet = meet.filter(meet_date__lte=request.get('data_from'))
        if request.get('complexity') != '-----':
            meet = meet.filter(meet_status=request.get('status'))
        return meet
    except:
        return meet
