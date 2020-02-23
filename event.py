import queue

class Event(object):
    def __init__( self, bus, eventData ):
        self.timestamp = bus.timestamp
        self.route = bus.route
        self.eventType = eventData.eventType
        self.componentType = eventData.component.componentType
        self.id = eventData.component.id
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


class EventData(object):
    def __init__(self, eventType, Component):
        self.eventType = eventType
        self.component = Component

class Component(object):
    def __init__(self, id, componentType, processingTime, numAtQ ):
        self.id = id
        self.componentType = componentType
        self.processingTime = processingTime
        self.numAtQ = numAtQ

class Scheduler():
    def __init__(self):
        self.time = 0
        self.FEL = queue.PriorityQueue()

    def schedule(self, event ):
        # self.FEL.put( Event( bus, eventData ) )
        self.FEL.put(  event )

    def runSim(self, eventHandler, bus, endTime):
        while not self.FEL.empty():

            # print(self.FEL.queue)
            nextEvent = self.FEL.get()

            now = nextEvent.timestamp
            if now > endTime:
                break

            eventHandler.handle( nextEvent, bus )
            # print( nextEvent )
            print( 'current timestamp is %s ' % (nextEvent.timestamp) )
            print('current route is %s ' % (nextEvent.route))
            print('current eventType is %s ' % (nextEvent.eventType))
            print('current componentType is %s ' % (nextEvent.componentType))
            print( )

            # self.time = nextEvent.timestamp

class EventHandeler(object):
    def __init__(self):
        pass

    def handle(self, event, bus):
        if event.eventType == 'generate':
            bus.busGenerate()

        elif event.eventType == 'arrival':
            bus.busArrival()

        else:
            bus.busDepature()



class Bus(object):
    def __init__(self, route, timestamp, stop, capacity, scheduler):
        self.route = route
        self.timestamp = timestamp

        self.numAtStop = stop.busAtQ
        self.numOnRoad = 0
        self.capacity = capacity
        self.peopleOnBus = 0
        self.scheduler = scheduler

    def busGenerate(self):
        self.numOnRoad += 1


        self.timestamp += 10

        stop = Stop(12)
        self.scheduler.schedule( Event( Bus( self.route, self.timestamp, stop, self.capacity, self.scheduler  ), EventData( 'generate' ,Component(34, 'Generator', 10, 0)) ) )

        # print('number of the bus on the road: %i' % (self.numOnRoad) )

    def busArrival(self):
        self.numAtStop += 1

    def busDeparture(self):
        self.numAtStop -= 1


class Stop(object):
    def __init__(self, stopId):
        self.id = stopId
        self.peopleInStop = 0
        self.busAtQ = 0



if __name__ == '__main__':

    stopImpl = Stop(455)

    scheduler = Scheduler()


    bus = Bus(23, 2355, stopImpl, 50, scheduler)
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
    scheduler.runSim( eventHandler, bus, 2485 )



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

