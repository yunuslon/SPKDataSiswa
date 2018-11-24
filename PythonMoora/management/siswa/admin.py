from django.contrib import admin
from orm.models import Siswa 

class SiswaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Siswa, SiswaAdmin)
