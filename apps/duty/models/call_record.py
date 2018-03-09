#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
@version: v1.0
@author: cm
@time: 02/03/2018 1:28 AM
"""

__all__ = ['CallRecord']

from django.db import models
from base.models import TenantModelBase


class CallRecord(TenantModelBase):
    """
    来电记录
    """
    CALL_REASON_CHOICES = (
        ('报修', '报修'),
        ('申请运货', '申请运货'),
        ('拾物', '拾物'),
        ('投诉', '投诉'),
        ('其他', '其他'),
    )

    HANDLE_STATUS_CHOICES = (
        ('待处理', '待处理'),
        ('处理中', '处理中'),
        ('已处理', '已处理'),
    )

    call_number = models.CharField(
        '来电号码',
        max_length=32,
        blank=True
    )

    call_time = models.DateTimeField(
        '来电时间',
        blank=True,
        null=True
    )

    call_department = models.CharField(
        '来电科室',
        max_length=64,
        blank=True
    )

    call_reason = models.CharField(
        '来电事由',
        max_length=32,
        choices=()
    )

    area = models.ForeignKey(
        'base.Area',
        verbose_name='报修区域',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    elevator = models.ForeignKey(
        'device.Elevator',
        verbose_name='报修电梯',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    call_content = models.TextField(
        '来电明细',
        max_length=512,
        blank=True
    )

    recover_time = models.DateTimeField(
        '电梯恢复时间',
        null=True,
        blank=True
    )

    on_duty_ppl = models.ForeignKey(
        'base.User',
        verbose_name='值班人员',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    handle_result = models.TextField(
        '处理结果',
        max_length=512,
        blank=True
    )

    handle_status = models.CharField(
        '处理状态',
        max_length=32,
        choices=HANDLE_STATUS_CHOICES,
        default='待处理',
        blank=True
    )

    def __str__(self):
        return '{}-{}'.format(self.call_number, self.call_reason)

    class Meta:
        db_table = 'call_record'
        verbose_name = verbose_name_plural = '电话记录'
