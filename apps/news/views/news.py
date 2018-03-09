#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
@version: v1.0
@author: cm
@time: 28/02/2018 4:47 PM
"""

__all__ = ['NewsViewSet']

from rest_framework import viewsets
from ..models import News
from ..serializers import NewsSerializer
from remsapi.common.permissions import IsSupertenantOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().only('title')
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsSupertenantOrReadOnly,)
