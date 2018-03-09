#!/usr/bin/env python3
# -*- coding=utf-8 -*-

""" 
@version: v1.0 
@author: cm   
@time: 02/03/2018 10:09 AM 
"""

__all__ = ['Terminal']

from django.db import models
from base.models import TenantModelBase
from .elevator import Elevator


class Terminal(TenantModelBase):
    LOCATION_CHOICES = (
        ('cage', '轿箱'),
        ('other', '其他'),
    )
    name = models.CharField('名称', max_length=128)
    ip = models.GenericIPAddressField('IP地址', max_length=32, null=True, blank=True)
    hx_id = models.CharField('环信ID', max_length=64, blank=True)
    elevator = models.ForeignKey(Elevator, verbose_name='所属电梯', null=True, blank=True, on_delete=models.SET_NULL)
    install_location = models.CharField('安装位置', max_length=16, choices=LOCATION_CHOICES, blank=True, default='cage')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'terminal'
        unique_together = ('tenant', 'name')
        verbose_name = verbose_name_plural = '显示终端'
