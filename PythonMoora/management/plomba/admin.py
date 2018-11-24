from django.contrib import admin
from orm.models import Plomba

class PlombaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Plomba, PlombaAdmin)
