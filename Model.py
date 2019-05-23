

import numpy as N

import Road
import Garage

class Model(obj):

    def __init__(self, dt=0.25, trafficWeight=1):

        self.trafficWeight = trafficWeight

        self.northGarage = Garage("North Garage", 300, 20, 20, 1)
        self.southGarage = Garage("South Garage", 200, 10, 10, 1)

        self.campusWayRoad = Road(adjacentGarage=self.southGarage, adjacentGarage2=self.northGarage, trafficWeight = 1)

        self.northGarage.outsideRoad = self.campusWayRoad
        self.southGarage.outsideRoad = self.campusWayRoad

        self.numberGarage = 2

        self.vehicleList = makeVehicleList()


