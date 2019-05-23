

import numpy as N
import queue


import Garage


class Road(object):
    """Create a road

    """

    def __init__(self, adjacentGarage=None, adjacentGarage2=None, trafficWeight=1):
        self.length = 1     # depends on how long we want the road to be
        self.width = 3*16   # depends on how long we want the road to be
        self.adjacentGarage = adjacentGarage
        self.adjacentGarage2 = adjacentGarage2

        self.vehicleList = []

        self.queueGoingIn = queue.Queue(maxsize=200)
        self.queueGoingOut = queue.Queue(maxsize=200)

        self.trafficWeight = trafficWeight


    def enterGarage(self):

        while (queueGoingIn.empty() == False):
            
            if N.random.randint(2) == 1:
                #need a traffic weight
                vehicle = queueGoingIn.get()
                adjacentGarage.vehicleEnterGarage(vehicle)
                continue
            else:
                #need a traffic weight
                vehicle = queueGoingIn.get()
                adjacentGarage2.vehicleEnterGarage(vehicle)
                continue
