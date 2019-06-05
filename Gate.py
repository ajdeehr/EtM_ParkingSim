

import random as rand
import Constants as C
import numpy as N
import queue
import sys

import Road
import Agent
import Vehicle

import Data

class Gate(object):

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        '''A method to get a string representation of a class'''

        #Print the garage information.
        out = "Gate: Dump *******************************" + "\n"
        out += "Gate: Total Number Of Agents Entered: " + str(len(self.agents_list)) + "\n"
        out += "Gate: Total Number Of Vehicles Entered: " + str(len(self.vehicle_list)) + "\n"
        out += "Gate: Total Number Of Agents Left: " + str(self.total_agents_left) + "\n"
        out += "Gate: Total Number Of Vehicles Left: " + str(self.total_vehicles_left) + "\n"
        out += "Gate: Number in going in Queue == " + str(self.q_going_in.qsize()) + "\n"
        out += "Gate: Number in going out Queue == " + str(self.q_going_out.qsize()) + "\n"
        out += "******************************************"
        return out

    def __init__(self):

        self.q_going_in = queue.Queue()
        self.q_going_out = queue.Queue()

        #added after first milestne meetup (wed 5/29)
        self.agents_list = []
        self.vehicle_list = []

        # self.vehicle_gen(50)

        self.num_vehicles_per_t = 0
        self.num_vehicle_per_t = 0

        self.total_vehicles_left = 0
        self.total_agents_left = 0

        #Key == arriving_time_step, Value == sum_of_all_arrival_times
        self.sum_t_to_gate = {}

        #Key == arriving_time_step, Value == num_of_agents_left_at_time_step
        #It is used for calcularing the average instant rate leaving.
        self.num_leaving = {}


    def estimate_vehicles(self, no_agent):

        if (no_agent == 0):
            return 0

        else:
            normal_dist_estimated_agent = N.floor((no_agent * 0.05) * N.random.randn() + no_agent)
            self.num_vehicles_per_t = normal_dist_estimated_agent

    def leave_gate(self):
        ''' A method which returns the vehicle if ant exist, if not it returns None'''
        if self.q_going_in.qsize() == 0:
            return None
        else:
            return self.q_going_in.get()

    def enter_gate(self, vehicle):
        ''' A method which puts the vehicle inside the gate (To go out)'''
        if vehicle is not None:
            self.q_going_out.put(vehicle)
        else:
            print("Gate: enter_gate(): Error, vehicle is None.", file=sys.stderr)


    def exit_gate(self, curr_t):
        ''' A method which exits all the cars at the gate and returns average
        leaving time, and number of agents leaving.'''

        num_agents_leaving = 0
        avg_time_to_leave = 0

        #Go through every agent leaving and calculate the sum of times.
        while self.q_going_out.qsize() != 0:
            vehicle = self.q_going_out.get()

            for agent in vehicle.agents:
                num_agents_leaving += 1
                avg_time_to_leave += agent.time_spent(curr_t)

            #Keep track of total agents and vehicles that left.
            self.total_agents_left += num_agents_leaving
            self.total_vehicles_left += 1

        #Calculate average time it took for them to leave.
        if num_agents_leaving != 0:
            avg_time_to_leave /= num_agents_leaving

        #Reset the going out queue.
        self.q_going_out = queue.Queue()

        return avg_time_to_leave, num_agents_leaving


    def vehicle_gen(self, curr_t):

        total_agent = 0
        total_vehicle = 0

        while total_agent < self.num_vehicles_per_t:
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
                curr_vehicle.num_of_agents = 1

                total_agent = total_agent + 1

            else:   #Add multiple passengers to vehicle if not standard vehicle.
                for j in range(rand.randint(C.MIN_PASSENGERS, C.MAX_PASSENGERS)):
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

                    #update number of agent in the current vehicle
                    curr_vehicle.num_of_agents += 1

                    #update number of agent
                    total_agent = total_agent + 1


            self.vehicle_list.append(curr_vehicle)
            self.q_going_in.put(curr_vehicle)
            total_vehicle += 1

        self.num_vehicles_per_t = total_agent
        self.num_vehicle_per_t = total_vehicle
