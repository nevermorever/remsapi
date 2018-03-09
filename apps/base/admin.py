from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from mptt.admin import DraggableMPTTAdmin
from .models import *

admin.site.site_header = '梯+后台管理系统'
admin.site.site_title = '梯+后台管理系统'


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'tel', 'created', 'modified',)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        'name',
        'mobile',
        'tenant',
        'department',
        'gender',
        'email',
        'avatar',
        'last_login',
        'is_active',
        'is_staff'
    )
    search_fields = ('name', 'mobile', 'email')
    ordering = ('-created',)
    fieldsets = (
        (None, {'fields': ('mobile', 'password')}),
        ('个人信息',
         {'fields': ('tenant', 'department', 'name', 'gender', 'mobile', 'email', 'avatar', 'experience', 'score')}),
        ('权限', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('重要日期', {'fields': ('last_login', 'date_joined')}),
    )


@admin.register(Department)
class DepartmentAdmin(DraggableMPTTAdmin):
    pass


@admin.register(Area)
class AreaAdmin(DraggableMPTTAdmin):
    pass


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'hx_group_id', 'created', 'modified')


@admin.register(UserTeamRelation)
class UserTeamRelationAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'created', 'modified')
