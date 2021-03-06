# Generated by Django 2.0.2 on 2018-03-09 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('name', models.CharField(max_length=64, verbose_name='名称')),
                ('version', models.CharField(max_length=32, unique=True, verbose_name='版本')),
                ('platform', models.CharField(choices=[('android', '安卓'), ('ios', 'ios')], max_length=16, verbose_name='平台')),
                ('source', models.FileField(upload_to='apk', verbose_name='资源')),
            ],
            options={
                'verbose_name': 'apk',
                'verbose_name_plural': 'apk',
                'db_table': 'apk',
            },
        ),
    ]
