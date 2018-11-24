from django.contrib import admin
from orm.models import Bobot

class BobotAdmin(admin.ModelAdmin):
    pass
admin.site.register(Bobot, BobotAdmin)

# Register your models here.
