# -*- coding: utf-8 -*-
#==============================================================================
#                        General Documentation
"""
"""
#------------------------------------------------------------------------------
#                       Additional Documentation
# Modification History:
# - 23 May 2019:  Original by Dewey Nguyen, CSS458 A,
#   University of Washington Bothell.
# - Subsequent Revisions from Xavier Cheng, Ardalan Ahanchi,
#   and Adam Deehring
#
# Notes:
# - Written for Python 3.5.2.
#==============================================================================

#---------------- Module General Import and Declarations ----------------------
from pathlib import Path      #For platform independent path.

#Student data from PDF
FTE_2016 = 8217  # Full time student Fall 2016
FTE_2018 = 7731  # Full time student Fall 2018
FTE_AVG = int((FTE_2016 + FTE_2018)/2)

# Student who drives along
DRIVE_ALONE_16 = 0.579
DRIVE_ALONE_18 = 0.539
DRIVE_ALONE_AVG = (DRIVE_ALONE_16 + DRIVE_ALONE_18)/2

# Student who carpool
CARPOOL_16 = 0.136  #
CARPOOL_18 = 0.088
CARPOOL_AVG = (CARPOOL_16 + CARPOOL_18)/2

#Total number of student car
TOTAL_STUDENT_CAR = int(FTE_AVG * (DRIVE_ALONE_AVG + CARPOOL_AVG))

# Other personnel
STAFF_16 = 329
STAFF_18 = 371
STAFF_AVG = int((STAFF_16 + STAFF_18)/2)

FACULTY_16 = 360
FACULTY_18 = 357
FACULTY_AVG = int((FACULTY_16 + FACULTY_18) /2)

TOTAL_CAR = TOTAL_STUDENT_CAR + FACULTY_AVG + STAFF_AVG

# Variables For the Vehicle Class.
PERCENT_BIKE = 0.05  # The probablitiy of generating bike instead of a car.
PERCENT_HCAP = 0.05  # Probability of the Car to belong to a disabled person.
#PERCENT_CARPOOL = 0.05  # Probability of the Car having more than
						 # One passenger.
#(8217+7731)/2 = 7974, (0.136+0.088)/2 = 0.113
PERCENT_CARPOOL = 0.113  # Probability of the Car having more than
						 # One passenger.

VEHICLE_TYPE_CAR = 0  # Represent the types of the vehicle.
VEHICLE_TYPE_BIKE = 1
VEHICLE_TYPE_HCAP = 2
VEHICLE_TYPE_CARPOOL = 3

VEHICLE_TYPES = {"Car":0, "Bike":1, "HCap":2, "Carpool":3}

STATE_MOVING = 0  # Current state of the vehicle in the simulation.
STATE_PARKED = 1
STATE_LEFT = 2

ROAD_FLOW_MIN = 20          #Minimum number of vehicles who enter or leave
							# in a t.
ROAD_FLOW_MAX = 50          #Maximum number of vehicles who eenter or leave
							# in a t.
# Variables for the Agent class.
AGENT_STUDENT = 0
AGENT_FACULTY = 1
AGENT_STAFF = 2

MIN_NO_DAYS_SCHOOL = 2
MAX_NO_DAYS_SCHOOL = 5

# Constants for the model.
MIN_PASSENGERS = 2
MAX_PASSENGERS = 4

# Constants for data sampling in Data.py
PLUS_MINUS = 30

#Dataset Constants
DATA_FOLDER_PATH = Path("data")
DATA_FILE_NAME = DATA_FOLDER_PATH / "on_campus_2018.csv"
DATA_TIME_STEP = 15                     #Data's time step.
DATA_START_TIME = 0                     #Starting time.
DATA_MINS_IN_HR = 60                    #Number of minutes in an hr.
DATA_MID_DAY_MULT = 0.5                 #Mid day time step multiplier (Get 12pm).
DATA_LATE_CLASS_MULT = 0.66             #Late classes time multiplier (Get 8pm).
DATA_LATE_CLASS_CREDITS = 1             #Number of credits if coming late.

#Visualization contants.
VIS_OUT_PATH = Path("visualization")

#Simulation Variables
TIME_STEP = 1       #Default simulation time step (1 Minute by default).

#Dictionary of days to allow easy access to days.
DAYS = { "Mon":0, "Tue":1, "Wed":2, "Thu":3, "Fri":4 }
