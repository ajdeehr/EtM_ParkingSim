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
import EtM_ParkingSim

class Tests(object):
    def test_pkg_init(self):
        self.failUnless( hasattr(EtM_ParkingSim, "Model"))
        self.failUnless( hasattr(EtM_ParkingSim, "Agent"))
        self.failUnless( hasattr(EtM_ParkingSim, "Garage"))
        self.failUnless( hasattr(EtM_ParkingSim, "visualize"))