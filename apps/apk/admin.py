from django.contrib import admin

from .models import Apk


@admin.register(Apk)
class ApkAdmin(admin.ModelAdmin):
    list_display = ('name', 'platform', 'version', 'source')
