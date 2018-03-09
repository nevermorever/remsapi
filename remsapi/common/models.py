#!/usr/bin/env python3
# -*- coding=utf-8 -*-

""" 
@version: v1.0 
@author: cm   
@time: 28/02/2018 4:12 PM 
"""

from django.db import models


class ModelBase(models.Model):
    """
    common base model
    """

    created = models.DateTimeField(
        '创建时间',
        auto_now_add=True,
        null=True,
        blank=True
    )

    modified = models.DateTimeField(
        '修改时间',
        auto_now=True,
        null=True,
        blank=True
    )

    # 逻辑删除
    deleted = models.BooleanField(
        '是否删除',
        blank=True,
        default=False
    )

    def delete(self, using=None, keep_parents=False):
        self.deleted = True
        self.save()

    class Meta:
        abstract = True
