import sys
import datetime
import time
#read txt and time into list
def loadDatadet(f):
    sourceInLine=f.readlines()
    dataset=[]
    for line in sourceInLine:
        line=line.rstrip("\n")
        dataset.append(line)
    #bustime.txt=['5:25', '5:55', '6:25', '6:55', '7:25', '7:55', '8:25', '8:55', '9:25', '9:55', '10:25', '10:55', '11:25', '11:55', '12:25', '12:55', '13:25', '13:55', '14:25', '14:55', '15:25', '15:55', '16:25', '16:55', '17:25', '17:55', '18:25', '18:55', '19:25', '19:55', '20:25', '20:55', '21:25', '21:55', '22:25', '22:55', '23:25', '23:55','0:25']
    return dataset
    print(dataset)

f=open(r'./Desktop/bustime.txt')
infile=loadDatadet(f)
a=iter(infile)
t=0

def bus_time():
    global t
    #football season from 20190905
    if t==0:
        aa='2019-09-05'+' '+infile[0]
        endTime=(datetime.datetime.strptime(aa, "%Y-%m-%d %H:%M") + datetime.timedelta(0)).strftime("%Y-%m-%d %H:%M")
        finalTime=datetime.datetime.strptime(endTime,"%Y-%m-%d %H:%M")
        busTime=finalTime.strftime("%Y-%m-%d %H:%M")
        #TimeStamp
        stamp = finalTime.timetuple()
        timeStamp = int(time.mktime(stamp))
        print('busTime: ',busTime,'busTimeStamp: ',timeStamp)
        t+=1
    if t%38==0:
        aa='2019-09-05'+' '+infile[-1]
        endTime=(datetime.datetime.strptime(aa, "%Y-%m-%d %H:%M") + datetime.timedelta(days=t//38)).strftime("%Y-%m-%d %H:%M")
        finalTime=datetime.datetime.strptime(endTime,"%Y-%m-%d %H:%M")
        busTime=finalTime.strftime("%Y-%m-%d %H:%M")
        #TimeStamp
        stamp = finalTime.timetuple()
        timeStamp = int(time.mktime(stamp))
        print('busTime: ',busTime,'busTimeStamp: ',timeStamp)
        t+=1
    else:
        aa='2019-09-05'+' '+infile[t%39]
        endTime=(datetime.datetime.strptime(aa, "%Y-%m-%d %H:%M") + datetime.timedelta(days=t//38)).strftime("%Y-%m-%d %H:%M")
        finalTime=datetime.datetime.strptime(endTime,"%Y-%m-%d %H:%M")
        busTime=finalTime.strftime("%Y-%m-%d %H:%M")
        #TimeStamp
        stamp = finalTime.timetuple()
        timeStamp = int(time.mktime(stamp))
        print('busTime: ',busTime,'busTimeStamp: ',timeStamp)
        t+=1


