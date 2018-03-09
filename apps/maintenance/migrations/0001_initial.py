# Generated by Django 2.0.2 on 2018-03-09 03:54

from django.conf import settings
import django.contrib.postgres.fields.jsonb
import django.contrib.postgres.fields.ranges
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        ('device', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('duty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualInspectionPlan',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='计划编号')),
                ('planned_time', django.contrib.postgres.fields.ranges.DateRangeField(verbose_name='计划预定时间')),
                ('is_active', models.BooleanField(default=False, verbose_name='是否启用')),
                ('desc', models.TextField(blank=True, verbose_name='备注')),
                ('executors', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='执行人')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Tenant', verbose_name='所属租户')),
            ],
            options={
                'verbose_name': '年度检验计划',
                'verbose_name_plural': '年度检验计划',
                'db_table': 'annual_inspection_plan',
            },
        ),
        migrations.CreateModel(
            name='MaintenancePlan',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='计划编号')),
                ('name', models.CharField(blank=True, max_length=128, null=True, verbose_name='计划名称')),
                ('type', models.CharField(choices=[('半月保', '半月保'), ('季度保', '季度保'), ('半年保', '半年保'), ('年度保', '年度保')], max_length=32, verbose_name='保养类型')),
                ('maintenance_items', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='保养项目')),
                ('planned_time', django.contrib.postgres.fields.ranges.DateRangeField(verbose_name='计划预定时间')),
                ('is_active', models.BooleanField(default=False, verbose_name='是否启用')),
                ('desc', models.TextField(blank=True, verbose_name='备注')),
                ('executors', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='计划执行人')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Tenant', verbose_name='所属租户')),
            ],
            options={
                'verbose_name': '保养计划',
                'verbose_name_plural': '保养计划',
                'db_table': 'maintenance_plan',
            },
        ),
        migrations.CreateModel(
            name='MaintenanceRecord',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='记录编号')),
                ('type', models.CharField(choices=[('半月保', '半月保'), ('季度保', '季度保'), ('半年保', '半年保'), ('年度保', '年度保')], max_length=32, verbose_name='维保类型')),
                ('planned_time', django.contrib.postgres.fields.ranges.DateRangeField(verbose_name='计划预定时间')),
                ('actual_execution_time', django.contrib.postgres.fields.ranges.DateTimeRangeField(blank=True, null=True, verbose_name='实际执行时间')),
                ('execution_status', models.CharField(blank=True, choices=[('已完成', '已完成'), ('已超期', '已超期')], max_length=32, verbose_name='执行状态')),
                ('execution_result', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='执行结果')),
                ('desc', models.TextField(blank=True, verbose_name='备注')),
                ('elevator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.Elevator', verbose_name='所属电梯')),
                ('executors', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='计划执行人')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Tenant', verbose_name='所属租户')),
            ],
            options={
                'verbose_name': '保养记录',
                'verbose_name_plural': '保养记录',
                'db_table': 'maintenance_record',
            },
        ),
        migrations.CreateModel(
            name='RepairRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('type', models.CharField(blank=True, choices=[('一般维修', '一般维修'), ('大修', '大修'), ('改造', '改造')], default='一般维修', max_length=32, verbose_name='维修类型')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='开始时间')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='结束时间')),
                ('check_content', models.TextField(blank=True, verbose_name='检查内容')),
                ('repair_content', models.TextField(blank=True, verbose_name='维修内容')),
                ('fittings_replace', models.TextField(blank=True, verbose_name='配件更换')),
                ('desc', models.TextField(blank=True, verbose_name='备注')),
                ('call_record', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='duty.CallRecord', verbose_name='对应电话记录')),
                ('elevator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.Elevator', verbose_name='所属电梯')),
                ('executors', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='维修执行人')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Tenant', verbose_name='所属租户')),
            ],
            options={
                'verbose_name': '维修记录',
                'verbose_name_plural': '维修记录',
                'db_table': 'repair_record',
            },
        ),
    ]