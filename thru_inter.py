#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 18:03:58 2020

@author: chenjiayu
"""
from trafficlight import checklight
import random
def thru_intersection(bus,intersection):
    distance=intersection.distance
    ######
    delay1=int(distance/15.6)
    temptime=bus.timestamp+delay1
    check=checklight(temptime)
    if check[0]:
        delay2=0
    else:
        delay2=check[1]
    delay3=3+2.87*random.randint(1,10)
    delay=int(delay1+delay2+delay3)
    tempid=intersection.id
    bus.timestamp+=delay
    if tempid+1<=max(list(Distance.keys())):
        if tempid+1 in Busstoplist:
            scheduler.schedule( Event( bus,EventData( 'arrival' ,Component(tempid+1, 'busArrival',delay)) ) )
        else:
            scheduler.schedule( Event( bus,EventData( 'thru_intersection' ,Component(tempid+1, 'thru_intersection',delay )) ) )
