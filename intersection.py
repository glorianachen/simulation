#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 21:36:26 2020

@author: chenjiayu
"""

import time
from scipy import stats
import random
import numpy as np
import threading


def intersection(bus):
    # r is the poisson generated number of cars when a bus gets in intersection, 10 estimated as mean
    r = stats.poisson.rvs(3, size=1)
    r=r[0]
    def timerprint():
        print('bus starts and goes through intersection at'+str(time.time()))
    print('bus enter intersection')
    if r>=5:
        """
        here time is absolute, need replace with the one in main. Use the relative time .
        """
        print('bus stops at intersection at'+str(time.time()))
        timer=threading.Timer(2*r,timerprint)
        timer.start()
    else:
        print('bus goes through intersection'+str(time.time()))
    """
    missing the coordinate changing part,need to unify standard usage
    """
