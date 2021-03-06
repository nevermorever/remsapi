# Generated by Django 2.0.2 on 2018-03-09 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        ('device', '0001_initial'),
        ('certificate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='elevatorcertificate',
            name='elevator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.Elevator', verbose_name='所属电梯'),
        ),
        migrations.AddField(
            model_name='elevatorcertificate',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Tenant', verbose_name='所属租户'),
        ),
    ]
