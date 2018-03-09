#!/usr/bin/env python3
# -*- coding=utf-8 -*-

""" 
@version: v1.0 
@author: cm   
@time: 02/03/2018 10:09 AM 
"""

__all__ = ['Camera']

from django.db import models
from base.models import TenantModelBase


class Camera(TenantModelBase):
    LOCATION_CHOICES = (
        ('cage', '电梯轿箱'),
        ('machine_room', '电梯机房'),
        ('hall', '电梯大厅'),
        ('other', '其他位置'),
    )
    name = models.CharField('名称', max_length=64)
    brand = models.CharField('品牌', max_length=32, blank=True)
    elevator = models.ForeignKey(
        'device.Elevator',
        verbose_name='所属电梯',
        related_name='cameras',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    install_location = models.CharField('安装位置', max_length=32, choices=LOCATION_CHOICES, default='other')
    ip = models.GenericIPAddressField('IP地址', max_length=15, null=True, blank=True)
    account = models.CharField('登录帐号', max_length=32)
    password = models.CharField('登录密码', max_length=32)
    rtsp_src = models.CharField('rtsp源地址', max_length=128)
    rtmp_addr = models.CharField('rtmp播放地址', max_length=128, null=True, blank=True)
    stream_pushed = models.BooleanField('是否已开启推流', default=False, blank=True)
    ffmpeg_pid = models.IntegerField('ffmpeg进程id', null=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        super(Camera, self).save(*args, **kwargs)
        self.rtmp_addr = 'rtmp://localhost:1935/live/{}'.format(self.id)
        super(Camera, self).save()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'camera'
        verbose_name = verbose_name_plural = '摄像头'
