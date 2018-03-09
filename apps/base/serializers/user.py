#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
@version: v1.0
@author: cm
@time: 28/02/2018 4:43 PM
"""

__all__ = [
    'UserSerializer',
    'UserShortSerializer',
    'PasswordResetSerializer',
]

from rest_framework import serializers

from ..models import User


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'name',
            'mobile',
            'gender',
            'avatar',
            'experience',
            'score',
            'tenant',
            'department',
            'team',
            'last_login',
            'password1',
            'password2',
        )

    def validate(self, data):
        # 两次输入密码必须一致
        if data.get('password1') != data.get('password2'):
            raise serializers.ValidationError('密码两次输入不一致')

        # 若密码两次一致，进行django默认的密码规则校验
        from django.contrib.auth.password_validation import validate_password
        validate_password(data.get('password1'))

        return data

    def create(self, validated_data):
        validated_data.pop('password1')
        password2 = validated_data.pop('password2')

        # 设置用户密码
        user = User(**validated_data)
        user.set_password(password2)

        user.save()
        return user


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'uid',
            'username',
            'name',
        )


class PasswordResetSerializer(serializers.ModelSerializer):
    """用于用户重置密码
    """
    password = serializers.CharField(required=True)
    password1 = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = (
            'password',
            'password1',
            'password2',
        )

    # 密码校验
    def validate(self, data):
        # 校验原始密码
        if not self.instance.check_password(data.get('password')):
            raise serializers.ValidationError('原始密码输入错误')

        # 两次输入密码必须一致
        if data.get('password1') != data.get('password2'):
            raise serializers.ValidationError('修改密码两次输入不一致')

        # 若修改密码两次一致，进行django默认的密码规则校验
        from django.contrib.auth.password_validation import validate_password
        validate_password(data.get('password2'))

        return data

    # 重写update方法，save之前，通过set_password设置用户密码
    def update(self, instance, validated_data):
        instance.set_password(validated_data['password2'])
        instance.save()
        return instance
