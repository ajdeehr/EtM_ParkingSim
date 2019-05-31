

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
        vehicle_gen()



    def vehicle_gen(self, no_cars):

        curr_no_car = 0

        while curr_no_car < no_cars:
            #Create a vehicle to add.
            curr_vehicle = Vehicle.Vehicle()

            cur_no_agent = 0

            #Add one passenger of standard or bike.
            if curr_vehicle.is_single_passenger():
                curr_vehicle.add_agent(Agent())
                curr_no_agent = cur_no_agent + 1
                #update number of agent
                curr_vehicle.num_of_agents = curr_no_agent

            else:   #Add multiple passengers to vehicle if not standard vehicle.
                for j in range(rand.randint(C.MIN_PASSENGERS, C.MAX_PASSENGERS)):
                    curr_vehicle.add_agent(Agent())
                    curr_no_agent = cur_no_agent + 1
                #update number of agent
                curr_vehicle.num_of_agents = curr_no_agent


            queueGoingIn.put(curr_vehicle)
            curr_no_car = curr_no_car + 1
