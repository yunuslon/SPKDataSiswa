from django.contrib import admin
from orm.models import Kelas

class KelasAdmin(admin.ModelAdmin):
    pass
admin.site.register(Kelas, KelasAdmin)
