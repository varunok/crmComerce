# -*- coding: utf-8 -*-


from django.forms import ModelForm, SelectMultiple, Textarea, DateTimeField
from meeting.models import Meeting


class MeetingForm(ModelForm):
    # format_date = ['%Y-%m-%d %H:%M:%S',    # '2006-10-25 14:30:59'
    #                '%Y-%m-%d %H:%M',       # '2006-10-25 14:30'
    #                '%Y-%m-%d',             # '2006-10-25'
    #                '%m/%d/%Y %H:%M:%S',    # '10/25/2006 14:30:59'
    #                '%m/%d/%Y %H:%M',       # '10/25/2006 14:30'
    #                '%m/%d/%Y',             # '10/25/2006'
    #                '%m/%d/%y %H:%M:%S',    # '10/25/06 14:30:59'
    #                '%m/%d/%y %H:%M',       # '10/25/06 14:30'
    #                '%m/%d/%y']
    # meet_date = DateTimeField(input_formats=format_date)
    class Meta:
        model = Meeting
        fields = ('meet_date', 'meet_facility', 'meet_arendator', 'meet_buyer', 'access', 'rieltor', 'meet_status',
                  'meet_comment')
        widgets = {
            'access': SelectMultiple(attrs={'class': 'multiple', 'multiple': 'multiple'}),
            'meet_comment': Textarea(attrs={'cols': '30', 'rows': '7'})
        }

