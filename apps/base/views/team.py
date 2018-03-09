#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
@version: v1.0
@author: cm
@time: 28/02/2018 4:47 PM
"""

__all__ = ['TeamViewSet']

from rest_framework import viewsets
from ..models import Team
from ..serializers import TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
