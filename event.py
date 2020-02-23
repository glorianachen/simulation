#Queue is in python2,queue in python3
import heapq
import random
    # event = Event(bus, eventData)
class Event(object):
    def __init__( self, bus, eventData ):
        self.bus=bus
        self.timestamp = bus.timestamp
        self.route = bus.route
        self.eventType = eventData.eventType
        self.componentType = eventData.component.componentType
        self.id = eventData.component.id
        # self.next = next
        return

    def printSelf(self):
        print( 'its timestamp is %s ' % (self.timestamp) )
        print( 'its eventType is %s ' % (self.eventType))
        print( 'its componentType is %s ' % (self.componentType) )
        # print('its next is %s ' % (self.next))
    
#compare with others??
    def __lt__(self, other):
        return self.timestamp < other.timestamp
    def __eq__(self, other):
        return self.timestamp == other.timestamp

# eventData = EventData('arrival', comp)
class EventData(object):
    def __init__(self, eventType, Component):
        self.eventType = eventType
        self.component = Component
    
# usage: comp = Component(34, 'station', 12, 0)
# ???
class Component(object):
    def __init__(self, comid, componentType, processingTime):
        self.id = comid
        self.componentType = componentType
        self.processingTime = processingTime

class Scheduler():
    def __init__(self):
        self.time = 0
        self.FEL = []

    def schedule(self, event ):
        # self.FEL.put( Event( bus, eventData ) )
        heappush(self.FEL,(event.timestamp,event))
# change the bus off the input, taken from nextevent
    def runSim(self, eventHandler, endTime):
        while len(self.FEL)>0:

            # print(self.FEL.queue)
            nextEvent = heapq.heappop(self.FEL)[1]
            now = nextEvent.timestamp
            if now > endTime:
                break

            eventHandler.handle( nextEvent )
            # print( nextEvent )
            print( 'current timestamp is %s ' % (nextEvent.timestamp) )
            print('current route is %s ' % (nextEvent.route))
            print('current eventType is %s ' % (nextEvent.eventType))
            print('current componentType is %s ' % (nextEvent.componentType))
            print( )

            # self.time = nextEvent.timestamp
#?????
class EventHandeler(object):
    def __init__(self):
        pass

    def handle(self, event):
        if event.eventType == 'generate':
            event.bus.busGenerate()

        elif event.eventType == 'arrival':
            busArrival(event.bus,Object[event.id])

        else:
            thru_intersection(event.bus,Object[event.id])



#usage: bus = Bus(23, 1255, 50, scheduler)
class Bus(object):
    def __init__(self, route, timestamp, capacity, scheduler,numOnRoad):
        self.route = route
        self.timestamp = timestamp
    #numAtStop is the deleted
        #self.numAtStop = stop.busAtQ
        self.numOnRoad=numOnRoad
        self.capacity = capacity
        self.peopleOnBus = 0
        #busy time or station
        #data_poisson = poisson.rvs(mu=5, size=5)
        #peopleOnBus = sum(data_poisson)
        #normal time or station
        #data_poisson = poisson.rvs(mu=5, size=5)
        #peopleOnBus = sum(data_poisson)
        self.scheduler = scheduler
        
    def busGenerate(self):
#set a maximum for numOnRoad
        #if self.numOnRoad<2:
#NEED:here 10 means interval for second bus
            #self.scheduler.schedule( Event( Bus(self.route,self.timestamp+10,self.scheduler,self.numOnRoad+1), EventData( 'generate' ,Component(1, 'busGenerate', 10)) ) )
        delay=round(Distance[0]/600,2)
#NEED: interval is a RV
        self.timestamp += delay
#temporary setting,busstop erased
        #stop = BusStop(12,10)
        #component __init__(self, comid, componentType, processingTime, numAtQ ):
#NEED: need to change the component comid 34 here
        self.scheduler.schedule( Event( self, EventData( 'arrival' ,Component(1, 'busArrival', delay)) ) )
        # print('number of the bus on the road: %i' % (self.numOnRoad) )


#NEED: set up bus stop, where the people count should increase over time, and could drop because of buses
class BusStop(object):
    def __init__(self, stopId,peoplecount):
        self.id = stopId
        self.peopleInStop = peoplecount
        self.distance=Distance[stopId]

