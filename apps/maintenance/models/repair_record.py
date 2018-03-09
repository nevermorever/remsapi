#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
@version: v1.0
@author: cm
@time: 02/03/2018 1:28 AM
"""

__all__ = ['RepairRecord']

from django.db import models
from base.models import TenantModelBase


class RepairRecord(TenantModelBase):
    """
    维修记录
    """
    TYPE_CHOICES = (
        ('一般维修', '一般维修'),
        ('大修', '大修'),
        ('改造', '改造'),
    )

    type = models.CharField(
        '维修类型',
        max_length=32,
        choices=TYPE_CHOICES,
        blank=True,
        default='一般维修'
    )

    elevator = models.ForeignKey('device.Elevator', verbose_name='所属电梯', on_delete=models.CASCADE)
    start_time = models.DateTimeField('开始时间', null=True, blank=True)
    end_time = models.DateTimeField('结束时间', null=True, blank=True)
    executors = models.ManyToManyField('base.User', verbose_name='维修执行人', blank=True)
    check_content = models.TextField('检查内容', blank=True)
    repair_content = models.TextField('维修内容', blank=True)
    fittings_replace = models.TextField('配件更换', blank=True)
    desc = models.TextField('备注', blank=True)
    call_record = models.OneToOneField(
        'duty.CallRecord',
        verbose_name='对应电话记录',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.elevator.name.join('值班维修记录')

    class Meta:
        db_table = 'repair_record'
        verbose_name = verbose_name_plural = '维修记录'
