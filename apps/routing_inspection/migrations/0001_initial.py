# Generated by Django 2.0.2 on 2018-03-09 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoutingInspectionPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('title', models.CharField(max_length=128, verbose_name='标题')),
                ('is_active', models.BooleanField(default=False, verbose_name='生效')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Tenant', verbose_name='所属租户')),
            ],
            options={
                'verbose_name': '巡检计划',
                'verbose_name_plural': '巡检计划',
                'db_table': 'routing_inspection_plan',
            },
        ),
        migrations.CreateModel(
            name='RoutingInspectionRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='标题')),
            ],
            options={
                'verbose_name': '巡检记录',
                'verbose_name_plural': '巡检记录',
                'db_table': 'routing_inspection_record',
            },
        ),
    ]
