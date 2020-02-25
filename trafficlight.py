#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 17:59:17 2020

@author: chenjiayu
"""

def checklight(timestamp):
    if timestamp%60<36:
        return (True,0)
    else:
        return (False,60-timestamp%60)