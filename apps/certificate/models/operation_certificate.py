#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
@version: v1.0
@author: cm
@time: 02/03/2018 10:09 AM
"""

__all__ = ['OperationCertificate']

from django.db import models
from base.models import TenantModelBase


class OperationCertificate(TenantModelBase):
    """操作证"""

    certificate_number = models.CharField(
        '证书编号',
        max_length=128,
        unique=True
    )

    user = models.ForeignKey(
        'base.User',
        verbose_name='所属人员',
        on_delete=models.CASCADE
    )

    file = models.FileField(
        '附件',
        upload_to='user_license'
    )

    def __str__(self):
        return self.certificate_number

    class Meta:
        db_table = 'operation_certificate'
        verbose_name = verbose_name_plural = '人员操作证'
