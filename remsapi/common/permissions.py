#!/usr/bin/env python3
# -*- coding=utf-8 -*-

""" 
@version: v1.0 
@author: cm   
@time: 28/02/2018 4:51 PM 
"""

from rest_framework import permissions
from rest_framework.permissions import BasePermission


class AnyOf(BasePermission):
    """
    传入多个权限，其中之一满足即可
    """

    def __init__(self, *perms):
        # DRF调用permission_classes序列中的各个权限
        self.perms = [p() for p in perms]

    def has_permission(self, request, view):
        return any(perm.has_permission(request, view) for perm in self.perms)

    def has_object_permission(self, request, view, obj):
        # 注意此处，必须先检查每个子权限类的has_permission通过
        return any((perm.has_permission(request, view) and
                    perm.has_object_permission(request, view, obj))
                   for perm in self.perms)

    def __call__(self):
        return self


class IsAdminOrIsSelf(permissions.BasePermission):
    """
    只允许admin或者user自己操作个人信息
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user == obj:
            return True
        else:
            return False


class IsSupertenantOrReadOnly(permissions.BasePermission):
    """"""

    def has_permission(self, request, view):
        if request.method not in permissions.SAFE_METHODS and request.tenant.name != 'public':
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method not in permissions.SAFE_METHODS and request.tenant.name != 'public':
            return False
        return True
