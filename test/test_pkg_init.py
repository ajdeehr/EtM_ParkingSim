import copy
import EtM_ParkingSim

class Tests(object):
    def test_pkg_init(self):
        self.failUnless( hasattr(EtM_ParkingSim, "Model"))
        self.failUnless( hasattr(EtM_ParkingSim, "Agent"))
        self.failUnless( hasattr(EtM_ParkingSim, "Garage"))
        self.failUnless( hasattr(EtM_ParkingSim, "visualize"))