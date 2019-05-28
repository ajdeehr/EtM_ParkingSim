import numpy as N

import Agent
import Vehicle
import Road
import Garage

STUDENT = 0
FACULTY = 1
STAFF = 2

STANDARD = 0
HANDICAP = 1
CARPOOL = 2

PARKED = 0
MOVING = 1

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
            a = N.random.normal(15,1.5, 10).astype('i')
            temp = a[N.where(N.logical_and(a > 0, a < 20))]
            credits = N.concatenate([temp, credits])
        
        agents = N.ndarray((limit,), dtype=Agent.Agent)
        for i in range(limit):
            # print("Student {:2}: Credits {:2}".format(i + 1, credits[i]))
            agents[i] = Agent.Agent(agenttype=STUDENT,creditshours=credits[i], \
                            stayhours = (credits[i]//5) * 2, \
                            agent_id = i, ta = (8,30) )
        
        return agents
      
    def makeVehicleList(self, list_agents):
        vehicles = []
        ite = 0
        while ite < limit:
            if N.random.random() > .95:
                vehicles.append(Vehicle.Vehicle(STANDARD, \
                            [list_agents[ite], list_agents[ite+1]], MOVING))
                ite = ite + 1
            else:
                vehicles.append(Vehicle.Vehicle(STANDARD, \
                            [list_agents[ite]], MOVING))
            ite = ite + 1
    
        return w
        # for i in range(len(vehicles)):
        #     print(vehicles[i])
