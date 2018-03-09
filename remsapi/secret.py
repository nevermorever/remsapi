#!/usr/bin/env python3
# -*- coding=utf-8 -*-

""" 
@version: v1.0 
@author: cm   
@time: 04/03/2018 11:40 PM 
"""

import string
import random


def generate_key():
    """
    Generates the key.
    """
    uni = string.ascii_letters + string.digits + string.punctuation
    key = ''.join([random.SystemRandom().choice(uni) for i in range(random.randint(45, 50))])
    return key
