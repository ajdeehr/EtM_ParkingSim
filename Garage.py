import numpy as N
import queue

import Road
import Vehicle
import School
import Constants as C


class ParkingSpot(object):

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        '''A method to get a string representation of a class'''

        #Print the garage information.
        out = "ParkingSpot: Dump ********************************" + "\n"
        out += "ParkingSpot: Spot ID == " + str(self.parking_number) + "\n"
        out += "ParkingSpot: Parking Type == " + str(self.parking_type) + "\n"
        out += "ParkingSpot: Is Occupied == " + str(self.vehicle_occupied != None) + "\n"
        out += "*************************************************"
        return out

    def __init__(self, parking_number=0, parking_type="Blank"):

        # parkingID
        self.parking_number = parking_number

        # VEHICLE_TYPE_CAR = 0     #Represent the types of the vehicle.
        # VEHICLE_TYPE_BIKE = 1
        # VEHICLE_TYPE_HCAP = 2
        # VEHICLE_TYPE_CARPOOL = 3
        self.parking_type = parking_type

        # put the vehicle obj here
        self.vehicle_occupied = None


    def get_parking_type(self):
        if self.state is 1:
            return 4
        if self.parking_type is None:
            return 5
        else:
            return self.parking_type


class Garage(object):

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        '''A method to get a string representation of a class'''

        #Print the garage information.
        out = "Garage: Dump *****************************" + "\n"
        out += "Garage: Number Filled == " + str(self.utilization()) + "\n"
        out += "Garage: Number of Spots == " + str(self.num_spot) + "\n"
        out += "Garage: Number in going in Queue == " + str(self.q_going_in.qsize()) + "\n"
        out += "Garage: Number in going out Queue == " + str(self.q_going_out.qsize()) + "\n"
        out += "******************************************"
        return out
    
    def __init__(self, garage_name="Garage1", num_spot=771,
                 num_carpool_spot=23, num_handicapped_spot=20,
                 num_bike_spot=12, garage_width=31):
        self.garage_name = garage_name
        self.num_spot = num_spot

        self.blankspots = (int(N.ceil(self.num_spot / garage_width)) * garage_width) - self.num_spot
        
        self.num_carpool_spot = num_carpool_spot
        self.num_handicapped_spot = num_handicapped_spot
        self.num_bike_spot = num_bike_spot
        self.num_normal_spot = num_spot - num_carpool_spot - num_handicapped_spot - num_bike_spot        
        self.garage_width = garage_width
        
        
        self.curr_id = 1
        self.spot_dict = {}

        #Initialize all the parking spaces.
        self.init_parking_spaces(C.VEHICLE_TYPES["Car"], self.num_normal_spot)
        self.init_parking_spaces(C.VEHICLE_TYPES["Bike"], self.num_bike_spot)
        self.init_parking_spaces(C.VEHICLE_TYPES["HCap"], self.num_handicapped_spot)
        self.init_parking_spaces(C.VEHICLE_TYPES["Carpool"], self.num_carpool_spot)

        # going in/out lane
        self.q_going_in = queue.Queue()
        self.q_going_out = queue.Queue()

    def utilization(self):
        ''' A method which returns the utilization size (number of filled spots) '''

        #Calculate the number of spots that are filled.
        num_filled = 0
        for dict in self.spot_dict:
            for spot in self.spot_dict[dict]:
                if self.spot_dict[dict][spot].vehicle_occupied is not None:
                    #print(self.spot_dict[dict][spot].parking_number)
                    num_filled += 1

        return num_filled


    def init_parking_spaces(self, spot_type, size):
        ''' A method which initializes the list for the parking types'''

        self.spot_dict[spot_type] = {}

        #Create and initiate parking spots.
        for i in range(size):
            self.spot_dict[spot_type][self.curr_id] = ParkingSpot(self.curr_id, spot_type)
            self.curr_id += 1

    def leave_garage(self):
        ''' A method which returns the vehicle if any exist, if not it returns None'''
        if self.q_going_out.qsize() == 0:
            return None
        else:
            return self.q_going_out.get()

    #Find the agent's car and put it in the out queue.
    def find_car(self, agent):
        #Add the agent to the leaving car.
        for dict in self.spot_dict:
            if agent.parking_spot_id in self.spot_dict[dict]:
                org_id = agent.parking_spot_id

                agent.parking_spot_id = 0
                self.spot_dict[dict][org_id].vehicle_occupied.add_agent(agent)

                vehicle = self.spot_dict[dict][org_id].vehicle_occupied
                #Check if all the passengers are here to leave.
                if len(vehicle.agents) == vehicle.num_of_agents:
                    self.q_going_out.put(vehicle)
                    self.spot_dict[dict][org_id].vehicle_occupied = None

    def find_parking_spot(self, vehicle):
        ''' Find spot, if not successful, return -1. '''
        for spot in self.spot_dict[vehicle.type]:
            if self.spot_dict[vehicle.type][spot].vehicle_occupied == None:
                self.spot_dict[vehicle.type][spot].vehicle_occupied = vehicle
                return self.spot_dict[vehicle.type][spot].parking_number

        return -1
