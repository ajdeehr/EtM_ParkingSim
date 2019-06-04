

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

        self.q_going_in = queue.Queue(maxsize=50)
        self.q_going_out = queue.Queue(maxsize=50)

        #added after first milestne meetup (wed 5/29)
        self.agents_list = []
        self.vehicle_list = []

        # self.vehicle_gen(50)

        self.num_agents_per_15_mins = 0
        self.num_vehicle_per_15_mins = 0


    def estimate_agent(no_agent):

        if (no_agent == 0):
            return 0

        else:
            normal_dist_estimated_agent = N.floor((no_agent * 0.05) * N.random.randn() + no_agent)
            self.num_agents_per_15_mins = normal_dist_estimated_agent



    def vehicle_gen(self, curr_t):

        total_agent = 0
        total_vehicle = 0

        while total_agent < self.num_agents_per_15_mins:

            #Create a vehicle to add.
            curr_vehicle = Vehicle.Vehicle()

            cur_no_agent_in_a_car = 0

            #Add one passenger of standard or bike.
            if curr_vehicle.is_single_passenger():

                #make a a new agent
                agent = Agent.Agent()

                #record time_start
                agent.time_start(curr_t)

                #add agent to the current car
                curr_vehicle.add_agent(agent)

                #add to list of agents
                self.agents_list.append(agent)

                #increment
                curr_no_agent_in_a_car = cur_no_agent_in_a_car + 1

                #update number of agent in the current vehical
                curr_vehicle.num_of_agents = curr_no_agent_in_a_car

                total_agent = total_agent + 1

            else:   #Add multiple passengers to vehicle if not standard vehicle.
                for j in range(rand.randint(C.MIN_PASSENGERS, C.MAX_PASSENGERS)):
                    
                    #make a a new agent
                    agent = Agent.Agent()
                    
                    #record time_start
                    agent.time_start(curr_t)

                    #add agent to the current car
                    curr_vehicle.add_agent()

                    #add to list of agents
                    self.agents_list.append(agent)

                    #increment
                    curr_no_agent_in_a_car = cur_no_agent_in_a_car + 1

                    #update number of agent in the current vehicle
                    curr_vehicle.num_of_agents = curr_no_agent_in_a_car

                    #update number of agent
                    total_agent = total_agent + 1

                #update number of agent in the current vehicle
                curr_vehicle.num_of_agents = curr_no_agent_in_a_car



            self.vehicle_list.append(curr_vehicle)
            self.q_going_in.put(curr_vehicle)
            total_vehicle += 1

        self.num_agents_per_15_mins = total_agent
        self.num_vehicle_per_15_mins = total_vehicle
