#!/usr/bin/env python3
# -*- coding=utf-8 -*-

""" 
@version: v1.0 
@author: cm   
@time: 02/03/2018 10:09 AM 
"""

__all__ = ['RunDataRecord']

from django.db import models
from base.models import TenantModelBase


class RunDataRecord(TenantModelBase):
    """电梯运行数据统计"""
    elevator = models.ForeignKey('device.Elevator', verbose_name='所属电梯', on_delete=models.CASCADE)
    timestamp = models.DateTimeField('时间戳')
    opt_count = models.IntegerField('运行次数', null=True, blank=True, default=0)
    travel_count = models.IntegerField('运行趟数', null=True, blank=True, default=0)
    door_open_close_count = models.IntegerField('开关门次数', null=True, blank=True, default=0)
    rope_bend_count = models.IntegerField('钢丝绳弯折次数', null=True, blank=True, default=0)

    def __str__(self):
        return self.timestamp

    class Meta:
        db_table = 'run_data_record'
        verbose_name = verbose_name_plural = '运行统计数据'
