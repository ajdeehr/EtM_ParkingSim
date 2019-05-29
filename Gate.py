

import random as rand
import Constants as C
import numpy as N
import queue

import Road
import Agent
import Vehicle

class Gate(object):

    def __init__(self):

        
        self.queueGoingIn = queue.Queue(maxsize=50)
        self.queueGoingOut = queue.Queue(maxsize=50)

        #added after first milestne meetup (wed 5/29)
        self.agents_list = []
        self.vehicle_list = []
        generate_car() 



    def agent_init(self, rate):
        credits = N.zeros((0,), dtype='i')
        while (N.size(credits) < rate):
            a = N.random.normal(3,.5, 10).astype('i') * 5
            temp = a[N.where(N.logical_and(a > 0, a <= 20))]
            credits = N.concatenate([temp, credits])

        agents = N.ndarray((rate,), dtype=Agent.Agent)
        for i in range(rate):
            print("Student {:2}: Credits {:2}".format(i + 1, credits[i]))
            agents[i] = Agent.Agent(agenttype=C.AGENT_STUDENT,creditshours=credits[i], \
                            stayhours = (credits[i]//5) * 2, \
                            agent_id = i, ta = (8,30) )

        return agents




    def vehicle_init(self, rate, list_agents):
        vehicles = []
        curr_agent = 0
        while curr_agent > rate+1:
            #Create a vehicle to add.
            curr_vehicle = Vehicle.Vehicle()

            #Add one passenger of standard or bike.
            if curr_vehicle.is_single_passenger():
                curr_vehicle.add_agent(list_agents[curr_agent])
                curr_agent += 1
            else:   #Add multiple passengers to vehicle if not standard vehicle.
                for j in range(R.randint(C.MIN_PASSENGERS, C.MAX_PASSENGERS)):
                    curr_vehicle.add_agent(list_agents[curr_agent])
                    curr_agent += 1
            vehicles.append(curr_vehicle)
        return vehicles

        for i in range(len(vehicles)):
            print(vehicles[i])
        



    def generate_car(self, rate):

        self.agents_list = agent_init(rate) #has to do something with rate
        self.vehicle_list = vehicle_init(rate, agents_list) #has to do something with rate

        for vehicle in vehicle_list:
            
            #capture time somehow
            
            queueGoingIn.put(vehicle)