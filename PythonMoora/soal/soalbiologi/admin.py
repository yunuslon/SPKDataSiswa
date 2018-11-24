from django.contrib import admin
from orm.models import SoalBiologi

class SoalBiologiAdmin(admin.ModelAdmin):
    pass
admin.site.register(SoalBiologi, SoalBiologiAdmin)
