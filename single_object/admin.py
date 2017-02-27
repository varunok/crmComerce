from django.contrib import admin
import single_object.models
# Register your models here.
admin.site.register(single_object.models.TypeShows)
admin.site.register(single_object.models.SingleObjComments)
admin.site.register(single_object.models.Tie)
admin.site.register(single_object.models.TieBuyer)