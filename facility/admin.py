from django.contrib import admin
import facility.models
# Register your models here.

admin.site.register(facility.models.TypeFacility)
admin.site.register(facility.models.AddressFacilityData)
admin.site.register(facility.models.TypeOperations)
admin.site.register(facility.models.TypeContactOwner)
admin.site.register(facility.models.ContactOwner)
admin.site.register(facility.models.PhoneOwner)
admin.site.register(facility.models.TypeRepairs)
admin.site.register(facility.models.TypeActuality)
admin.site.register(facility.models.TypeCondition)
admin.site.register(facility.models.TypeHeating)
admin.site.register(facility.models.TypeLocations)
admin.site.register(facility.models.TypeStoreys)
admin.site.register(facility.models.TypeEntrance)
admin.site.register(facility.models.TypeDocumentation)
admin.site.register(facility.models.TypeUnderThat)
admin.site.register(facility.models.TypeAvailability)
