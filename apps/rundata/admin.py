from django.contrib import admin
from .models import RunDataRecord


@admin.register(RunDataRecord)
class RunDataRecordAdmin(admin.ModelAdmin):
    pass
