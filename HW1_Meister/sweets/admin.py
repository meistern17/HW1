from django.contrib import admin
from sweets.models import Sweet

class SweetAdmin(admin.ModelAdmin):
    pass
admin.site.register(Sweet,SweetAdmin)
