from django.contrib import admin
from .models import AnnualInspectionPlan, MaintenancePlan, MaintenanceRecord, RepairRecord


@admin.register(AnnualInspectionPlan)
class AnnualInspectionPlanAdmin(admin.ModelAdmin):
    pass


@admin.register(MaintenancePlan)
class MaintenancePlanAdmin(admin.ModelAdmin):
    pass


@admin.register(MaintenanceRecord)
class MaintenanceRecordAdmin(admin.ModelAdmin):
    pass


@admin.register(RepairRecord)
class RepairRecordAdmin(admin.ModelAdmin):
    pass
