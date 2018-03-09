#!/usr/bin/env python3
# -*- coding=utf-8 -*-

""" 
@version: v1.0 
@author: cm   
@time: 02/03/2018 1:30 AM 
"""

__all__ = [
    'Tenant',
    'TenantModelBase'
]

from django.db import models
from remsapi.common.models import ModelBase


class Tenant(ModelBase):
    """租户"""

    name = models.CharField(
        '名称',
        max_length=256,
        unique=True
    )

    address = models.CharField(
        '地址',
        max_length=256,
        blank=True
    )

    tel = models.CharField(
        '联系电话',
        max_length=32,
        blank=True
    )

    users_limit = models.PositiveIntegerField(
        '用户数限制',
        null=True,
        blank=True,
        default=100
    )

    is_supertenant = models.BooleanField(
        '是否超级租户',
        default=False
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tenant'
        verbose_name = verbose_name_plural = '租户'


class TenantModelBase(ModelBase):
    tenant = models.ForeignKey(
        'base.Tenant',
        null=True,
        blank=True,
        verbose_name='所属租户',
        on_delete=models.CASCADE
    )

    class Meta:
        abstract = True
