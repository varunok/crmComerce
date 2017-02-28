from django.apps import AppConfig
from watson import search as watson


class ContactOwnerConfig(AppConfig):
    name = "facility"

    def ready(self):
        from facility.models import ContactOwner, AddressFacilityData
        watson.register(ContactOwner)
        watson.register(AddressFacilityData)
