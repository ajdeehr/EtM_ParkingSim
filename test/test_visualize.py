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
import matplotlib.pyplot as plt
import numpy as N
from EtM_ParkingSim import Agent
from EtM_ParkingSim import Model
from EtM_ParkingSim import Garage 
from EtM_ParkingSim import visualize 

class Tests(object):
    
    def test_run_session(self):
        modelobj = Model.Model()
        modelobj.run_session("Mon")
        
        
if __name__ == "__main__":
    import unittest
    class TheseTests(unittest.TestCase, Tests): pass
    run_verbose = True
    run_verbose = False
    suite = unittest.TestSuite()
    suite.addtest(unittest.makeSuite(TheseTests))
    
    if run_verbose:
        unittest.TextTestRunner(verbosity=2).run(suite)
    else:
        unittest.TextTestRunner(verbosity=1).run(suite)
        

