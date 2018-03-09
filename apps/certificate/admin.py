from django.contrib import admin
from .models import ElevatorCertificate, OperationCertificate


@admin.register(ElevatorCertificate)
class ElevatorCertificateAdmin(admin.ModelAdmin):
    pass


@admin.register(OperationCertificate)
class OperationCertificateAdmin(admin.ModelAdmin):
    pass
