#!/usr/bin/env python3
# -*- coding=utf-8 -*-

""" 
@version: v1.0 
@author: cm   
@time: 02/03/2018 10:09 AM 
"""

__all__ = ['News']

from django.db import models


class News(models.Model):
    title = models.CharField(
        '标题',
        max_length=128
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = '新闻'
