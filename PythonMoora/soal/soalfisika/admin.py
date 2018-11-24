from django.contrib import admin
from orm.models import SoalFisika

class SoalFisikaAdmin(admin.ModelAdmin):
    pass
admin.site.register(SoalFisika, SoalFisikaAdmin)
