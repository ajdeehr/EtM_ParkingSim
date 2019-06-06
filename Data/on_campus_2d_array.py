#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
#=======================================================================
#                        General Documentation


""" This progam is used to scrape class schedule of UWB in fall 2018.
   It read the CSV data file create by the scraping program, and print
   another CSV files and return some a 2D array of number of students
   in class each 15 minutes
   
   This program has been merged to the scraping, NOT IN USE ANYMORE
    """

#-----------------------------------------------------------------------
#                       Additional Documentation
#
#
# Modification History:
# - 30 May 2019:  Original by Xavier, UW Bothell.
#    Passed passably reasonable tests.
#
# Notes:
# - Written for Python 3.x.
# - Module docstrings can be tested using the doctest module.  To
#   test, execute "python computational_error.py".
# - See import statements throughout for more information on non-
#   built-in packages and modules required.
#
# Copyright (c) 2019 by Xavier Cheng.
#=======================================================================

#========================== Imported module ==========================

import numpy as np
import numpy.ma as ma
import csv
import numpy.random as r

def on_campus_arr(filename):
    schedule = []
    
    # read the CSV file
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for line in csv_reader:
            schedule.append(line[1])    # day and time
            schedule.append(line[-1])   # the number of student enrolled
            
        schedule = np.asarray(schedule)
        schedule = schedule.reshape((-1,2))
        
        # mask any item without meating day and time
        masked = ma.masked_where(schedule == 'to be arranged',  schedule)
        masked = ma.masked_where(masked == '0', masked)
        
        unmasked= []
        index = 0
        
        #generate a list with every non masked data
        for item in masked:
            if ma.is_masked(item) == False:
                unmasked.append(schedule[index])
            index += 1
                
        unmasked = np.asarray(unmasked)
        
        final_schedule = np.empty((unmasked.shape[0],4),dtype = 'U14')
        
        # Split the day and time into different array element
        for i in range(len(unmasked)):
            
            final_schedule[i,3] = unmasked[i,1]
            
            day_time = unmasked[i,0].split(' ')
            unmasked[i,0] = day_time[0]
            unmasked[i,1] = day_time[1]   
            final_schedule[i,0] = unmasked[i,0]
    
            hour =  unmasked[i,1].split('-')
            unmasked[i,0] = hour[0]
            unmasked[i,1] = hour[1]
            
            final_schedule[i,1] = unmasked[i,0]
            final_schedule[i,2] = unmasked[i,1]
            
            # modify the time information to a consistent menthod
            # that can be read and calculated
            if final_schedule[i,2][-1] == 'P':
                final_schedule[i,1] = int(final_schedule[i,1]) + 1200
                final_schedule[i,2] = int(final_schedule[i,2][0:-1]) + 1200
            
            if int(final_schedule[i,1]) > int(final_schedule[i,2]):
                final_schedule[i,2] = int(final_schedule[i,2]) + 1200
                
            if int(final_schedule[i,2]) < 800:
                final_schedule[i,1] = int(final_schedule[i,1]) + 1200
                final_schedule[i,2] = int(final_schedule[i,2]) + 1200
                
            if int(final_schedule[i,1]) < 800 and int(final_schedule[i,2]):
                final_schedule[i,1] = int(final_schedule[i,1]) + 1200
                final_schedule[i,2] = int(final_schedule[i,2]) + 1200
                
            if (final_schedule[i,2][-2:] == '05' or final_schedule[i,2][-2:] == '10'):
                if r.randint(2) == 0:
                    final_schedule[i,2] = final_schedule[i,2][0:-2] + '00'
                else:
                    final_schedule[i,2] = final_schedule[i,2][0:-2] + '15'
    
            if (final_schedule[i,2][-2:] == '20' or final_schedule[i,2][-2:] == '25'):
                if r.randint(2) == 0:
                    final_schedule[i,2] = final_schedule[i,2][0:-2] + '15'
                else:
                    final_schedule[i,2] = final_schedule[i,2][0:-2] + '30'
                
            if (final_schedule[i,2][-2:] == '35' or final_schedule[i,2][-2:] == '40'):
                if r.randint(2) == 0:
                    final_schedule[i,2] = final_schedule[i,2][0:-2] + '30'
                else:
                    final_schedule[i,2] = final_schedule[i,2][0:-2] + '45'
                    
            if (final_schedule[i,2][-2:] == '50' or final_schedule[i,2][-2:] == '55'):
                if r.randint(2) == 0:
                    final_schedule[i,2] = final_schedule[i,2][0:-2] + '45'
                else:
                    final_schedule[i,2] = final_schedule[i,2][0:-2] + '00'
                    temp_str = int(final_schedule[i,2]) + 100
                    final_schedule[i,2] = str(int(temp_str))
                
            if (final_schedule[i,1][-2:] != '00'):
                convert_to_quarter = int(final_schedule[i,1][-2:]) * 100 / 60
                convert_to_quarter = str(int(convert_to_quarter))
                
                time_str = final_schedule[i,1][0:-2]
                time_str += convert_to_quarter
                final_schedule[i,1] = time_str
    
            if (final_schedule[i,2][-2:] != '00'):
                convert_to_quarter = int(final_schedule[i,2][-2:]) * 100 / 60
                convert_to_quarter = str(int(convert_to_quarter))
                
                time_str = final_schedule[i,2][0:-2]
                time_str += convert_to_quarter
                final_schedule[i,2] = time_str
    
    #- from 0 - 24 = 24hrs = 2400
    #- 25 mins a timestep 
    #- 2400 / 25 = 96 steps 
    
    #- 800 - 8:00, 825 = 8:15, 850 = 8:30, 875 = 8:45
    #- 1600 - 4:00, 1625 = 4:15, 1650 = 4:30, 1675 = 4:45
    STEPS = 25
    BEGINNING = 0
    # Can change the beginning value to remove all uncessary
    # zeros in the 2D array
    
    on_campus = np.zeros((96,5))

    # a function that will be called when needing
    # to add student to a time slot
    def save2arr(day,in_time,out_time,destination,value):
        start = int(in_time) 
        end = int(out_time)
        time1 = int((start - BEGINNING)/STEPS)
        time2 = int((end - BEGINNING)/STEPS)
    
    #    print(start,end,time1,time2)
        time = range(time1,time2)
    #    print(time1,time2)
        for i in time:
            destination[i][day] += int(value)


    # Selete day and time, and add the studnet into the
    # corrosponding 2D array cell

    #M = [0], T = [1], W = [2], TH = [3], F = [4]
    for row in final_schedule:
    
        for day in range(len(row[0])):
            
            if row[0][day] == 'M':
                save2arr(0,row[1],row[2],on_campus,row[-1])
    #            print('M')
                
            elif row[0][day] == 'T':
                if day < len(row[0])-1 and row[0][day+1] == 'h':
#                    if row[0][day+1] == 'h':
                    save2arr(3,row[1],row[2],on_campus,row[-1])
                else:
                    save2arr(1,row[1],row[2],on_campus,row[-1])
            
            elif row[0][day] == 'W':
                save2arr(2,row[1],row[2],on_campus,row[-1])
    
            elif row[0][day] == 'F':
                save2arr(4,row[1],row[2],on_campus,row[-1])
    
            else:
                continue
                
    on_campus = on_campus.astype(int)           
                    
    '''    
        with open("2DonCampus.csv","w+") as my_csv:
            csvWriter = csv.writer(my_csv,delimiter=',')
            csvWriter.writerows(on_campus)

        with open("fileReadableSchedule.csv","w+") as my_csv:
            csvWriter = csv.writer(my_csv,delimiter=',')
            csvWriter.writerows(final_schedule)
    '''
    return on_campus
