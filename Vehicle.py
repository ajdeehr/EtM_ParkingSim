

import random as rand
import Constants as C

class Vehicle(object):
    '''Create a Vehicle and Randomize the type and the number of occupants.
    '''

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        '''A method to get a string representation of a class'''
        out = "Vehicle: Type == " + str(self.type) + "\n"
        out += "Vehicle: State == " + str(self.state)
        return out

    def __init__(self):
        '''Default Constructor'''

        #Set the vehicle type by randomly assigning based on the constants.
        if rand.random() <  C.PERCENT_BIKE:         #If a Bike.
            self.type = C.VEHICLE_TYPE_BIKE
        elif rand.random() <  C.PERCENT_HCAP:       #If a Handicapped.
            self.type = C.VEHICLE_TYPE_HCAP
        elif rand.random() < C.PERCENT_CARPOOL:     #If Carpool.
            self.type = C.VEHICLE_TYPE_CARPOOL
        else:                                       #If a Regular Car.
            self.type = C.VEHICLE_TYPE_CAR

        #Set the state of the vehicle to moving by default.
        self.state = C.STATE_MOVING

        #The set which contains all the agents.
        self.agents = set()

    def add_agent(self, agent):
        '''Adds a new agent to this car'''
        self.agents.add(agent)

    def is_single_passenger(self):
        '''Returns if the car can accept multiple agents'''
        if self.type == VEHICLE_TYPE_CAR or self.type == VEHICLE_TYPE_BIKE:
            return true
        else
            return false

    def park(self):
        '''Sets the status to parked'''
        self.state = C.STATE_PARKED

    def leave(self):
        '''Sets the status to left'''
        self.state = C.STATE_LEFT

    def move(self):
        '''Sets the status to moving'''
        self.state = C.STATE_MOVING
