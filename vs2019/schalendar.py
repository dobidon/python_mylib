# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 17:56:52 2019

@author: omemi
"""
import time
import datetime
from typing import NamedTuple

def Is_Holiday(date=None):
    from workalendar.europe import Turkey

    ans = False

    if date == None:
        date = datetime.datetime.today()
    cal = Turkey()
    
    ans = True if date.weekday() == 6 else False

    ans_list = [True for i in cal.holidays(date.year) if i[0] == date.date()]
    ans = True if len(ans_list) or ans else False
    
    return ans

def Is_Time_Between(start='00.00', end='23.59'):
    res = False
    dt = datetime.datetime.now()
    dt_opening = datetime.datetime.strptime(start,            \
                 '%H.%M').replace(year=dt.year, month=dt.month,\
                 day=dt.day)
    dt_closing = datetime.datetime.strptime(end, \
                 '%H.%M').replace(year=dt.year, month=dt.month,\
                 day=dt.day)
    dt_dif_op = dt - dt_opening
    dt_dif_cl = dt_closing - dt
#    Debug_Call('Difference from opening: '+ str(dt_dif_op))
#    Debug_Call('Difference from closing: '+ str(dt_dif_cl))
    
    # If the time is in DUTY hours
    #
    if ((dt_dif_op.days >= 0) and (dt_dif_cl.days >= 0)):
        res = True
    return res

class Schedular:
    time_list: list
    idex: int
    interval: int
    
    def __init__(self, time_list, interval):
        self.time_list = time_list
        self.interval = interval
        self.idex = None
        return
    
    def schedule(self):
        time_list = self.time_list
        idex = self.idex
        interval = self.interval
        
        if (int(interval) <= 0):
            interval = 1
        dt = datetime.datetime.now()
        tm_schedule = None
        
        # If first call to the method
        #
        if (idex != None):
            if (idex == 0):
                dt += datetime.timedelta(days=1)
            dt_shift = datetime.datetime.strptime(time_list[idex], '%H.%M').replace( \
                       year=dt.year, month=dt.month, day=dt.day)
            dt_str = str(dt_shift.year) + '-' + str(dt_shift.month) + '-' +   \
                     str(dt_shift.day) + ' ' + time_list[idex]
            tm_schedule = time.mktime(time.strptime(dt_str,'%Y-%m-%d %H.%M'))
        
        else:
            idex = 0
            dt_save = dt + datetime.timedelta(minutes=interval)
            dt_str_hour = str(dt_save.hour) + '.' + str(dt_save.minute)
            
            for i in time_list:
                idex = time_list.index(i)
                dt_shift = datetime.datetime.strptime(i, '%H.%M').replace(    \
                                    year=dt.year, month=dt.month, day=dt.day)
                dt_dif = dt_shift - dt
                dt_dif_abs = abs(dt_shift - dt)
                if (dt_dif_abs.seconds < interval * 60):
                    dt_str_hour =  str(dt_shift.hour) + '.' + str(dt_shift.minute)
                    break
                elif (dt_dif.days >= 0):
                    dt_str_hour = i
                    break
                elif (time_list.index(i) >= (len(time_list) - 1)):
                    idex = 0
                    ii = time_list[0]
                    dt_shift = datetime.datetime.strptime(ii, '%H.%M').replace(       \
                                year=dt.year, month=dt.month, day=dt.day)
                    dt_shift += datetime.timedelta(days=1)
                    dt_str_hour = ii
            
            dt_str = str(dt_shift.year) + '-' + str(dt_shift.month) + '-' +   \
                     str(dt_shift.day) + ' ' + dt_str_hour
            tm_schedule = time.mktime(time.strptime(dt_str,'%Y-%m-%d %H.%M'))
        
        self.idex = ((idex + 1) % len(time_list))
        return tm_schedule


#################

def Schedule_Create(time_list, idex=None, interval=3):
    if (int(interval) <= 0):
        interval = 1
    dt = datetime.datetime.now()
    tm_schedule = None
    if (idex != None):
        if (idex == 0):
            dt += datetime.timedelta(days=1)
        dt_shift = datetime.datetime.strptime(time_list[idex], '%H.%M').replace( \
                   year=dt.year, month=dt.month, day=dt.day)
        dt_str = str(dt_shift.year) + '-' + str(dt_shift.month) + '-' +   \
                 str(dt_shift.day) + ' ' + time_list[idex]
        tm_schedule = time.mktime(time.strptime(dt_str,'%Y-%m-%d %H.%M'))
        return tm_schedule, ((idex + 1) % len(time_list))
    
    idex = 0
    dt_save = dt + datetime.timedelta(minutes=interval)
    dt_str_hour = str(dt_save.hour) + '.' + str(dt_save.minute)
    
    for i in time_list:
        idex = time_list.index(i)
        dt_shift = datetime.datetime.strptime(i, '%H.%M').replace(    \
                            year=dt.year, month=dt.month, day=dt.day)
        dt_dif = dt_shift - dt
        dt_dif_abs = abs (dt_shift - dt)
        if (dt_dif_abs.seconds < interval * 60):
            dt_str_hour =  str(dt_shift.hour) + '.' + str(dt_shift.minute)
            break
        elif (dt_dif.days >= 0):
            dt_str_hour = i
            break
        elif (time_list.index(i) >= (len(time_list) - 1)):
            ii = time_list[0]
            dt_shift = datetime.datetime.strptime(ii, '%H.%M').replace(       \
                        year=dt.year, month=dt.month, day=dt.day)
            dt_shift += datetime.timedelta(days=1)
            dt_str_hour = ii
    
    dt_str = str(dt_shift.year) + '-' + str(dt_shift.month) + '-' +   \
             str(dt_shift.day) + ' ' + dt_str_hour
    tm_schedule = time.mktime(time.strptime(dt_str,'%Y-%m-%d %H.%M'))
    
    return tm_schedule, ((idex + 1) % len(time_list))
