from django.contrib import admin
from .models import DutyRecord, CallRecord


@admin.register(DutyRecord)
class DutyRecordAdmin(admin.ModelAdmin):
    pass


@admin.register(CallRecord)
class CallRecordAdmin(admin.ModelAdmin):
    pass
