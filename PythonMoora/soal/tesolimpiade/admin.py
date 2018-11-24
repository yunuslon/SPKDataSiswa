from django.contrib import admin
from orm.models import TesOlimpiade

class TesolimpiadeAdmin(admin.ModelAdmin):
    pass
admin.site.register(TesOlimpiade, TesolimpiadeAdmin)

# Register your models here.
