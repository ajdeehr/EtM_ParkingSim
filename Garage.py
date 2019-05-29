

import numpy as N
import queue

import Road

class ParkingSpot(object):

    def __init__(self, parkingNumber=0, parkingType=0):

        #parkingID 
        self.parkingNumber = parkingNumber

        #parkingType, 0 = carpool, 1 = handicapped, 2 = normal, 3 = EV
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

    def __init__(self, garageName="Garage1", numberofSpot=300, numberofCarpoolSpot=20, numberofHandicappedSpot=20, numberofEVSpot=0, trafficWeight=1):
        self.garageName = garageName
        self.numberofSpot = numberofSpot
        self.numberofCarpoolSpot = numberofCarpoolSpot
        self.numberofHandicappedSpot = numberofHandicappedSpot
        self.numberofEVSpot = numberofEVSpot
        self.numberofNormalSpot = numberofSpot - numberofCarpoolSpot - numberofHandicappedSpot - numberofEVSpot


        self.spotDict, self.spotPriorityQueue = self.initParkingSpaces()

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
                spotDict[i] = aCarpoolSpot
                spotPriorityQueue.put(i, aCarpoolSpot)
            
            for range in (0, self.numberofHandicappedSpot):
                aHandicappedSpot = ParkingSpot(parkingNumber=i, parkingType=1)
                i = i + 1
                spotDict[i] = aHandicappedSpot
                spotPriorityQueue.put(i, aHandicappedSpot)

            for range in (0, self.numberofEVSpot):
                aEVSpot = ParkingSpot(parkingNumber=i, parkingType=3)
                i = i + 1
                spotDict[i] = aEVSpot
                spotPriorityQueue.put(i, aEVSpot)
 
            for range in (0, self.numberofNormalSpot):
                aSpot = ParkingSpot(parkingNumber=i, parkingType=2)
                i = i + 1
                spotDict[i] = aSpot
                spotPriorityQueue.put(i, aSpot)

        return spotDict, spotPriorityQueue



    #mechanics for leave and enter garage and parking spot
    def vehicleEnterGarage(self, vehicle):
        self.queueGoingIn.put(vehicle)

    def vehicleEnterSpot(self, ParkingSpot):
        vehicle = self.queueGoingIn.get()
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
    def findParkingSpot(self):
        
        while (self.queueGoingIn.empty() == False):
            
            for spot in self.spotList:

                if (spot.state == 0):
                    #use trafficWeight to wait out the parking process
                    self.vehicleEnterSpot(spot)
                    continue

            #if no more spot availble, random choice
            if N.random.randint(self.queueGoingIn.qsize()) > int(self.queueGoingIn.maxsize)/4:
                #leave the garage, enter back to road!
                vehicle = self.vehicleLeavingGarage()


            else:
                #reenter the garage
                self.vehicleTurnAround()
