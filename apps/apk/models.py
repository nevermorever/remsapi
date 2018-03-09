from django.db import models
from remsapi.common.models import ModelBase


class Apk(ModelBase):
    PLATFORM_CHOICES = (
        ('android', '安卓'),
        ('ios', 'ios'),
    )

    name = models.CharField(
        '名称',
        max_length=64,
    )

    version = models.CharField(
        '版本',
        max_length=32,
        unique=True,
    )

    platform = models.CharField(
        '平台',
        choices=PLATFORM_CHOICES,
        max_length=16
    )

    source = models.FileField(
        '资源',
        upload_to='apk'
    )

    def __str__(self):
        return self.version

    class Meta:
        db_table = 'apk'
        verbose_name_plural = verbose_name = 'apk'
