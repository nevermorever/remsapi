#!/usr/bin/env python3
# -*- coding=utf-8 -*-

""" 
@version: v1.0 
@author: cm   
@time: 02/03/2018 10:09 AM 
"""
__all__ = ['Team']

from django.db import models
from .tenant import TenantModelBase


class Team(TenantModelBase):
    """团队"""

    name = models.CharField(
        '名称',
        max_length=256,
        # default='test'
    )

    hx_group_id = models.CharField(
        '环信聊天群组id',
        max_length=128,
        blank=True,
        editable=False
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'team'
        # unique_together = ('tenant', 'name')
        verbose_name = verbose_name_plural = '团队'