#The function for busstop scenario:
def busArrival(bus,busstop):
    tempid=busstop.id
    if tempid in nearbystation:
        bus.peopleOnBus=bus.capacity

    distance=busstop.distance
    #delay in the busstop is proportional to the distance,velocity is assumed 600 here
    delay=round(distance/600,2)
    #here 1 counts for the stopping time 
    bus.timestamp+=delay+1
    if tempid+1 in Busstoplist:
        scheduler.schedule( Event( bus, EventData( 'arrival' ,Component(tempid+1, 'busArrival',delay )) ) ）
    else:
        scheduler.schedule( Event( bus,EventData( 'thru_intersection' ,Component(tempid+1, 'thru_intersection',delay )) )） 

    #else:
        #diff=Bus.capacity-Bus.peopleOnBus
    #if diff >=0:
        #total_passenger_that_get_aboard=available empty space(if exist)+newspace from random number of people that leave
class intersection():
    def __init__(self,id):
        self.id=id
        self.distance=Distance[id]

def checklight(timestamp):
    #assume that since 0000, 30sec for green, 30 for red, for all traffic lights
    if timestamp%60<30:
        return (True,0)
    else:
        return (False,60-timestamp%60)
def thru_intersection(bus,intersection):
    distance=intersection.distance
    #delay1 is proportional to the distance,velocity is assumed 600 m/minhere
    delay1=round(distance/60,2)
    #delay2 is the time waiting for red light
    temptime=bus.timestamp+delay1
    check=checklight(temptime)
    if check[0]:
        delay2=0
    else:
        delay2=check[1]
    #delay3 is the time to accelerate and pass through the intersection, depends on how many cars in advance
    #If more time, change the random generator to the mod type from lecture notes
    delay3=3+2.87*random.randint(1,8)
    #delay1 in min, 2,3 in sec
    delay=delay1+round((delay2+delay3)/60,2)
    tempid=intersection.id
    bus.timestamp+=delay
    if tempid+1 in Busstoplist:
        scheduler.schedule( Event( bus,EventData( 'arrival' ,Component(tempid+1, 'busArrival',delay)) )） 
    else:
        scheduler.schedule( Event( bus,EventData( 'thru_intersection' ,Component(tempid+1, 'thru_intersection',delay )) )） 

    
if __name__ == '__main__':
#set up all bus stops, note that we need to set more people in stops that are closer to the stadium 
#NEED: define stops and intersections with id list
    numOnRoad=0
    stop1= BusStop(1,30)
    inter2=intersection(2)
    stop3=BusStop(1,30)
#NEED: a list of ids that indicate bus stops, not intersections
    Busstoplist=[1,3]
#NEED: Object list of stops and intersections, id is key
    Object={stop1.id:stop1,inter2.id:inter2,stop3.id:stop3}
#NEED: need the dict of distance after each busstop/intersection, stopid is key
    Distance={0:1000,1:1000,2:1000,3:1000}
#NEED: nearby station means that stops close to stadium, always a lot of people
    nearbystation=[1,3]
    scheduler = Scheduler()

    bus1 = Bus(23, 2355, 50, scheduler,1)
    # bus.busGenerate()
    # bus.busGenerate()

    #comp = Component(34, 'station', 12, 0)
    #eventData = EventData('generate', comp)
    #event = Event(bus, eventData)

    #scheduler.schedule(event)

    eventHandler = EventHandeler()
    # eventHandler.handle( event, bus )

    # scheduler = Scheduler()
    # scheduler.schedule(event)

    scheduler.runSim( eventHandler, 2485 )



    # bus = Bus(23, 1255, stopImpl, 50, scheduler)
    # bus.busGenerate()
    # bus.busGenerate()
    #
    # comp = Component(34, 'station', 12, 0)
    # eventData = EventData('arrival', comp)
    # event = Event(bus, eventData)
    #
    # # scheduler = Scheduler()
    # scheduler.schedule(event)
    # # scheduler.runSim()
    #
    #
    #
    # bus = Bus(24, 2155, stopImpl, 50, scheduler)
    # bus.busGenerate()
    # bus.busGenerate()
    #
    # comp = Component(34, 'station', 12, 0)
    # eventData = EventData('arrival', comp)
    # event = Event(bus, eventData)
    #
    #
    # # scheduler = Scheduler()
    # scheduler.schedule( event )
    # scheduler.runSim()

    # pq = queue.PriorityQueue()
    # pq.put((2, 'a'))
    # pq.put((1, 'b'))
    # print(pq.queue ) # output: [(1, 'b'), (2, 'a')]
    # print(pq.get())  # output: (1, 'b')
    # print(pq.queue)  # output: [(1, 'b'), (2, 'a')]
    # pq.queue  # output: [(2, 'a')]



    # bus = Bus(23)
    # bus.busGenerate()
    # bus.busGenerate()


    # event.printSelf()


