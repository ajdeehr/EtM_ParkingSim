

import numpy as N
import queue

import Road

class ParkingSpot(object):

    def __init__(self, parkingNumber=0, parkingType=0):

        #parkingID 
        self.parkingNumber = parkingNumber

        #parkingType, 0 = carpool, 1 = handicapped, 2 = normal
        self.parkingType = parkingType

        #state, 0 = free, 1 occupied
        self.state = 0

        #put the vehicle obj here
        self.vehicleOccupied = None
        
    def park(self, vehicle):
        self.vehicleOccupied = vehicle

    def leave(self):
        leavingVehicle = self.vehicleOccupied
        return leavingVehicle


class Garage(object):

    def __init__(self, garageName="Garage1", numberofSpot=300, numberofCarpoolSpot=20, numberofHandicappedSpot=20, trafficWeight=1):
        self.garageName = garageName
        self.numberofSpot = numberofSpot
        self.numberofCarpoolSpot = numberofCarpoolSpot
        self.numberofHandicappedSpot = numberofHandicappedSpot
        self.numberofNormalSpot = numberofSpot - numberofCarpoolSpot - numberofHandicappedSpot


        self.spotList = initParkingSpaces()

        #going in/out lane
        self.queueGoingIn = queue.Queue(maxsize=50)
        self.queueGoingOut = queue.Queue(maxsize=50)
        
        #how fast traffic is moving
        self.trafficWeight = trafficWeight

        #outside road link
        self.outsideRoad = None


    def initParkingSpaces(self):
        i = 1
        spotList = []
        while i < (numberofSpot+1):

            for range in (0, numberofCarpoolSpot):
                aCarpoolSpot = ParkingSpot(parkingNumber=i, parkingType=0)
                i = i + 1 #increase parkingNumber
                spotList.append(aCarpoolSpot)
            
            for range in (0, numberofHandicappedSpot):
                aHandicappedSpot = ParkingSpot(parkingNumber=i, parkingType=1)
                i = i + 1
                spotList.append(aHandicappedSpot)

            for range in (0, numberofNormalSpot):
                aSpot = ParkingSpot(parkingNumber=i, parkingType=2)
                i = i + 1
                spotList.append(aSpot)
            
        return spotList



    #mechanics for leave and enter garage and parking spot
    def vehicleEnterGarage(self, vehicle):
        queueGoingIn.put(vehicle)

    def vehicleEnterSpot(self, ParkingSpot):
        vehicle = queueGoingIn.get()
        ParkingSpot.park(vehicle)
    
    def vehicleLeavingSpot(self, ParkingSpot):
        vehicle = ParkingSpot.leave()
        queueGoingOut.put(vehicle)

    def vehicleLeavingGarage(self):
        vehicle = queueGoingOut.get()
        return vehicle

    def vehicleTurnAround(self):
        vehicle = queueGoingIn.get()
        queueGoingIn.put(vehicle)


    #find spot
    def findParkingSpot(self):
        
        while (queueGoingIn.empty() == False):
            
            for spot in self.spotList:

                if (spot.state == 0):
                    #use trafficWeight to wait out the parking process
                    vehicleEnterSpot(spot)
                    continue

            #if no more spot availble, random choice
            if N.random.randint(2) == 1:
                #leave the garage, enter back to road!
                vehicle = vehicleLeavingGarage()


            else:
                #reenter the garage
                vehicleTurnAround()