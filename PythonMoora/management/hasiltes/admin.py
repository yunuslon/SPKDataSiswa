from django.contrib import admin
from orm.models import HasilTes

class HasilTesAdmin(admin.ModelAdmin):
    pass
admin.site.register(HasilTes, HasilTesAdmin)
