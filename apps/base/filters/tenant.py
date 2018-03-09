#!/usr/bin/env python3
# -*- coding=utf-8 -*-

""" 
@version: v1.0 
@author: cm   
@time: 02/03/2018 1:30 AM 
"""

__all__ = ['TenantFilter']

from django_filters import rest_framework as filters
from ..models import Tenant


class TenantFilter(filters.FilterSet):
    class Meta:
        model = Tenant
        fields = {
            'name': ['exact', 'icontains'],
        }
