import numpy as N
import queue

import Road
import Vehicle
import School


class ParkingSpot(object):

    def __init__(self, parkingNumber=0, parkingType=0):

        # parkingID
        self.parkingNumber = parkingNumber

        # VEHICLE_TYPE_CAR = 0     #Represent the types of the vehicle.
        # VEHICLE_TYPE_BIKE = 1
        # VEHICLE_TYPE_HCAP = 2
        # VEHICLE_TYPE_CARPOOL = 3
        self.parkingType = parkingType

        # state, 0 = free, 1 occupied
        self.state = 0

        # put the vehicle obj here
        self.vehicleOccupied = None

    def park(self, vehicle):
        self.vehicleOccupied = vehicle

    def leave(self):
        leavingVehicle = self.vehicleOccupied
        self.vehicleOccupied = None
        return leavingVehicle

    def get_parking_type(self):
        if self.parkingType is None:
            return 5
        else:
            return self.parkingType


class Garage(object):

    def __init__(self, garageName="Garage1", numberofSpot=771,
                 numberofCarpoolSpot=23, numberofHandicappedSpot=20,
                 numberofEVSpot=12, trafficWeight=1):
        self.garageName = garageName
        self.numberofSpot = numberofSpot
        self.blankspots = int(N.power(N.ceil(N.sqrt(numberofSpot)), 2) - numberofSpot)
        self.numberofCarpoolSpot = numberofCarpoolSpot
        self.numberofHandicappedSpot = numberofHandicappedSpot
        self.numberofEVSpot = numberofEVSpot
        self.numberofNormalSpot = numberofSpot - numberofCarpoolSpot - numberofHandicappedSpot - numberofEVSpot

        self.spotDict, self.spotPriorityQueue = self.initParkingSpaces()
        self.spotList = []

        # going in/out lane
        self.queueGoingIn = queue.Queue(maxsize=50)
        self.queueGoingOut = queue.Queue(maxsize=50)

        # how fast traffic is moving
        self.trafficWeight = trafficWeight

        # outside road link
        self.outsideRoad = None
        
    def initParkingSpaces(self):
        i = 1
        spotDict = {}
        spotPriorityQueue = queue.PriorityQueue()
        while i < (self.numberofSpot + 1):

            for spot in range(0, self.numberofCarpoolSpot):
                aCarpoolSpot = ParkingSpot(parkingNumber=i, parkingType=0)
                spotDict[str(i)] = aCarpoolSpot
                i = i + 1  # increase parkingNumber
                # spotList.append(aCarpoolSpot)
                
                # spotPriorityQueue.put(i, aCarpoolSpot)

            for spot in range(0, self.numberofHandicappedSpot):
                aHandicappedSpot = ParkingSpot(parkingNumber=i, parkingType=1)
                spotDict[str(i)] = aHandicappedSpot
                i = i + 1
                # spotList.append(aHandicappedSpot)

                
                # spotPriorityQueue.put(i, aHandicappedSpot)

            for spot in range(0, self.numberofEVSpot):
                aEVSpot = ParkingSpot(parkingNumber=i, parkingType=3)
                spotDict[str(i)] = aEVSpot
                i = i + 1
                # spotList.append(aEVSpot)

                
                # spotPriorityQueue.put(i, aEVSpot)

            for spot in range(0, self.numberofNormalSpot):
                aSpot = ParkingSpot(parkingNumber=i, parkingType=2)
                spotDict[str(i)] = aSpot
                i = i + 1
                # spotList.append(aSpot)

                
                # spotPriorityQueue.put(i, aSpot)

            for spot in range(0, self.blankspots):
                aSpot = ParkingSpot(parkingNumber=i, parkingType=None)
                spotDict[str(i)] = aSpot

                i = i + 1
                # spotList.append(aSpot)

                
        return spotDict, spotPriorityQueue

    # mechanics for leave and enter garage and parking spot
    def vehicleEnterGarage(self, vehicle):
        self.queueGoingIn.put(vehicle)

    def vehicleEnterSpot(self, ParkingSpot, vehicle):
        # vehicle = self.queueGoingIn.get()
        ParkingSpot.park(vehicle)

    def vehicleLeavingSpot(self, ParkingSpot):
        vehicle = ParkingSpot.leave()
        self.queueGoingOut.put(vehicle)

    def vehicleLeavingGarage(self):
        vehicle = self.queueGoingOut.get()
        return vehicle

    def vehicleTurnAround(self):
        vehicle = self.queueGoingIn.get()
        self.queueGoingIn.put(vehicle)

    # find spot
    def findParkingSpot(self, vehicle):

        while (self.queueGoingIn.empty() == False):

            for spot in self.spotList:
                if (spot.state == 0):

                    if (vehicle.type == spot.parkingType):
                        # use trafficWeight to wait out the parking process
                        self.vehicleEnterSpot(spot, vehicle)

                        # make agents remember where they parked
                        for agent in vehicle.agents:
                            agent.parking_spot_id = spot.parkingNumber
                            # agent.lot_id = garageName

                        # make agents go to School
                        while len(vehicle.agents) != 0:
                            School.go_to_school(vehicle.agents.pop())

                        # continue through the loop
                        continue


                    else:
                        continue

            # if no more spot availble, random choice
            if N.random.randint(self.queueGoingIn.qsize()) > int(
                    self.queueGoingIn.maxsize) / 4:
                # leave the garage, enter back to road!
                vehicle = self.vehicleLeavingGarage()


            else:
                # reenter the garage
                self.vehicleTurnAround()
