from django.contrib import admin
from orm.models import Karakter

class KarakterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Karakter, KarakterAdmin)
