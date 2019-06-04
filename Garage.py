import numpy as N
import queue

import Road
import Vehicle
import School


class ParkingSpot(object):

    def __init__(self, parking_number=0, parking_type=0):

        # parkingID
        self.parking_number = parking_number

        # VEHICLE_TYPE_CAR = 0     #Represent the types of the vehicle.
        # VEHICLE_TYPE_BIKE = 1
        # VEHICLE_TYPE_HCAP = 2
        # VEHICLE_TYPE_CARPOOL = 3
        self.parking_type = parking_type

        # state, 0 = free, 1 occupied
        self.state = 0

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

    def __init__(self, garage_name="Garage1", number_of_spot=771,
                 number_of_carpool_spot=23, number_of_handicapped_spot=20,
                 number_of_EV_spot=12, trafficWeight=1, outsideRoad=campus_way_road):
        self.garage_name = garage_name
        self.number_of_spot = number_of_spot
        
        self.blank_spots = int(N.power(N.ceil(N.sqrt(number_of_spot)), 2) - number_of_spot)

        self.number_of_carpool_spot = number_of_carpool_spot
        self.number_of_handicapped_spot = number_of_handicapped_spot
        self.number_of_EV_spot = number_of_EV_spot
        self.number_of_normal_spot = number_of_spot - number_of_carpool_spot - number_of_handicapped_spot - number_of_EV_spot

        self.spot_dict = self.init_parking_spaces()

        # going in/out lane
        self.q_going_in = queue.Queue(maxsize=50)
        self.q_going_out = queue.Queue(maxsize=50)

        # how fast traffic is moving
        self.traffic_weight = trafficWeight

        # outside road link
        self.outside_road = None
        


    def init_parking_spaces(self):
        i = 1
        spot_dict = {}
        spotPriorityQueue = queue.PriorityQueue()
        while i < (self.number_of_spot + 1):

            for spot in range(0, self.number_of_carpool_spot):
                aCarpoolSpot = ParkingSpot(parking_number=i, parking_type=0)
                spot_dict[str(i)] = aCarpoolSpot
                i = i + 1  # increase parking_number

            for spot in range(0, self.number_of_handicapped_spot):
                aHandicappedSpot = ParkingSpot(parking_number=i, parking_type=1)
                spot_dict[str(i)] = aHandicappedSpot
                i = i + 1

            for spot in range(0, self.number_of_EV_spot):
                aEVSpot = ParkingSpot(parking_number=i, parking_type=3)
                spot_dict[str(i)] = aEVSpot
                i = i + 1


            for spot in range(0, self.number_of_normal_spot):
                aSpot = ParkingSpot(parking_number=i, parking_type=2)
                spot_dict[str(i)] = aSpot
                i = i + 1


            for spot in range(0, self.blank_spots):
                aSpot = ParkingSpot(parking_number=i, parking_type=None)
                spot_dict[str(i)] = aSpot
                i = i + 1
                # spotList.append(aSpot)

                
        return spot_dict, spotPriorityQueue


    # find spot
    def find_parking_spot(self, vehicle, curr_t):

        while (self.q_going_in.empty() == False):

            #CAR
            if vehicle.type is 0:

                for i in range(self.number_of_spot - self.number_of_normal_spot, self.number_of_spot):
                    spot = spot_dict[str(i)]
                    
                    if spot.vehicle_occupied == None:
                        spot = vehicle

                        # make agents remember where they parked
                        for agent in vehicle.agents:
                            agent.parking_spot_id = spot.parking_number
                            agent.time_spent(curr_t)
                            # agent.lot_id = garage_name

                        # make agents go to School
                        while len(vehicle.agents) != 0:
                            School.go_to_school(vehicle.agents.pop())

                    else:
                        pass

                if len(vehicle.agents) != 0:
                    q_going_out.put(vehicle)

            #BIKE
            elif vehicle.type is 1:
                pass

            #HCAP
            elif vehicle.type is 2:

                for i in range(self.number_of_carpool_spot, self.number_of_carpool_spot + self.number_of_handicapped_spot):

                    spot = spot_dict[str(i)]

                    if spot.vehicle_occupied == None:

                        # make agents remember where they parked
                        for agent in vehicle.agents:
                            agent.parking_spot_id = spot.parking_number
                            agent.time_spent(curr_t)
                            # agent.lot_id = garage_name

                        # make agents go to School
                        while len(vehicle.agents) != 0:
                            School.go_to_school(vehicle.agents.pop())

                    else:
                        pass

                if len(vehicle.agents) != 0:
                    q_going_out.put(vehicle)



            #CARPOOL
            else:

                for i in range(self.number_of_carpool_spot + self.number_of_handicapped_spot, self.number_of_spot - self.number_of_normal_spot):
                    
                    spot = spot_dict[str(i)]

                    if spot.vehicle_occupied == None:

                        # make agents remember where they parked
                        for agent in vehicle.agents:
                            agent.parking_spot_id = spot.parking_number
                            agent.time_spent(curr_t)
                            # agent.lot_id = garage_name

                        # make agents go to School
                        while len(vehicle.agents) != 0:
                            School.arrived(vehicle.agents.pop(), curr_t)

                    else:
                        # continue through the loop
                        pass

                if len(vehicle.agents) != 0:
                    q_going_out.put(vehicle)




            # if no more spot availble, random choice
            if N.random.randint(self.q_going_in.qsize()) > int(
                    self.q_going_in.maxsize) / 4:
                # leave the garage, enter back to road!
                self.outside_road.leave_garage(vehicle)

            else:
                self.q_going_in.put(vehicle)
