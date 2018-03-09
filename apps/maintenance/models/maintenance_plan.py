#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
@version: v1.0
@author: cm
@time: 02/03/2018 1:28 AM
"""

__all__ = ['MaintenancePlan']

from django.db import models
from base.models import TenantModelBase
from django.contrib.postgres.fields import JSONField, DateRangeField
import uuid


class MaintenancePlan(TenantModelBase):
    TYPE_CHOICES = (
        ('半月保', '半月保'),
        ('季度保', '季度保'),
        ('半年保', '半年保'),
        ('年度保', '年度保'),
    )

    id = models.UUIDField('计划编号', default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField('计划名称', max_length=128, null=True, blank=True)
    type = models.CharField('保养类型', choices=TYPE_CHOICES, max_length=32)
    maintenance_items = JSONField(verbose_name='保养项目', null=True, blank=True)
    planned_time = DateRangeField('计划预定时间')
    is_active = models.BooleanField('是否启用', default=False, blank=True)
    executors = models.ManyToManyField('base.User', verbose_name='计划执行人', blank=True)
    desc = models.TextField('备注', blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'maintenance_plan'
        verbose_name = verbose_name_plural = '保养计划'
