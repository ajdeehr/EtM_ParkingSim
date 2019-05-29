
import numpy as N
from datetime import timedelta as TD
from datetime import datetime as DT

STUDENT = 0
FACULTY = 1
STAFF = 2


class Agent(object):
    def __repr__(self):
        return self.__str__()
        
    def __str__(self):
        string = "   ID = %s\nAgent = %s\n" \
                % (self.agent_ID, Agent.agent_type_as_str(self.agent_type))
        if self.agent_type is 0:
            string += "Credits = %s\nStayhours = %s\n" \
                % (self.credits,self.stay_hours )
        # if self.agent_type is 1:
        #     pass
            
        return string
        # self.credits = credits
        # self.agent_type =         self.stay_hours = stayhours
        # self.time_arrived = DT(2019, 5, 20, ta[0], ta[1])
        # self.agent_ID = agent_id
        # self.total_week_hours = 0
        # self.expected_week_hours = 0
    
    def __init__(self, agenttype=0, stayhours = 8, creditshours = 0, ta = (8, 45), agent_id = 0):
        self.credits = creditshours
        self.agent_type = agenttype
        self.stay_hours = stayhours
        self.time_arrived = DT(2019, 5, 20, ta[0], ta[1])
        self.agent_ID = agent_id
        self.total_week_hours = 0
        self.expected_week_hours = 0
        
        
        
    def update(self, currentTime):
        addedTime = TD(hours = self.stay_hours)
        if (self.time_arrived + addedTime) is currentTime:
            pass

    def agent_type_as_str(ag_type):
        if ag_type is 0:
            return "Student"
        elif ag_type is 1:
            return "Faculty"
        elif ag_type is 2:
            return "Staff"
            
        

    