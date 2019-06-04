

import random as rand
import Constants as C
import Garage
import Gate
import Road

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

    def __init__(self, environment=Gate):
        '''Default Constructor'''

        self.environment = environment
        #Set the vehicle type by randomly assigning based on the constants.
        if rand.random() <  C.PERCENT_BIKE:         #If a Bike.
            self.type = C.VEHICLE_TYPE_BIKE
        elif rand.random() <  C.PERCENT_HCAP:       #If a Handicapped.
            self.type = C.VEHICLE_TYPE_HCAP
        elif rand.random() < C.PERCENT_CARPOOL:     #If Carpool.
            self.type = C.VEHICLE_TYPE_CARPOOL
        else:                                       #If a Regular Car.
            self.type = C.VEHICLE_TYPE_CAR


        #The set which contains all the agents.
        self.agents = set()

        #added after first milestne meetup (wed 5/29)
        self.num_of_agents = 0

    def add_agent(self, agent):
        '''Adds a new agent to this car'''
        self.agents.add(agent)

    def remove_agent(self, agent):
        '''Remove one agent and return it to the calling function'''
        return self.agents.pop()

    def is_single_passenger(self):
        '''Returns if the car can accept multiple agents'''
        if self.type == C.VEHICLE_TYPE_CAR or self.type == C.VEHICLE_TYPE_BIKE:
            return True
        else:
            return False
