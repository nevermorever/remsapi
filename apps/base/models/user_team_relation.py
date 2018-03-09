#!/usr/bin/env python3
# -*- coding=utf-8 -*-

""" 
@version: v1.0 
@author: cm   
@time: 08/03/2018 6:54 PM 
"""

__all__ = ['UserTeamRelation']

from django.db import models
from .tenant import TenantModelBase


class UserTeamRelation(TenantModelBase):
    user = models.ForeignKey(
        'base.User',
        on_delete=models.CASCADE
    )

    team = models.ForeignKey(
        'base.Team',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{}-{}'.format(self.user, self.team)

    class Meta:
        db_table = 'user_team_relation'
        unique_together = ('user', 'team')
        verbose_name = verbose_name_plural = '用户团队关系'
