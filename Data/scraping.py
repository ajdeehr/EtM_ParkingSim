#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
#=======================================================================
#                        General Documentation


""" This progam is used to scrape class schedule of UWB in fall 2018.
    It filtered out everything our CSS458 group project doesn't need
    and keep the useful data for our final project.
    The data scrapped will be outputed as a  sinlge csv file, so we can
    fairly easy to read all the data
    
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
import bs4 as bs
import requests
import csv
import re

link_list = []
output = []

page = requests.get('https://www.uwb.edu/registration/time/aut2018')
soup = bs.BeautifulSoup(page.text, 'html.parser')
 
for link in soup.find_all('a', attrs={'href': re.compile("^http://www.washington.edu/students/timeschd/B/AUT2018/")}):
    
    url = link.get('href')
    
    for i in range(len(url)):
        if url[i] == '#':
            url = url[:i]
            break;

    link_list.append(url)
    
for weburl in link_list:

    page2 = requests.get(weburl)
    soup2 = bs.BeautifulSoup(page2.text, 'html.parser')
    
    #    quarter = soup2.find(class_='forceclear')
    #    quarter = quarter.text
    #    print(quarter,"\n")
    
    check_availability = soup2.find('h1').text
    check_availability = " ".join(check_availability.split())
    
    if (check_availability == 'Time Schedule - No Courses Offered'):
        continue
    
    subject = soup2.find('h2')
    subject = subject.text
    sub_start = subject.index('(')
    subject = subject[:sub_start]
    print(subject)
    print(weburl)

    
    class_list = soup2.find_all('pre')
    class_list = class_list[1:]
    
    artist_name_list = class_list
    artist_name_list_items = artist_name_list
    
    
    for artist_name in artist_name_list_items:
        artist_name = artist_name.text
        artist_name = artist_name[8:100]
        
        sln = artist_name[:5]
        sln = int(sln)
        period = artist_name[17:35]
        period = " ".join(period.split())
        instructor = artist_name[49:76]
        instructor = " ".join(instructor.split())
        enrolled = artist_name[85:87]
        enrolled = int(enrolled)
    
        output.append(sln)
        output.append(period)
        output.append(instructor)
        output.append(enrolled)

output = np.asarray(output).reshape((-1,4)) 

with open("new_file.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(output)
    
#print(output)

