from django.contrib import admin
import arendator.models
# Register your models here.

admin.site.register(arendator.models.Arendator)
admin.site.register(arendator.models.TypeState)
admin.site.register(arendator.models.TypeClient)
admin.site.register(arendator.models.TypeStage)
