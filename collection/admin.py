from django.contrib import admin
# import your model
from collection.models import Thing


# set up automated slug creation
class ThingAdmin(admin.ModelAdmin):
    models =Thing
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',),}


# register
admin.site.register(Thing, ThingAdmin)

