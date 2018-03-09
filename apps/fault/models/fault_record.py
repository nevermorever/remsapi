#!/usr/bin/env python3
# -*- coding=utf-8 -*-

""" 
@version: v1.0 
@author: cm   
@time: 08/03/2018 1:24 AM 
"""

__all__ = ['FaultRecord']

from base.models import TenantModelBase
from django.db import models
from django.contrib.postgres.fields import JSONField
import uuid


class FaultRecord(TenantModelBase):
    """故障记录"""

    RECORD_FROM_CHOICES = (
        ('电话报修', '电话报修'),
        ('班组自查', '班组自查'),
        ('系统检测', '系统检测'),
    )

    HANDLE_STATUS_CHOICES = (
        ('未处理', '未处理'),
        ('处理中', '处理中'),
        ('已处理', '已处理'),
    )

    id = models.UUIDField(
        '故障编号',
        primary_key=True,
        unique=True,
        default=uuid.uuid4
    )

    record_from = models.CharField(
        '故障生成形式',
        max_length=32,
        choices=RECORD_FROM_CHOICES,
        blank=True
    )

    elevator = models.ForeignKey(
        'device.Elevator',
        verbose_name='故障电梯',
        on_delete=models.CASCADE
    )

    fault_code = models.CharField(
        '故障代码',
        max_length=32,
    )

    # 填写手工故障单时需要此字段
    fault_desc = models.TextField(
        '故障现象描述',
        blank=True
    )

    occur_time = models.DateTimeField(
        '发生时间',
        null=True,
        blank=True
    )

    ppl_traped = models.BooleanField(
        '是否困人',
        blank=True,
        default=False
    )

    #  故障处理状态
    handle_status = models.CharField(
        '处理状态',
        choices=HANDLE_STATUS_CHOICES,
        max_length=32,
        default='未受理',
        blank=True
    )

    execution_ppl = models.ManyToManyField(
        'base.User',
        verbose_name='执行人',
        blank=True
    )

    handle_time = models.DateTimeField(
        '受理时间',
        null=True,
        blank=True
    )

    handle_result = models.TextField(
        '处理结果',
        blank=True
    )

    end_time = models.DateTimeField(
        '结束时间',
        null=True,
        blank=True
    )

    desc = models.TextField(
        '备注',
        blank=True
    )

    # 故障发生时的系统状态
    run_status = JSONField(
        '故障时刻电梯运行状态',
        null=True,
        blank=True
    )

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table = 'fault_record'
        verbose_name_plural = verbose_name = '故障记录'
