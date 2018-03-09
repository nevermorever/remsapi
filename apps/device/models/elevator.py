#!/usr/bin/env python3
# -*- coding=utf-8 -*-

""" 
@version: v1.0 
@author: cm   
@time: 02/03/2018 10:09 AM 
"""

__all__ = ['Elevator']

from django.db import models
from base.models.tenant import TenantModelBase
from django.contrib.postgres.fields import ArrayField


class Elevator(TenantModelBase):
    name = models.CharField('使用编号', max_length=64)

    type = models.CharField(
        '梯型',
        choices=(
            ('elevator', '直梯'),
            ('escalator', '扶梯'),
        ),
        max_length=9,
        default='直梯'
    )

    sn = models.CharField('注册代码', max_length=20, unique=True)

    charge_ppl = models.ManyToManyField(
        'base.User',
        verbose_name='责任人',
        related_name='charged_elevators',
        blank=True
    )

    area = models.ForeignKey(
        'base.Area',
        verbose_name='安装区域',
        related_name='elevators',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    maintenance_org = models.CharField('维保单位', max_length=128, blank=True)

    maintenance_ppl = models.ManyToManyField(
        'base.User',
        verbose_name='维保人员',
        related_name='maintain_elevators',
        blank=True
    )

    maintenance_plan = models.ForeignKey('maintenance.MaintenancePlan', null=True, blank=True, on_delete=models.SET_NULL)

    # 设备基本参数
    manufacturer = models.CharField('制造厂家', max_length=64, blank=True)
    product_model = models.CharField('产品型号', max_length=64, blank=True)
    start_using_date = models.DateField('投入使用时间', null=True, blank=True)
    control_mode = models.CharField('控制类型', max_length=32, blank=True)
    main_motor_power = models.CharField('主电机功率', max_length=64, blank=True)
    lifting_height = models.CharField('提升高度', max_length=64, blank=True)
    rated_speed = models.CharField('额定速度', max_length=64, blank=True)
    rated_load = models.CharField('额定载重', max_length=64, blank=True)
    lng = models.CharField('经度', max_length=64, blank=True)
    lat = models.CharField('纬度', max_length=64, blank=True)
    next_inspection_date = models.DateField('下次检验日期', null=True, blank=True)
    ip = models.GenericIPAddressField('采集板ip地址', blank=True, null=True)
    is_online = models.BooleanField('是否在线', blank=True, default=False)

    # 楼层映射列表
    base_station = models.CharField(verbose_name='基站楼层', max_length=32, default=1, blank=True)
    station_mapping_list = ArrayField(
        models.CharField(max_length=3),
        verbose_name='层站名称映射表',
        null=True,
        blank=True
    )

    # 扶梯字段
    step_width = models.CharField('梯级宽度', max_length=64, blank=True)
    transport_capacity = models.CharField('输送能力', max_length=64, blank=True)
    use_segment_length = models.CharField('使用区段长度', max_length=64, blank=True)
    tilt_angle = models.CharField('倾斜角', max_length=64, blank=True)
    handrail_length = models.CharField('扶手带长度', max_length=64, blank=True)
    handrail_size = models.CharField('扶手带尺寸', max_length=64, blank=True)

    # 直梯字段
    door_open_mode = models.CharField('开门形式', max_length=32, blank=True)
    floor = models.PositiveIntegerField('层数', null=True, blank=True)
    station = models.PositiveIntegerField('站数', null=True, blank=True)
    pit_depth = models.CharField('底坑深度', max_length=64, blank=True)
    traction_machine_model = models.CharField('曳引机型号', max_length=64, blank=True)
    speed_limiter_model = models.CharField('限速器型号', max_length=64, blank=True)
    traction_wheel_diameter = models.CharField('曳引轮直径', max_length=64, blank=True)
    landing_door_size = models.CharField('厅门规格', max_length=64, blank=True)
    cable_diameter = models.CharField('钢丝绳直径', max_length=64, blank=True)
    buffer_model = models.CharField('缓冲器型号', max_length=64, blank=True)
    door_open_width = models.CharField('开门宽度', max_length=64, blank=True)
    top_floor_height = models.CharField('顶层高度', max_length=64, blank=True)
    reducer_speed_ratio = models.CharField('减速机速比', max_length=64, blank=True)
    main_motor_speed = models.CharField('主电机转速', max_length=64, blank=True)
    speed_limiter_action_speed = models.CharField('限速器动作速度', max_length=64, blank=True)
    door_motor_model = models.CharField('门机型号', max_length=64, blank=True)
    cage_size = models.CharField('轿箱尺寸', max_length=64, blank=True)
    safety_gea_model = models.CharField('安全钳型号', max_length=64, blank=True)
    well_size = models.CharField('井道尺寸', max_length=64, blank=True)
    usage = models.CharField('电梯用途', max_length=64, blank=True)
    door_control_system_type = models.CharField('门控系统类型', max_length=64, blank=True)
    have_power_failure_reflatfloor = models.BooleanField('断电再平层装置', blank=True, default=False)
    have_energy_feedback_system = models.BooleanField('有能量回馈系统', blank=True, default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'elevator'
        unique_together = ('tenant', 'name')
        verbose_name = verbose_name_plural = '电梯'
