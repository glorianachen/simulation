#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 21:43:26 2020

@author: chenjiayu
"""

import RanGenNew
RandomGenerator=RanGenNew.ClassRanGen()
import heapq,random
from numberformat import timestampToStr
from trafficlight import checklight
from thru_inter import thru_intersection
##total is the count of people boarding and alighting in busstops
total=[]
T=1000
t=T
class Event(object):
    def __init__( self,bus,eventData):
        self.bus=bus
        self.timestamp = bus.timestamp
        self.route = bus.route
        self.eventType = eventData.eventType
        self.componentType = eventData.component.componentType
        self.id = eventData.component.id
    def printSelf(self):
        print( 'its timestamp is %s ' % (timestampToStr(self.timestamp) ))
        print( 'its eventType is %s ' % (self.eventType))
        print( 'its componentType is %s ' % (self.componentType) )
    def __lt__(self, other):
        return self.timestamp < other.timestamp
    def __eq__(self, other):
        return self.timestamp == other.timestamp
class EventData(object):
    def __init__(self, eventType, Component):
        self.eventType = eventType
        self.component = Component
class Component(object):
    def __init__(self, comid, componentType, processingTime ):
        self.id = comid
        self.componentType = componentType
        self.processingTime = processingTime

class Scheduler():
    def __init__(self):
        self.time = 0
        self.FEL = []
    def schedule(self, event ):
        heapq.heappush(self.FEL,(event.timestamp,event))
    def runSim(self, eventHandler, endTime):
        while len(self.FEL)>0:
            nextEvent = heapq.heappop(self.FEL)[1]
            now = nextEvent.timestamp
            if now > endTime:
                break
            eventHandler.handle( nextEvent )

class EventHandeler(object):
    def __init__(self):
        pass
    def handle(self, event):
        if event.eventType == 'initiate':
            event.bus.busInitiate()
        elif event.eventType == 'arrival':
            busArrival(event.bus,Object[event.id])
        else:
            thru_intersection(event.bus,Object[event.id])
class Bus(object):
    def __init__(self, route, timestamp, capacity, scheduler,numOnRoad):
        self.route = route
        self.timestamp = timestamp
        self.numOnRoad=numOnRoad
        self.capacity = capacity
        #generator
        self.peopleOnBus = int(capacity*RandomGenerator.Rand())
        self.scheduler = scheduler
        
    def busInitiate(self):
        #speed?
        if self.route==94:
            delay=int(Distance[0]/15.6)
            self.timestamp += delay
            if 1 in Busstoplist:
                scheduler.schedule( Event( self, EventData( 'arrival' ,Component(1, 'busArrival',delay )) )) 
            else:
                scheduler.schedule( Event( self,EventData( 'thru_intersection' ,Component(1, 'thru_intersection',delay ))) ) 
        else:
            delay=int(Distance[1000]/15.6)
            self.timestamp += delay
            scheduler.schedule( Event( self, EventData( 'arrival' ,Component(1001, 'busArrival',delay )) )) 
            
class BusStop(object):
    def __init__(self, stopId,peoplecount):
        self.id = stopId
        self.peopleInStop = peoplecount
        self.distance=Distance[stopId]        
def busArrival(bus,busstop):
    tempid=busstop.id
    distance=busstop.distance
    ######
    delay=int(distance/15.6)
    bus.timestamp+=delay+10
    if tempid+1 in list(Distance.keys()):
        if tempid+1 in Busstoplist:
            scheduler.schedule( Event( bus, EventData( 'arrival' ,Component(tempid+1, 'busArrival',delay )) )) 
        else:
            scheduler.schedule( Event( bus,EventData( 'thru_intersection' ,Component(tempid+1, 'thru_intersection',delay ))) ) 
    ####calculate people boarding and alighting
    alight=int(bus.peopleOnBus*RandomGenerator.Rand())
  
    boarding=min(busstop.peopleInStop,bus.capacity-bus.peopleOnBus+alight)
   
    busstop.peopleInStop+=(int(30*RandomGenerator.Rand())-boarding)
    total.append(alight+boarding)

    bus.peopleOnBus+=(boarding-alight)

class intersection():
    def __init__(self,id):
        self.id=id
        self.distance=Distance[id]
        

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
    if tempid+1 in list(Distance.keys()):
        if tempid+1 in Busstoplist:
            scheduler.schedule( Event( bus,EventData( 'arrival' ,Component(tempid+1, 'busArrival',delay)) ) )
        else:
            scheduler.schedule( Event( bus,EventData( 'thru_intersection' ,Component(tempid+1, 'thru_intersection',delay )) ) )


Distance={0:50,1:500,2:170,3:150,4:150,5:480,6:40,7:10,8:420,\
          9:0,1000:200,1001:240,1002:90,1003:150,1004:240,\
          1005:110,1006:110,1007:130,1008:120,1009:60,1010:0}
#route 94
inter1=intersection(1)
inter2=intersection(2)
inter3=intersection(3)
stop4=BusStop(4,int(30*RandomGenerator.Rand()))
inter5=intersection(5)
inter6=intersection(6)
inter7=intersection(7)
stop8=BusStop(8,int(30*RandomGenerator.Rand()))
stop9=BusStop(9,int(30*RandomGenerator.Rand()))
#route 26
stop1001=BusStop(1001,int(30*RandomGenerator.Rand()))
inter1002=intersection(1002)
stop1003=BusStop(1003,int(30*RandomGenerator.Rand()))
inter1004=intersection(1004)
inter1005=intersection(1005)
stop1006=BusStop(1006,int(30*RandomGenerator.Rand()))
inter1007=intersection(1007)
inter1008=intersection(1008)
inter1009=intersection(1009)
stop1010=BusStop(1010,int(30*RandomGenerator.Rand()))
#common
Busstoplist=[4,8,9,1001,1003,1006,1010]
Object={inter1.id:inter1,inter2.id:inter2,inter3.id:inter3,\
        stop4.id:stop4,inter5.id:inter6,inter6.id:inter6,\
        inter7.id:inter7,stop8.id:stop8,stop9.id:stop9,\
        stop1001.id:stop1001,inter1002.id:inter1002,stop1003.id:stop1003,\
        inter1004.id:inter1004,inter1005.id:inter1005,stop1006.id:stop1006,\
        inter1007.id:inter1007,inter1008.id:inter1008,inter1009.id:inter1009,\
        stop1010.id:stop1010}

while T>0:
    scheduler = Scheduler()
    bus1 = Bus(94, 1569769200, 50, scheduler,1)
    bus2 = Bus(94, 1569769200+1800, 50, scheduler,2)
    bus3 = Bus(94, 1569769200+1800*2, 50, scheduler,3)
    bus4 = Bus(94, 1569769200+1800*3, 50, scheduler,4)
    bus5 = Bus(94, 1569769200+1800*4, 50, scheduler,5)
    bus6 = Bus(94, 1569769200+1800*5, 50, scheduler,6)
    bus7 = Bus(94, 1569769200+1800*6, 50, scheduler,7)
    bus8 = Bus(94, 1569769200+1800*7, 50, scheduler,8)
    bus101=Bus(26, 1569769800, 50, scheduler,1)
    bus102=Bus(26, 1569769800+1800, 50, scheduler,2)
    bus103=Bus(26, 1569769200+1800*2, 50, scheduler,3)
    bus104=Bus(26, 1569769200+1800*3, 50, scheduler,4)
    bus105=Bus(26, 1569769200+1800*4, 50, scheduler,5)
    bus106=Bus(26, 1569769200+1800*5, 50, scheduler,6)
    bus107=Bus(26, 1569769200+1800*6, 50, scheduler,7)
    bus108=Bus(26, 1569769200+1800*7, 50, scheduler,8)

    eventHandler = EventHandeler()
    bus1.busInitiate();bus2.busInitiate()
    bus3.busInitiate();bus4.busInitiate()
    bus5.busInitiate();bus6.busInitiate()
    bus7.busInitiate();bus8.busInitiate()
    bus101.busInitiate();bus102.busInitiate()
    bus103.busInitiate();bus104.busInitiate()
    bus105.busInitiate();bus106.busInitiate()
    bus107.busInitiate();bus108.busInitiate()

    scheduler.runSim( eventHandler, 1569783600)
#finalcount is the number of passengers that board and alight
    finalcount=int(sum(total)/2)
    #print('final count is '+str(finalcount))
    T-=1
average=int(finalcount/t)

print('average count is '+str(average))