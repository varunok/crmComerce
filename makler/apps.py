from django.apps import AppConfig
from watson import search as watson


class MaklerConfig(AppConfig):
    name = "makler"

    def ready(self):
        from makler.models import Makler
        watson.register(Makler)
