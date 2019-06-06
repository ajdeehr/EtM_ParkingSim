# -*- coding: utf-8 -*-
#==============================================================================
#                        General Documentation
"""
"""
#------------------------------------------------------------------------------
#                       Additional Documentation
# Modification History:
# - 24 May 2019:  Original by Adam Deehring, CSS458 A,
#   University of Washington Bothell.
# - Subsequent Revisions from Xavier Cheng, Ardalan Ahanchi,
#   and Dewey Nguyen
#
# Notes:
# - Written for Python 3.5.2.
#==============================================================================

#---------------- Module General Import and Declarations ----------------------
import numpy as N
import Constants as C
import Data

class Agent(object):
    curr_agent_id = 0

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        '''A method to get a string representation of a class'''

        out = "Agent: Dump *********************************" + "\n"
        out += "Agent: agent_id == " + str(self.agent_id) + "\n"
        out += "Agent: stay_time == " + str(self.stay_time) + "\n"
        out += "Agent: time_arrived == " + str(self.time_arrived) + "\n"
        out += "Agent: parking_spot_id == " + str(self.parking_spot_id) + "\n"
        out += "Agent: lot_id == " + str(self.lot_id) + "\n"
        out += "*********************************************"
        return out

    def __init__(self, curr_t, stayhours = 8, sigma = 5):
        '''Default constructor which creates the object with the hours staying'''

        #Get the total number of steps.
        num_steps = Data.get_num_steps()

        #Define the credits.
        self.credits = N.floor(3 * N.random.randn() + 15)

        #After mid day (Noon)
        if (curr_t > num_steps * C.DATA_MID_DAY_MULT):
            self.credits = N.floor(1 * (1 - curr_t / num_steps) \
                * N.random.randn() + 15 * (1 - curr_t / num_steps))

        #After the evening (8 pm)
        if (curr_t > num_steps * C.DATA_LATE_CLASS_MULT):
            self.credits = C.DATA_LATE_CLASS_CREDITS

        #Set the number of hours the student is staying.
        #C.MIN_NO_DAYS_SCHOOL = 2 (2 days of school in a week)
        #C.MAX_NO_DAYS_SCHOOL = 5 (5 days of school in a week)
        d = N.random.randint(C.MIN_NO_DAYS_SCHOOL, C.MAX_NO_DAYS_SCHOOL + 1)
        cr = self.credits / d
        self.stay_time = N.ceil(cr) * (60 / C.TIME_STEP)

        #Store and increment the agent id.
        self.agent_id = Agent.curr_agent_id
        Agent.curr_agent_id += 1

        #Added after first milestne meetup (wed 5/29)
        self.parking_spot_id = -1
        self.lot_id = "None"

    def time_start(self, curr_time):
        '''Save the current time to calculate waiting times.
        Will be called once when arrived to gate, and another time when leaving from school'''
        self.start_time = curr_time

    def time_spent(self, curr_time):
        '''Return the time spent since start_time.
        Will be called once when arrived to school, and another time when leaving from gate'''
        return curr_time - self.start_time

    def time_leaving_school(self, arrival_time):
        '''A method which returns the time step which the agent is supposed to
        leave the school based on the arrival time.'''
        return arrival_time + self.stay_time

    def _test_negative_time(self, time):
        self.time_start(time)
        return self.start_time >= 0
