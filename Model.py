import numpy as N
import random as R

import Agent
import Vehicle
import Road
import Garage
import Gate
import Constants as C

limit = 30

class Model(object):

    def __init__(self, dt=0.25, trafficWeight=1):

        self.trafficWeight = trafficWeight

        self.northGarage = Garage.Garage("North Garage", 300, 20, 20, 0, 1)
        self.southGarage = Garage.Garage("South Garage", 200, 10, 10, 0, 1)

        self.campusWayRoad = Road.Road(adjacentGarage=self.southGarage, adjacentGarage2=self.northGarage, trafficWeight = 1)

        self.northGarage.outsideRoad = self.campusWayRoad
        self.southGarage.outsideRoad = self.campusWayRoad

        self.numberGarage = 2

        self.gate = Gate.Gate()


def main():
    model = Model()
    
main()