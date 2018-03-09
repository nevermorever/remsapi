#!/usr/bin/env python3
# -*- coding=utf-8 -*-

""" 
@version: v1.0 
@author: cm   
@time: 02/03/2018 10:13 AM 
"""

__all__ = ['TeamSerializer']

from rest_framework import serializers
from ..models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
