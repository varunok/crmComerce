from django.apps import AppConfig
from watson import search as watson


class ArendatorConfig(AppConfig):
    name = "arendator"

    def ready(self):
        from arendator.models import Arendator
        watson.register(Arendator)

