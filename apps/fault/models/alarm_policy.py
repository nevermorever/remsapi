#!/usr/bin/env python3
# -*- coding=utf-8 -*-

""" 
@version: v1.0 
@author: cm   
@time: 09/03/2018 11:13 AM 
"""

__all__ = ['AlarmPolicy']

from django.db import models
from base.models import TenantModelBase


class AlarmPolicy(TenantModelBase):
    """告警策略"""

    is_active = models.BooleanField(
        '生效',
        blank=True,
        default=False
    )

    enable_sms_message_notify = models.BooleanField(
        '启用短信提示',
    )

    enable_app_message_push = models.BooleanField(
        '启用app消息推送',
    )

    elevator = models.ManyToManyField(
        'device.Elevator',
        verbose_name='适用电梯',
        blank=True
    )

    def __str__(self):
        return ""

    class Meta:
        db_table = 'alarm_policy'
        verbose_name_plural = verbose_name = '告警策略'
