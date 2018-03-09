#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
@version: v1.0
@author: cm
@time: 28/02/2018 4:47 PM
"""

__all__ = ['UserViewSet']

from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from remsapi.common.permissions import IsAdminOrIsSelf
from ..models import User
from .. import serializers
from ..filters import UserFilter
from remsapi.common.paginations import BasePagination


class UserViewSet(ModelViewSet):
    """
    匿名用户返回空值
    admin用户返回所有
    非admin，非匿名用户返回自身
    """
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAuthenticated, IsAdminOrIsSelf,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = UserFilter
    pagination_class = BasePagination
    model = User

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        else:
            return User.objects.filter(pk=self.request.user.pk)

    @list_route(['GET'])
    def mine(self, request):
        """
        查看个人信息
        只允许登陆用户访问
        """
        return Response(self.get_serializer(request.user).data)

    @list_route(
        methods=['POST'],
        url_path='password',
        serializer_class=serializers.PasswordResetSerializer
    )
    def password(self, request):
        """
        修改密码
        """
        serializer = self.get_serializer(request.user, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'detail': '修改密码成功'},
        )
