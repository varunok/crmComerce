# -*- coding: utf-8 -*-


import os
from django.conf import settings
from django.core import management
from django_cron import CronJobBase, Schedule


class Backup(CronJobBase):
    # RUN_AT_TIMES = ['6:00', '18:00']
    RUN_EVERY_MINS = 43200
    # schedule = Schedule(run_at_times=RUN_AT_TIMES)
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'crm.Backup'

    def do(self):
        management.call_command('dbbackup')
