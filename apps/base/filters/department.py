#!/usr/bin/env python3
# -*- coding=utf-8 -*-

""" 
@version: v1.0 
@author: cm   
@time: 02/03/2018 1:30 AM 
"""

__all__ = ['DepartmentFilter']

from django_filters import rest_framework as filters
from ..models import Department


class DepartmentFilter(filters.FilterSet):
    class Meta:
        model = Department
        fields = {
            'name': ['exact', 'icontains'],
        }
