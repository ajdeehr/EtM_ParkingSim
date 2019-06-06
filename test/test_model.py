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
from EtM_ParkingSim import Model

class Tests(object):
   
    def test_model_init(self):
        model = Model.Model()
        
        self.failUnless(model)

