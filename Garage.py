

import numpy as N
import queue

import Road
import Vehicle
import School

class ParkingSpot(object):

    def __init__(self, parkingNumber=0, parkingType=0):

        #parkingID 
        self.parkingNumber = parkingNumber

        # VEHICLE_TYPE_CAR = 0     #Represent the types of the vehicle.
        # VEHICLE_TYPE_BIKE = 1
        # VEHICLE_TYPE_HCAP = 2
        # VEHICLE_TYPE_CARPOOL = 3
        self.parkingType = parkingType

        #state, 0 = free, 1 occupied
        self.state = 0

        #put the vehicle obj here
        self.vehicleOccupied = None
        
    def park(self, vehicle):
        self.vehicleOccupied = vehicle

    def leave(self):
        leavingVehicle = self.vehicleOccupied
        self.vehicleOccupied = None
        return leavingVehicle


class Garage(object):

    def __init__(self, garageName="Garage1", numberofSpot=300, numberofCarpoolSpot=20, numberofHandicappedSpot=20, numberofEVSpot=0, trafficWeight=1):
        self.garageName = garageName
        self.numberofSpot = numberofSpot
        self.numberofCarpoolSpot = numberofCarpoolSpot
        self.numberofHandicappedSpot = numberofHandicappedSpot
        self.numberofEVSpot = numberofEVSpot
        self.numberofNormalSpot = numberofSpot - numberofCarpoolSpot - numberofHandicappedSpot - numberofEVSpot


        self.spotDict, self.spotPriorityQueue = self.initParkingSpaces()
        self.spotList = []

        #going in/out lane
        self.queueGoingIn = queue.Queue(maxsize=50)
        self.queueGoingOut = queue.Queue(maxsize=50)
        
        #how fast traffic is moving
        self.trafficWeight = trafficWeight

        #outside road link
        self.outsideRoad = None


    def initParkingSpaces(self):
        i = 1
        spotDict = {}
        spotPriorityQueue = queue.PriorityQueue()
        while i < (self.numberofSpot+1):

            for range in (0, self.numberofCarpoolSpot):
                aCarpoolSpot = ParkingSpot(parkingNumber=i, parkingType=0)
                i = i + 1 #increase parkingNumber
                spotList.append(aCarpoolSpot)
                # spotDict[i] = aCarpoolSpot
                # spotPriorityQueue.put(i, aCarpoolSpot)
            
            for range in (0, self.numberofHandicappedSpot):
                aHandicappedSpot = ParkingSpot(parkingNumber=i, parkingType=1)
                i = i + 1
                spotList.append(aHandicappedSpot)

                # spotDict[i] = aHandicappedSpot
                # spotPriorityQueue.put(i, aHandicappedSpot)

            for range in (0, self.numberofEVSpot):
                aEVSpot = ParkingSpot(parkingNumber=i, parkingType=3)
                i = i + 1
                spotList.append(aEVSpot)

                # spotDict[i] = aEVSpot
                # spotPriorityQueue.put(i, aEVSpot)
 
            for range in (0, self.numberofNormalSpot):
                aSpot = ParkingSpot(parkingNumber=i, parkingType=2)
                i = i + 1
                spotList.append(aSpot)

                # spotDict[i] = aSpot
                # spotPriorityQueue.put(i, aSpot)

        return spotDict, spotPriorityQueue



    #mechanics for leave and enter garage and parking spot
    def vehicleEnterGarage(self, vehicle):
        self.queueGoingIn.put(vehicle)

    def vehicleEnterSpot(self, ParkingSpot, vehicle):
        #vehicle = self.queueGoingIn.get()
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


    #find spot
    def findParkingSpot(self, vehicle):
        
        while (self.queueGoingIn.empty() == False):
            
            for spot in self.spotList:
                if (spot.state == 0):

                    if (vehicle.type == spot.parkingType):
                    #use trafficWeight to wait out the parking process
                        self.vehicleEnterSpot(spot, vehicle)

                        #make agents remember where they parked
                        for agent in vehicle.agents:
                            agent.parking_spot_id = spot.parkingNumber
                            agent.lot_id = garageName

                        #make agents go to School
                        while len(vehicle.agents) != 0:
                            School.go_to_school(vehicle.agents.pop())

                        #continue through the loop    
                        continue


                    else:
                        continue

            #if no more spot availble, random choice
            if N.random.randint(self.queueGoingIn.qsize()) > int(self.queueGoingIn.maxsize)/4:
                #leave the garage, enter back to road!
                vehicle = self.vehicleLeavingGarage()


            else:
                #reenter the garage
                self.vehicleTurnAround()
