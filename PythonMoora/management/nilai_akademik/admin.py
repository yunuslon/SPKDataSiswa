from django.contrib import admin
from orm.models import NilaiAkademik

class NilaiAkdemikAdmin(admin.ModelAdmin):
    pass
admin.site.register(NilaiAkademik, NilaiAkdemikAdmin)
