#!/usr/bin/env python3
# -*- coding=utf-8 -*-

""" 
@version: v1.0 
@author: cm   
@time: 02/03/2018 10:09 AM 
"""

__all__ = ['RoutingInspectionRecord']

from django.db import models
from base.models import TenantModelBase


class RoutingInspectionRecord(TenantModelBase):
    title = models.CharField(
        '标题',
        max_length=128
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'routing_inspection_record'
        verbose_name = verbose_name_plural = '巡检记录'
