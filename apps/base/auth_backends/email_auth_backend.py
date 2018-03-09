#!/usr/bin/env python3
# -*- coding=utf-8 -*-

""" 
@version: v1.0 
@author: cm   
@time: 08/03/2018 2:50 PM 
"""

__all__ = ['EmailBackend']

from django.contrib.auth import get_user_model

User = get_user_model()


class EmailBackend(object):
    """
    email认证后端
    """

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            # 验证密码
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
