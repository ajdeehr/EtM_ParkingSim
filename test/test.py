    
import unittest

class SetUpTest(unittest.TestCase):
    def setUp(self):
        self.string_test = "Hello there"
        self.modelobj = model.Model()
        self.garageobj = garage.Garage()
        self.peopleobj = people.People()
class Tests(): pass


class setUpTestTests(SetUpTest, Tests): pass
class GarageTests(SetUpTest, Tests): pass
class PeopleTest(SetUpTest, Tests): pass
class ModelTest(SetUpTest, Tests): pass
class VisualizeTest(SetUpTest, Tests): pass
if __name__ == "__main__":
    run_verbose = True
    run_verbose = False
    suite = unittest.TestSuite()
    suite.addtest(unittest.makeSuite())
    suite.addtest(unittest.makeSuite())
    suite.addtest(unittest.makeSuite())
    
    if run_verbose:
        unittest.TextTestRunner(verbosity=2).run(suite)
    else:
        unittest.TextTestRunner(verbosity=2).run(suite)
        

