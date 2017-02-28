from django.apps import AppConfig
from watson import search as watson


class BuyerConfig(AppConfig):
    name = "buyer"

    def ready(self):
        from buyer.models import Buyer
        watson.register(Buyer)

