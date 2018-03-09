#!/usr/bin/env python3
# -*- coding=utf-8 -*-

""" 
@version: v1.0 
@author: cm   
@time: 02/03/2018 1:30 AM 
"""

__all__ = ['AreaFilter']

from django_filters import rest_framework as filters
from ..models import Area


class AreaFilter(filters.FilterSet):
    class Meta:
        model = Area
        fields = {
            'name': ['exact', 'icontains'],
        }
