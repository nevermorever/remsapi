#!/usr/bin/env python3
# -*- coding=utf-8 -*-

""" 
@version: v1.0 
@author: cm   
@time: 02/03/2018 10:09 AM 
"""

__all__ = ['DutyRecord']

from django.db import models
from base.models import TenantModelBase


class DutyRecord(TenantModelBase):
    class Meta:
        db_table = 'duty_record'
        verbose_name = verbose_name_plural = '值班记录'
