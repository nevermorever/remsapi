#!/usr/bin/env python3
# -*- coding=utf-8 -*-

""" 
@version: v1.0 
@author: cm   
@time: 28/02/2018 4:25 PM 
"""

__all__ = ['User']

from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from .tenant import TenantModelBase


class User(TenantModelBase, AbstractBaseUser, PermissionsMixin):
    """用户表"""

    mobile = models.CharField(
        '手机号码',
        max_length=11,
        unique=True
    )

    name = models.CharField(
        '姓名',
        max_length=20,
        blank=True
    )

    email = models.EmailField(
        '邮箱',
        blank=True
    )

    gender = models.CharField(
        '性别',
        max_length=6,
        choices=(
            ('male', '男'),
            ('female', '女')
        ),
        blank=True
    )

    avatar = models.ImageField(
        '头像',
        upload_to='avatar',
        null=True,
        blank=True,
        default='avatar/default.jpg'
    )

    experience = models.PositiveIntegerField(
        '经验',
        null=True,
        blank=True,
        default=0
    )

    score = models.PositiveIntegerField(
        '积分',
        null=True,
        blank=True,
        default=0
    )

    department = models.ForeignKey(
        'base.Department',
        verbose_name='所属部门',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='users'
    )

    teams = models.ManyToManyField(
        'base.Team',
        verbose_name='团队',
        blank=True,
        through='base.UserTeamRelation',
        related_name='users',
    )

    is_staff = models.BooleanField(
        '职员状态',
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ['email']

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.mobile

    class Meta:
        db_table = 'user'
        verbose_name = verbose_name_plural = '用户'
