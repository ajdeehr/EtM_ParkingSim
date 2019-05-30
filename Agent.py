
import numpy as N
import Constants as C

class Agent(object):
    curr_agent_id = 0

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        string = "Agent: agent_id == " + str(self.agent_id) + "\n"
        string += "Agent: stay_hours == " + str(self.stay_hours) + "\n"
        string += "Agent: time_arrived == " + str(self.time_arrived) + "\n"
        string += "Agent: parking_spot_id == " str(self.parking_spot_id) + "\n"
        string += "Agent: lot_id == " + self.lot_id + "\n"

        return string

    def __init__(self, stayhours = 8):
        '''Default constructor which creates the object with the hours staying'''

        #Set the number of hours the student is staying.
        self.stay_hours = stayhours

        #Store and increment the agent id.
        self.agent_id = curr_agent_id
        curr_agent_id += 1

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
