import numpy as N
import random as R

import Agent
import Vehicle
import Road
import Garage
import Constants as C

limit = 30

class Model(obj):

    def __init__(self, dt=0.25, trafficWeight=1):

        self.trafficWeight = trafficWeight

        self.northGarage = Garage("North Garage", 300, 20, 20, 0, 1)
        self.southGarage = Garage("South Garage", 200, 10, 10, 0, 1)

        self.campusWayRoad = Road(adjacentGarage=self.southGarage, adjacentGarage2=self.northGarage, trafficWeight = 1)

        self.northGarage.outsideRoad = self.campusWayRoad
        self.southGarage.outsideRoad = self.campusWayRoad

        self.numberGarage = 2

        self.agents_list = self.agent_init()

        self.vehicleList = self.makeVehicleList(self.agents_list)



    def agent_init(self):
        credits = N.zeros((0,), dtype='i')
        while (N.size(credits) < limit):
            a = N.random.normal(3,.5, 10).astype('i') * 5
            temp = a[N.where(N.logical_and(a > 0, a < 20))]
            credits = N.concatenate([temp, credits])

        agents = N.ndarray((limit,), dtype=Agent.Agent)
        for i in range(limit * 3):
            # print("Student {:2}: Credits {:2}".format(i + 1, credits[i]))
            agents[i] = Agent.Agent(agenttype=C.AGENT_STUDENT,creditshours=credits[i], \
                            stayhours = (credits[i]//5) * 2, \
                            agent_id = i, ta = (8,30) )

        return agents

    def makeVehicleList(self, list_agents):
        vehicles = []
        curr_agent = 0
        for i in range(limit):
            #Create a vehicle to add.
            curr_vehicle = Vehicle()

            #Add one passenger of standard or bike.
            if curr_vehicle.is_single_passenger():
                curr_vehicle.add_agent(vehicles[curr_agent])
                curr_agent += 1
            else:   #Add multiple passengers to vehicle if not standard vehicle.
                for j in range(R.randint(C.MIN_PASSENGER, C.MAX_PASSENGERS)):
                    curr_vehicle.add_agent(vehicles[curr_agent])
                    curr_agent += 1

        return vehicles

        # for i in range(len(vehicles)):
        #     print(vehicles[i])
