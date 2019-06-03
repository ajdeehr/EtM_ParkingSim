
import numpy as N
import Constants as C

class Agent(object):
    curr_agent_id = 0

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        string = "Agent: agent_id == " + str(self.agent_id) + "\n"
        string += "Agent: stay_hours == " + str(self.stay_hours) + "\n"
        # string += "Agent: time_arrived == " + str(self.time_arrived) + "\n"
        # string += "Agent: parking_spot_id == " + str(self.parking_spot_id) + "\n"
        string += "Agent: lot_id == " + self.lot_id + "\n"

        return string

    def __init__(self, stayhours = 8):
        '''Default constructor which creates the object with the hours staying'''

        global curr_agent_id

        #This generate a number of a norm distro with mean 15 and sigma 5
        self.credits = N.floor(5 * N.random.randn() + 15)

        #Set the number of hours the student is staying.
        #C.MIN_NO_DAYS_SCHOOL = 2 (2 days of school in a week)
        #C.MAX_NO_DAYS_SCHOOL = 5 (5 days of school in a week)
        d = N.random.randint(C.MIN_NO_DAYS_SCHOOL, C.MAX_NO_DAYS_SCHOOL + 1)
        cr = self.credits / d
        self.stay_hours = N.ceil(cr)

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
        return arrival_time + self.stay_hours
