"""
@version: v1.0
@author: cm
@time: 02/03/2018 1:28 AM
"""

__all__ = ['AnnualInspectionPlan']

from django.db import models
from base.models import TenantModelBase
from django.contrib.postgres.fields import DateRangeField
import uuid


class AnnualInspectionPlan(TenantModelBase):
    """设备年度检验计划"""
    id = models.UUIDField('计划编号', default=uuid.uuid4, editable=False, primary_key=True)
    planned_time = DateRangeField('计划预定时间')
    is_active = models.BooleanField('是否启用', default=False, blank=True)
    executors = models.ManyToManyField('base.User', verbose_name='执行人', blank=True)
    desc = models.TextField('备注', blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'annual_inspection_plan'
        verbose_name = verbose_name_plural = '年度检验计划'
