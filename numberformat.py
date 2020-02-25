#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 17:33:13 2020

@author: chenjiayu
"""

import datetime
import time

def timestampToStr( timestamp ):
    timeArray = time.localtime(timestamp)
    StyleTime = time.strftime("%Y-%b-%d %a %H:%M:%S", timeArray)

    return StyleTime

