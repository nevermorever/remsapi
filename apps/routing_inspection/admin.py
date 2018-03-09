from django.contrib import admin
from .models import RoutingInspectionPlan, RoutingInspectionRecord


@admin.register(RoutingInspectionPlan)
class RoutingInspectionPlanAdmin(admin.ModelAdmin):
    pass


@admin.register(RoutingInspectionRecord)
class RoutingInspectionRecordAdmin(admin.ModelAdmin):
    pass
