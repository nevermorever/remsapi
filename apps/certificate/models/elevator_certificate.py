#!/usr/bin/env python3
# -*- coding=utf-8 -*-

""" 
@version: v1.0 
@author: cm   
@time: 02/03/2018 10:09 AM 
"""

__all__ = ['ElevatorCertificate']

from django.db import models
from base.models import TenantModelBase


class ElevatorCertificate(TenantModelBase):
    """电梯准用证"""

    certificate_number = models.CharField(
        '证书编号',
        max_length=128,
        unique=True
    )

    elevator = models.ForeignKey(
        'device.Elevator',
        verbose_name='所属电梯',
        on_delete=models.CASCADE
    )

    file = models.FileField(
        '附件',
        upload_to='certificate'
    )

    def __str__(self):
        return self.certificate_number

    class Meta:
        db_table = 'elevator_certificate'
        verbose_name = verbose_name_plural = '电梯准用证'
