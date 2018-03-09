#!/usr/bin/env python3
# -*- coding=utf-8 -*-

""" 
@version: v1.0 
@author: cm   
@time: 02/03/2018 10:09 AM 
"""
__all__ = ['Department']

from django.db import models
from .tenant import TenantModelBase
from mptt.models import MPTTModel


class Department(MPTTModel, TenantModelBase):
    """部门"""

    name = models.CharField(
        '名称',
        max_length=256
    )

    parent = models.ForeignKey(
        'self',
        verbose_name='上级部门',
        null=True,
        blank=True,
        related_name='children',
        db_index=True,
        on_delete=models.SET_NULL
    )

    address = models.CharField(
        '地址',
        max_length=128,
        blank=True
    )

    tel = models.CharField(
        '联系电话',
        max_length=32,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'department'
        unique_together = (('tenant', 'name'), ('parent', 'name'))
        verbose_name = verbose_name_plural = '部门'
