

class Vehicle(object):
    def __repr__(self):
        return self.__str__()
        
    def __str__(self):
        return str(self.vehicle_type) + " " + str(self.occupants_list)
    
    def __init__(self, vehicletype, occupants, state):
        self.vehicle_type = vehicletype
        self.occupants_list = occupants
        self.state = state
        
    def park(parking_spot):
        pass
    
    # def move(intersection):
    #     pass
    #     
    def move(road):
        pass
        
    def leave(gate):
        pass
        
    def enter(gate):
        pass
    
    