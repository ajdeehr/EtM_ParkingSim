# -*- coding: utf-8 -*-
#==============================================================================
#                        General Documentation
"""
"""
#------------------------------------------------------------------------------
#                       Additional Documentation
# Modification History:
# - 5 Jun 2019:  Original by Adam Deehring, CSS458 A,
#   University of Washington Bothell.
# Notes:
# - Written for Python 3.5.2.
#==============================================================================

#---------------- Module General Import and Declarations ----------------------
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