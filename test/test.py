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
#
# Notes:
# - Written for Python 3.5.2.
#==============================================================================

#---------------- Module General Import and Declarations ----------------------
import os
if (__name__ == '__main__') and (__package__ is None):
    filename = os.path.abspath(__file__)
    tests_dir = os.path.dirname(filename)
    package_dir = os.path.dirname(tests_dir)
    parent_to_package_dir = os.path.dirname(package_dir)
    os.sys.path.append(parent_to_package_dir)


import unittest
from EtM_ParkingSim import Agent
from EtM_ParkingSim import Model
import test_agent
import test_visualize
import test_pkg_init
import test_model


class SetUpTest(unittest.TestCase):
    def setUp(self):
        self.string_test = "Hello there"
        self.modelobj = Model.Model()
        self.garageobj = Garage.Garage()
        self.agentobj = Agent.Agent()

class Tests(object):
    def test_SetUp_string_test(self):
        self.failUnless(self.string_test == "Hello there")
         



class setUpTestTests(SetUpTest, Tests): pass
class AgentTest(SetUpTest, test_agent.Tests): pass
class ModelTest(SetUpTest, test_model.Tests): pass
class VisualizeTest(SetUpTest, test_visualize.Tests): pass
class PkgInitTest(SetUpTest, test_pkg_init.Tests): pass



if __name__ == "__main__":
    run_verbose = True
    run_verbose = False
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(setUpTestTests))
    suite.addTest(unittest.makeSuite(AgentTest))
    suite.addTest(unittest.makeSuite(ModelTest))
    suite.addTest(unittest.makeSuite(VisualizeTest))
    suite.addTest(unittest.makeSuite(PkgInitTest))
    
    if run_verbose:
        unittest.TextTestRunner(verbosity=2).run(suite)
    else:
        unittest.TextTestRunner(verbosity=1).run(suite)
        

