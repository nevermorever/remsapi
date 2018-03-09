#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
@version: v1.0
@author: cm
@time: 28/02/2018 4:47 PM
"""

__all__ = ['DepartmentViewSet']

from rest_framework import viewsets
from ..models import Department
from ..serializers import DepartmentSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
