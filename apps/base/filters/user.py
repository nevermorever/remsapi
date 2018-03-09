#!/usr/bin/env python3
# -*- coding=utf-8 -*-

""" 
@version: v1.0 
@author: cm   
@time: 28/02/2018 4:25 PM 
"""
__all__ = ['UserFilter']

from django_filters import rest_framework as filters
from ..models import User


class UserFilter(filters.FilterSet):
    ordering = filters.OrderingFilter(
        fields=('date_joined', 'score', 'experience')
    )

    class Meta:
        model = User
        fields = {
            'username': ['exact', 'icontains'],
            'name': ['exact', 'icontains'],
            'mobile': ['exact'],
            'gender': ['exact'],
            'experience': ['exact', 'gte', 'lte'],
            'score': ['exact', 'gte', 'lte'],
            'is_active': ['exact'],
        }
