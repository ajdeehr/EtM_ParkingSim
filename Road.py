

import numpy as N
import queue


import Garage
import Gate


class Road(object):
    """Create a road

    """

    def __init__(self, adjacentGarage=None, adjacentGarage2=None, adjacentGate=None, trafficWeight=1):
        self.length = 3    # depends on how long we want the road to be
        self.width = 3*16   # depends on how long we want the road to be
        self.adjacentGarage = adjacentGarage
        self.adjacentGarage2 = adjacentGarage2
        self.adjacentGate = adjacentGate

        self.vehicleList = []

        self.queueGoingIn = queue.Queue(maxsize=200)
        self.queueGoingOut = queue.Queue(maxsize=200)

        self.trafficWeight = trafficWeight

    def enterRoad(self):
        vehicle = self.adjacentGate.queueGoingIn.get()
        self.queueGoingIn.put(vehicle)
        
    def leaveRoad(self):
        vehicle = self.queueGoingInget()
        self.adjacentGate.queueGoingOut.put(vehicle)
    
    def leaveGarage(self):
        vehicle = self.adjacentGarage.vehicleLeavingGarage()
        self.queueGoingOut.put(vehicle)

    def enterGarage(self):

        while (self.queueGoingIn.empty() > int(self.queueGoingIn.maxsize/4)):
            
            if N.random.randint(2) == 1:
                #need a traffic weight
                vehicle = self.queueGoingIn.get()
                self.adjacentGarage.vehicleEnterGarage(vehicle)
                continue
            else:
                #need a traffic weight
                vehicle = self.queueGoingIn.get()
                self.adjacentGarage2.vehicleEnterGarage(vehicle)
                continue
