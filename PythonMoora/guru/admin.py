from django.contrib import admin
from orm.models import Guru

class GuruAdmin(admin.ModelAdmin):
    pass
admin.site.register(Guru, GuruAdmin)

# Register your models here.
