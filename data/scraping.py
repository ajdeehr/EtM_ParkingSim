#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
#=======================================================================
#                        General Documentation


""" This progam is used to scrape class schedule of UWB in fall 2018.
    It filtered out everything our CSS458 group project doesn't need
    and keep the useful data for our final project.
    The data scrapped will be outputed as some csv files, so we can
    fairly check the data.
    
   See function docstring for description.
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
import numpy.random as r
import bs4 as bs
import requests
import csv
import re
import Constants as C    

def scraping(year):   
    link_list = []
    output = []
    
    # Get the UWB catalog website 
    page = requests.get('https://www.uwb.edu/registration/time/aut{}'.format(year))
    # Parse HTML
    soup = bs.BeautifulSoup(page.text, 'html.parser')
    
    # Find every line that has that part of URL
    for link in soup.find_all('a', attrs={'href': re.compile("^http://www.washington.edu/students/timeschd/B/")}):
        
        # Get the exact url without the #
        url = link.get('href')
        
        for i in range(len(url)):
            if url[i] == '#':
                url = url[:i]
                break;
    
        link_list.append(url)
    
    # find the div class with the specific name and 
    # print that last element of li
    # that is the quarter and year information
            
    quarter = soup.find(class_='w-Breadcrumbs')
    quarter = quarter.find_all('li')
    quarter = quarter[-1].text
    print(quarter)
    
    # start scraping data from the links we have            
    for weburl in link_list:
    
        page = requests.get(weburl)
        soup = bs.BeautifulSoup(page.text, 'html.parser')
        
        # See if the website is open correctly
        check_availability = soup.find('h1').text
        check_availability = " ".join(check_availability.split())
        
        # If error message occur, just skip
        if (check_availability == 'Time Schedule - No Courses Offered'):
            continue
            
        # get the correct format of names    
        # print the subject name    
        # print the subject rul
        subject = soup.find('h2')
        subject = subject.text
        sub_start = subject.index('(')
        subject = subject[:sub_start]
        print(subject)
        print(weburl)
        
        # Every class information is store as one line
        # Thus we just grap that line
        # crop the string size to fit the data into
        # different array cell.
        class_list = soup.find_all('pre')
        class_list = class_list[1:]        
        
        for class_name in class_list:
            class_name = class_name.text[8:100]
            
            sln = class_name[:5]
            sln = int(sln)
            period = class_name[17:35]
            period = " ".join(period.split())
            instructor = class_name[49:76]
            instructor = " ".join(instructor.split())
            enrolled = class_name[85:87]
            enrolled = int(enrolled)
        
            output.append(sln)
            output.append(period)
            output.append(instructor)
            output.append(enrolled)
    
    output = np.asarray(output).reshape((-1,4)) 
    
    schedule = []
       
    # read the array
    for line in output:
        schedule.append(line[1])
        schedule.append(line[-1])
                
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
            
        if (final_schedule[i,1][-2:] == '05' or final_schedule[i,1][-2:] == '10'):
            if r.randint(2) == 0:
                final_schedule[i,1] = final_schedule[i,1][0:-2] + '00'
            else:
                final_schedule[i,1] = final_schedule[i,1][0:-2] + '15'

        if (final_schedule[i,1][-2:] == '20' or final_schedule[i,1][-2:] == '25'):
            if r.randint(2) == 0:
                final_schedule[i,1] = final_schedule[i,1][0:-2] + '15'
            else:
                final_schedule[i,1] = final_schedule[i,1][0:-2] + '30'                
    
        if (final_schedule[i,1][-2:] == '35' or final_schedule[i,1][-2:] == '40'):
            if r.randint(2) == 0:
                final_schedule[i,1] = final_schedule[i,1][0:-2] + '30'
            else:
                final_schedule[i,1] = final_schedule[i,1][0:-2] + '45'
                
        if (final_schedule[i,1][-2:] == '50' or final_schedule[i,1][-2:] == '55'):
            if r.randint(2) == 0:
                final_schedule[i,1] = final_schedule[i,1][0:-2] + '45'
            else:
                final_schedule[i,1] = final_schedule[i,1][0:-2] + '00'
                temp_str = int(final_schedule[i,1]) + 100
                final_schedule[i,1] = str(int(temp_str))
            
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
    
    # Can change the beginning value to remove all uncessary
    # zeros in the 2D array
    BEGINNING = 0
    
    on_campus = np.zeros((96,5))
    
    
    # a function that will be called when needing
    # to add student to a time slot
    def save2arr(day,in_time,out_time,destination,value):
        start = int(in_time) 
        end = int(out_time)
        time1 = int((start - BEGINNING)/STEPS)
        time2 = int((end - BEGINNING)/STEPS)
    
        time = range(time1,time2)
        for i in time:
            destination[i][day] += int(value)
    
    
    # Selete day and time, and add the studnet into the
    # corrosponding 2D array cell
    #M = [0], T = [1], W = [2], TH = [3], F = [4]
    
    for row in final_schedule:
    
        for day in range(len(row[0])):
            
            if row[0][day] == 'M':
                save2arr(0,row[1],row[2],on_campus,row[-1])
                
            elif row[0][day] == 'T':
                if day < len(row[0])-1 and row[0][day+1] == 'h':
                    save2arr(3,row[1],row[2],on_campus,row[-1])
                else:
                    save2arr(1,row[1],row[2],on_campus,row[-1])
            
            elif row[0][day] == 'W':
                save2arr(2,row[1],row[2],on_campus,row[-1])
    
            elif row[0][day] == 'F':
                save2arr(4,row[1],row[2],on_campus,row[-1])
            else:
                continue
                
    on_campus = (on_campus*(C.DRIVE_ALONE_AVG + C.CARPOOL_AVG) * 774/2020 * (r.normal(0,0.5))).astype(int)
 
    # Output the 2D array as a CSV file
    with open("on_campus.csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(on_campus)

    return on_campus

