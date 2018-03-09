from django.contrib import admin
from .models import FaultRecord, AlarmPolicy


@admin.register(FaultRecord)
class FaultRecordAdmin(admin.ModelAdmin):
    pass


@admin.register(AlarmPolicy)
class AlarmPolicyAdmin(admin.ModelAdmin):
    pass
