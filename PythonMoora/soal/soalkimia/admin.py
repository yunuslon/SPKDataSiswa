from django.contrib import admin
from orm.models import SoalKimia

class SoalKimiaAdmin(admin.ModelAdmin):
    pass
admin.site.register(SoalKimia, SoalKimiaAdmin)
