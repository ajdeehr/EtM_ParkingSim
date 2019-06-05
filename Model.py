import numpy as N
import random as R

import Agent
import Vehicle
import Road
import Garage
import Gate
import School
import sys

import Data

import Constants as C
import visualize as V
import matplotlib.pyplot as plt

import importlib

importlib.reload(V)
importlib.reload(Agent)


class Model(object):

    def log(self, str):
        print(str, " | ", self.step, file=sys.stderr)

    def __init__(self, dt=0.25, trafficWeight=1):

        self.trafficWeight = trafficWeight

        self.gate = Gate.Gate()

        self.campus_way_road = Road.Road(2, 2, 3)

        # self.northGarage = Garage.Garage("North Garage", 300, 20, 20, 0, 1)
        self.south_garage = Garage.Garage("South Garage", num_spot=771,
                                         num_carpool_spot=23,
                                         num_handicapped_spot=20,
                                         num_bike_spot=12)

        self.numberGarage = 2

        self.school = School.School()

        self.num_days = 30
        self.dt = 0.15

        self.plot_figure = None
        self.plot_axis = None
        self.plot_image = None

    def dump(self):
        print("\n\nTimestep", self.step, "***********************************************************************************", file=sys.stderr)
        print(self.gate)
        print(self.campus_way_road)
        print(self.south_garage)
        print(self.school)
        print("**************************************************************************************************\n", file=sys.stderr)

    def run_session(self, num_days=30):

        for self.step in range(Data.get_num_steps()):
            # generate vehicle and agents in vehicle
            # every min
            self.gate.estimate_agent(Data.get_rate("Mon", self.step))
            self.gate.vehicle_gen(self.step)


            for i in range(self.campus_way_road.lanes_in):
                #Leave the vehicle from the gate.
                vehicle = self.gate.leave_gate()
                if vehicle is not None:
                    # enter road
                    self.campus_way_road.enter_road(vehicle, self.step)

                # enter garage
                cur_vehicle = self.campus_way_road.arrive_garage(self.step)

                # have to add vehicle to parking spot
                if cur_vehicle is not None:
                    spot_id = self.south_garage.find_parking_spot(cur_vehicle)
                    if spot_id > 0:
                        #Send all the agents to school.
                        for agent in cur_vehicle.agents:
                            agent.parking_spot_id = spot_id
                            self.school.arrived(agent, self.step)

                        #Remove them from the vehicle.
                        cur_vehicle.agents = set()

                else:   #If not parking spots were found.
                    #Go back to the road to find parking.
                    #self.campus_way_road.enter_road(cur_vehicle, self.step)
                    self.campus_way_road.leave_garage(cur_vehicle, self.step)

            # checking when is time to leave
            leaving_agent = self.school.leave(self.step)
            while leaving_agent != None:
                self.south_garage.find_car(leaving_agent)
                leaving_agent = self.school.leave(self.step)

            # Go though all the lanes, and leave garage.
            for i in range(self.campus_way_road.lanes_out):
                # leaving garage
                cur_vehicle = self.south_garage.leave_garage()
                if cur_vehicle != None :
                    # enter road
                    self.campus_way_road.leave_garage(cur_vehicle, self.step)
                    cur_vehicle = self.south_garage.leave_garage()

                # leaving road
                cur_vehicle = self.campus_way_road.exit_road(self.step)
                if cur_vehicle is not None:
                    # enter gate
                    self.gate.q_going_out.put(cur_vehicle)

            #Remove the vehicle from the gate and get avg.
            avg_leaving, num_leaving = self.gate.exit_gate(self.step)

            self.dump()

    def run_sim(self, day):
        self.step = 0

        #Go through every single time step in the data file.
        for self.step in range(Data.get_num_steps()):

            #Generate cars and put agents in them based on the rate from data.
            self.gate.estimate_agent(Data.get_rate(day, self.step))
            self.gate.vehicle_gen(self.step)

            print(self.gate)
            vehicle_to_leave = self.gate.leave_gate()
            self.gate.enter_gate(vehicle_to_leave)



    def run_session_plot_out(self, num_days=1):

        minute_in_a_day = 1440
        no_steps = minute_in_a_day * num_days

        for self.step in range(1, no_steps + 1):
            print(self.step)
            # generate vehicle and agents in vehicle
            # every min
            print("car gen")
            self.gate.estimate_agent(Data.get_rate("Mon", self.step))
            self.gate.vehicle_gen(self.step)


            # need to record spenttime for each vehicle's agent in the set
            if self.step is 1:
                agent = Agent.Agent()
                print(agent)
                vehicle = Vehicle.Vehicle()
                vehicle.add_agent(agent)

                self.south_garage.vehicleEnterSpot(self.southGarage.spot_dict["666"], vehicle)




            if self.step is 1:
                plt.ion()
                self.plot_figure, self.plot_axis, self.plot_image = \
                    V.plot_campus(self)
                # self.plot_figure, self.plot_axis = V.plot_garage(self)
                # plt.show()

            else:
                # pass
                self.plot_figure, self.plot_axis, self.plot_image = \
                    V.plot_campus(self, use_obj=(self.plot_figure, self.plot_axis, self.plot_image))

            plt.pause(.001)


def main():
    model = Model()
    model.run_session(1)
    #model.run_sim("Mon")
    #model.run_session_plot_out(num_days=30)


main()
