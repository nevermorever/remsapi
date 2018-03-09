#!/usr/bin/env python3
# -*- coding=utf-8 -*-

""" 
@version: v1.0 
@author: cm   
@time: 28/02/2018 4:13 PM 
"""

from rest_framework.pagination import PageNumberPagination


class BasePagination(PageNumberPagination):
    """
    分页
    """
    page_query_param = 'page'
    page_query_description = '页数'
    page_size_query_param = 'limit'
    page_size_query_description = '每页显示条数'
    page_size = 10
