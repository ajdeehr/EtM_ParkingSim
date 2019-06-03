

import random as rand
import Constants as C
import numpy as N
import queue

import Road
import Agent
import Vehicle

import Data

class Gate(object):

    def __init__(self):

        
        self.queueGoingIn = queue.Queue(maxsize=50)
        self.queueGoingOut = queue.Queue(maxsize=50)

        #added after first milestne meetup (wed 5/29)
        self.agents_list = []
        self.vehicle_list = []

        # self.vehicle_gen(50)

        self.num_agents_per_15_mins = 0
        self.num_vehicle_per_15_mins = 0
    

    def estimate_vehicle(row, col):

        if (Data.table[row, col] == 0):
            return 0

        else:
            estimated_agent = Data.table[row, col]
            normal_dist_estimated_agent = N.floor((estimated_agent * 0.05) * N.random.randn() + estimated_agent)

            self.num_agents_per_15_mins = normal_dist_estimated_agent

        

    def vehicle_gen(self):

        total_agent = 0
        total_vehicle = 0

        while total_agent < self.num_agents_per_15_mins:

            #Create a vehicle to add.
            curr_vehicle = Vehicle.Vehicle()

            cur_no_agent = 0

            #Add one passenger of standard or bike.
            if curr_vehicle.is_single_passenger():
                agent = Agent.Agent()
                curr_vehicle.add_agent(agent)
                self.agents_list.append(agent)
                curr_no_agent = cur_no_agent + 1
                #update number of agent
                curr_vehicle.num_of_agents = curr_no_agent

                total_agent = total_agent + 1

            else:   #Add multiple passengers to vehicle if not standard vehicle.
                for j in range(rand.randint(C.MIN_PASSENGERS, C.MAX_PASSENGERS)):
                    curr_vehicle.add_agent(Agent.Agent())
                    
                    curr_no_agent = cur_no_agent + 1
                    total_agent = total_agent + 1
                #update number of agent
                
                curr_vehicle.num_of_agents = j

            self.vehicle_list.append(curr_vehicle)
            self.queueGoingIn.put(curr_vehicle)
            curr_no_car = curr_no_car + 1

        self.num_agents_per_15_mins = total_agent
        self.num_vehicle_per_15_mins = total_vehicle
