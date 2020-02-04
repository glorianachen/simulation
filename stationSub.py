import random
import time
from datetime import datetime


# # string time -> timestamp
# def strTimeProp(start, end, prop, frmt):
#     # time.strptime: string time -> struct time
#     # time.mktime: struct_time -> timestamp
#     stime = time.mktime(time.strptime(start, frmt))
#     etime = time.mktime(time.strptime(end, frmt))
#
#     print("etime - stime: ", etime - stime)
#     # probability from 0 ~ 1
#     ptime = stime + prop * (etime - stime)
#
#     print( "strptime: ", time.strptime(start, frmt))
#     print( "mktime: ", time.mktime(time.strptime(start, frmt)))
#     print("prop: ", prop)
#     print("strTimeProp: ", ptime)
#
#     return int(ptime)
#
# # randomTimestamp: string time -> timestamp
# def randomTimestamp(start, end, frmt='%Y-%m-%d %H:%M:%S'):
#     #return the timestamp of the randomly time from start ~ end
#     return strTimeProp(start, end, random.random(), frmt)
#
# # randomDate: timestamp -> string time
# def randomDate(start, end, frmt='%Y-%m-%d %H:%M:%S'):
#     # time.localtime: timestamp -> time_struct
#     # time.strftime: time_struct -> string time
#     return time.strftime(frmt, time.localtime(randomTimestamp(start, end)))




"""
    stringtime -> timestamp
    scheduleTime: according to the schedule time for the bus
    beforeScheduleTime: we assume the time interval is 5 min, 300 sec
    prob: probability 
    frmt: format
"""
def strTimeProb( scheduleTime, beforeScheduleTime, prob, frmt ):
    stime = time.mktime( time.strptime( scheduleTime, frmt ) )
    curTime = stime + prob * beforeScheduleTime
    return int(curTime)

"""
    pass the random function to the strTimeProb()
"""
def randTimestamp( scheduleTime, beforeScheduleTime, frmt = '%Y-%m-%d %H:%M:%S' ):
    return strTimeProb(scheduleTime, beforeScheduleTime, random.random(), frmt)

"""
    timestamp -> time string 
"""
def randDate( scheduleTime, beforeScheduleTime, frmt = '%Y-%m-%d %H:%M:%S' ):
    return time.strftime(frmt, time.localtime(randTimestamp(scheduleTime, beforeScheduleTime)))



"""
    each time will call the arrival for next passenger
"""
def passengerArrival( scheduleTime, beforeScheduleTime, endTime, cnt ):
    nextArrival = randDate(scheduleTime, beforeScheduleTime)

    if nextArrival < endTime:
        cnt += 1
        print("next passenger arrive at: ", nextArrival)
        print("total passener: ", cnt)
        passengerArrival( nextArrival, beforeScheduleTime, endTime, cnt )

    # print("cnt: ", cnt)
    # return cnt




"""
    To calculate the timestamp of curtime = curTime + interval
"""
def intervalTimestamp(timestring, interval, frmt = '%Y-%m-%d %H:%M:%S' ):
    stime = time.mktime(time.strptime(timestring, frmt))
    curTime = stime + interval
    intCurTime = int(curTime)
    return time.strftime(frmt, time.localtime( intCurTime ))



def busGenerator( ArrivalTime, endtime, interval, capacity, peopleOnBus, peopleOnStation ):
    initPeople = random.randint(0, capacity)
    numAlight = random.randint(0, initPeople)
    numAfterAlight = initPeople - numAlight

    numBoard = capacity - numAfterAlight if peopleOnStation > capacity - numAfterAlight else peopleOnStation
    # if peopleOnStation > capacity - numAfterAlight:
    #     numBoard = capacity - numAfterAlight
    #
    # else:
    #     numboard = peopleOnStation

    peopleOnBus = numAfterAlight + numBoard



    print("bus arrive at: ", ArrivalTime)
    print("initPeople on bus: ", initPeople)
    print("people alight: ", numAlight)
    print("people num after alight: ", numAfterAlight)

    print("num Board: ", numBoard)
    print("people on bus: ", peopleOnBus)

    nextTime = intervalTimestamp(ArrivalTime, interval )
    if nextTime < endtime:
        # print("bus arrive at: ", nextTime)
        busGenerator( nextTime, endtime, interval, capacity, peopleOnBus, peopleOnStation )



# def stationHandeler():


passengerCnt = 0
start = '2020-02-01 12:12:12'
end = '2020-02-01 22:30:12'
busArrive = '2020-02-01 07:12:12'
passengerArrival( start, 300, end, passengerCnt)
busGenerator( busArrive, end, 600, 30, 0, 15 )