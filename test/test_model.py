
import copy
from EtM_ParkingSim import Model

class Tests(object):
   
    def test_model_init(self):
        model = Model.Model()
        
        self.failUnless(model)

