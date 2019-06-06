import copy
from EtM_ParkingSim.Agent import Agent
from EtM_ParkingSim.Garage import Garage

class Tests(object):
    
    def test_zero_credits(self):
        agent = Agent()
        self.failUnless(agent.credits < 0)
        
    
    def test_bad_time(self):
        agent = Agent()
        self.failUnless(agent._test_negative_time(-40) == True)