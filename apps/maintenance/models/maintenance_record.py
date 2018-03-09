#!/usr/bin/env python3
# -*- coding=utf-8 -*-

""" 
@version: v1.0 
@author: cm   
@time: 08/03/2018 12:20 AM 
"""

__all__ = ['MaintenanceRecord']

from base.models import TenantModelBase
from django.db import models
from django.contrib.postgres.fields import JSONField, DateRangeField, DateTimeRangeField
import uuid


class MaintenanceRecord(TenantModelBase):
    STATUS_CHOICES = (
        ('已完成', '已完成'),
        ('已超期', '已超期'),
    )
    TYPE_CHOICES = (
        ('半月保', '半月保'),
        ('季度保', '季度保'),
        ('半年保', '半年保'),
        ('年度保', '年度保'),
    )
    id = models.UUIDField('记录编号', default=uuid.uuid4, editable=False, primary_key=True)
    type = models.CharField('维保类型', choices=TYPE_CHOICES, max_length=32)
    elevator = models.ForeignKey('device.Elevator', verbose_name='所属电梯', on_delete=models.CASCADE)
    planned_time = DateRangeField('计划预定时间')
    actual_execution_time = DateTimeRangeField('实际执行时间', null=True, blank=True)
    execution_status = models.CharField(
        '执行状态',
        max_length=32,
        choices=STATUS_CHOICES,
        blank=True
    )
    executors = models.ManyToManyField('base.User', verbose_name='计划执行人', blank=True)
    execution_result = JSONField(verbose_name='执行结果', null=True, blank=True)
    desc = models.TextField('备注', blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'maintenance_record'
        verbose_name = verbose_name_plural = '保养记录'
