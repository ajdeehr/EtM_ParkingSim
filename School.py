# -*- coding: utf-8 -*-
#==============================================================================
#                        General Documentation
"""
"""
#------------------------------------------------------------------------------
#                       Additional Documentation
# Modification History:
# - 2 Jun 2019:  Original by Ardalan Ahanchi, CSS458 A,
#   University of Washington Bothell.
# - Subsequent Revisions from Xavier Cheng, Adam Deehring, and Dewey Nguyen
#
# Notes:
# - Written for Python 3.5.2.
#==============================================================================

#---------------- Module General Import and Declarations ----------------------

import random as rand
import Constants as C
import numpy as N

import Agent


class School(object):
    """ The container that all of the agents get placed into after they have 
	parked. The object stores when they will leave and arrive, placing them
	into a dictionary and storing the amounts, so that it can be reported 
	later.
	"""

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        '''A method to get a string representation of a class'''
        #Calculate the number still in school.
        num_agents_in_school = 0
        for timestep in self.agents_in_school:
            num_agents_in_school += len(self.agents_in_school[timestep])

        out = "School: Dump *****************************" + "\n"
        out += "School: Number of agents in school == " + \
               str(num_agents_in_school) + "\n"
        out += "******************************************"
        return out

    def __init__(self):
        ''' A simple default constructor to initialize the school dictionaries 
		'''

        #Key == time_step_to_leave , Value = list of Agents
        self.agents_in_school = {}

        #Key == arriving_time_step, Value == sum_of_all_arrival_times
        self.sum_t_to_school = {}

        #Key == arriving_time_step, Value == num_of_agents_arrived_at_time_step
        #It is used for calcularing the average instant rate arriving.
        self.num_arrived = {}


    def arrived(self, agent, curr_t):
        ''' A method which is called when the agent arrives to school, it adds 
		the agent to the dictionary, it also calculates the time spent from 
		enterance to arrival (Time on campus roads). '''

        #Calculate the time leaving, and add to the agents_in_school dict.
        leaving_time = agent.time_leaving_school(curr_t)

        #Check if the agents_in_school doesn't have the leaving_time_step key.
        if leaving_time not in self.agents_in_school:
            self.agents_in_school[leaving_time] = []

        #Add the agent to the list of agents leaving at that time.
        self.agents_in_school[leaving_time].append(agent)

        #Check if the current timestep is tracked in the dictionaries,
        #if it's not tracked, just set them to 0.
        if curr_t not in self.sum_t_to_school:
            self.sum_t_to_school[curr_t] = 0

        if curr_t not in self.num_arrived:
            self.num_arrived[curr_t] = 0

        #Add the time spent from gate to overall time for that arriving time 
		#step.
        self.sum_t_to_school[curr_t] += agent.time_spent(curr_t)

        #Increase the number of students arrived at that time step.
        self.num_arrived[curr_t] += 1


    def leave(self, curr_t):
        ''' A method which returns the agent which is ready to leave in the 
		current time step. If no agent is ready, it just returns None 
		'''

        #If none of the agents_in_school are ready to leave (Since key of the
        #dict is time_step_to_leave) just return None.
        if curr_t not in self.agents_in_school:
            return None
        elif len(self.agents_in_school[curr_t]) == 0:
            return None

        #Pop the agent to return from the list.
        leaving_agent = self.agents_in_school[curr_t].pop(0)

        #Begin the capture of time for this agent (So we can check the
        # time_spent again in the exit gate), and then return it.
        leaving_agent.time_start(curr_t)
        return leaving_agent


    def avg_time_to_arrive(self, time):
        ''' A method which returns the average time it took 
		(In terms of timesteps) for the students to arrive to the school at 
		the given time. 
		'''

        #Get the sum of times it took students to arrive to school at
        # given time.
        sum_times = 0
        if time in self.sum_t_to_school:
            sum_times = self.sum_t_to_school[time]

        #Get the number of students which were captured for that time step.
        num_times = 0
        if time in self.num_arrived:
            num_times = self.num_arrived[time]

        #If zero, just return the sum.
        if num_times == 0:
            return sum_times

        #Calculate average and return it.
        return sum_times / num_times


    def agents_arrived_at_t(self, time):
        ''' A method which returns the number of agents which arrived at time. 
		'''

        #If no agent has been recorded on that time, just return 0.
        if time not in self.num_arrived:
            return 0

        #Get the number arrived from the dictionary and return it.
        return self.num_arrived[time]
