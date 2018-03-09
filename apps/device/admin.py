from django.contrib import admin
from .models import Elevator, Camera, Terminal


@admin.register(Elevator)
class ElevatorAdmin(admin.ModelAdmin):
    pass


@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    pass


@admin.register(Terminal)
class TerminalAdmin(admin.ModelAdmin):
    pass
