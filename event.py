#Queue is in python2,queue in python3
import queue
import random
    # event = Event(bus, eventData)
class Event(object):
    def __init__( self, bus, eventData ):
        self.bus=bus
        self.timestamp = bus.timestamp
        self.route = bus.route
        self.eventType = eventData.eventType
        self.componentType = eventData.component.componentType
        self.componentid = eventData.component.comid
        self.numAtQ = eventData.component.numAtQ
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
    def __init__(self, comid, componentType, processingTime, numAtQ ):
        self.comid = comid
        self.componentType = componentType
        self.processingTime = processingTime
        self.numAtQ = numAtQ

class Scheduler():
    def __init__(self):
        self.time = 0
        self.FEL = queue.PriorityQueue()

    def schedule(self, event ):
        # self.FEL.put( Event( bus, eventData ) )
        self.FEL.put( event )
# change the bus off the input, taken from nextevent
    def runSim(self, eventHandler, endTime):
        while not self.FEL.empty():

            # print(self.FEL.queue)
            nextEvent = self.FEL.get()
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
            busArrival(event.bus,event.componentid)

        else:
            thru_intersection(event.bus,event.componentid)



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
        while self.numOnRoad<20:
            self.numOnRoad += 1
#NEED: interval is a RV
        self.timestamp += 10
#temporary setting,bus erased
        #stop = BusStop(12,10)

        #component __init__(self, comid, componentType, processingTime, numAtQ ):
#NEED: need to change the component comid 34 here
        self.scheduler.schedule( Event( self, EventData( 'generate' ,Component(34, 'Generator', 10, 0)) ) )
        # print('number of the bus on the road: %i' % (self.numOnRoad) )


#NEED: set up bus stop, where the people count should increase over time, and could drop because of buses
class BusStop(object):
    def __init__(self, stopId,peoplecount):
        self.stopid = stopId
        self.peopleInStop = peoplecount
        self.distance=Distance[stopId]

#The function for busstop scenario:
def busArrival(bus,busstop):
    if busstop.id in nearbystation:
        bus.peopleOnBus=bus.capacity
    distance=busstop.distance
    #delay in the busstop is proportional to the distance,velocity is assumed 20 here
    delay=round(distance/20,2)
    #34 is an id, provoke another schedule arrangement
    if busstop.id+1 in Busstoplist:
        scheduler.schedule( Event( Bus(bus.route,bus.timestamp+delay,bus.capacity, bus.scheduler,bus.numOnRoad)), \
        EventData( 'arrival' ,Component(id+1, 'busArrival',delay , 0)) ) 
    else:
        scheduler.schedule( Event( Bus(bus.route,bus.timestamp+delay,bus.capacity, bus.scheduler,bus.numOnRoad)), \
        EventData( 'thru_intersection' ,Component(id+1, 'thru_intersection',delay , 0)) ) 

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
    #delay1 is proportional to the distance,velocity is assumed 20 here
    delay1=round(distance/20,2)
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
    delay=delay1+delay2+delay3
    if intersection.id+1 in Busstoplist:
        scheduler.schedule( Event( Bus(bus.route,bus.timestamp+delay,bus.capacity, bus.scheduler,bus.numOnRoad)), \
        EventData( 'arrival' ,Component(id+1, 'busArrival',delay , 0)) ) 
    else:
        scheduler.schedule( Event( Bus(bus.route,bus.timestamp+delay,bus.capacity, bus.scheduler,bus.numOnRoad)), \
        EventData( 'thru_intersection' ,Component(id+1, 'thru_intersection',delay , 0)) ) 

    
if __name__ == '__main__':
#set up all bus stops, note that we need to set more people in stops that are closer to the stadium 
#NEED: define stops and intersections with id list
    numOnRoad=0
    stopImpl = BusStop(455,10)
#NEED: a list of ids that indicate bus stops, not intersections
    Busstoplist=[]
#NEED: Object list of stops and intersections, id is key
    Objects={}
#NEED: need the dict of distance after each busstop/intersection, stopid is key
    Distance={}
#NEED: nearby station means that stops close to stadium, always a lot of people
    nearbystation=[]
    scheduler = Scheduler()

    bus = Bus(23, 2355, 50, scheduler,0)
    # bus.busGenerate()
    # bus.busGenerate()

    comp = Component(34, 'station', 12, 0)
    eventData = EventData('generate', comp)
    event = Event(bus, eventData)

    scheduler.schedule(event)

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


