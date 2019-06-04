import numpy as N
import random as R

import Agent
import Vehicle
import Road
import Garage
import Gate
import School

import Data

import Constants as C
import visualize as V
import matplotlib.pyplot as plt

import importlib

importlib.reload(V)
importlib.reload(Agent)


class Model(object):

    def __init__(self, dt=0.25, trafficWeight=1):

        self.trafficWeight = trafficWeight

        self.gate = Gate.Gate()

        # self.northGarage = Garage.Garage("North Garage", 300, 20, 20, 0, 1)
        self.south_garage = Garage.Garage("South Garage", number_of_spot=771,
                                         number_of_carpool_spot=23,
                                         number_of_handicapped_spot=20,
                                         number_of_EV_spot=12, trafficWeight=1, outsideRoad= self.campus_way_road)

        self.campus_way_road = Road.Road(2, 2, 3)


        self.numberGarage = 2



        self.school = School.School()

        self.num_days = 30
        self.dt = 0.15

        self.plot_figure = None
        self.plot_axis = None
        self.plot_image = None

    def run_session(self, num_days=30):

        minute_in_a_day = 1440
        no_steps = minute_in_a_day * num_days

        for self.step in range(1, no_steps + 1):

            # generate vehicle and agents in vehicle
            # every min
            self.gate.estimate_vehicle(Data.get_rate("Mon", self.step))
            self.gate.vehicle_gen(self.step)


            # added to park spot

            # enter road
            self.campus_way_road.enter_road(gate.q_going_out.get(), self.step)

            # enter garage
            cur_vehicle = self.campus_way_road.arrive_garage(self.step)
            self.south_garage.q_going_in.put(cur_vehicle)

            # have to add vehicle to parking spot
            self.south_garage.find_parking_spot(cur_vehicle, self.step)
            
            
            # checking when is time to leave
            self.school.leave(self.step)




            # check if all agents at the car yet
            for spot in self.southGarage.spotList:

                if (spot.vehicle_occupied.num_of_agents == len(
                        spot.vehicle_occupied.agents)):
                    # need to record leaving time
                    # ready to move out
                    self.southGarage.vehicleLeavingSpot(spot)

            # leaving garage
            cur_vehicle = self.southGarage.vehicleLeavingGarage()

            # enter road
            self.campusWayRoad.q_going_out.put(cur_vehicle)

            # leaving road
            cur_vehicle = self.campusWayRoad.q_going_out.get()

            # enter gate
            self.gate.q_going_out.put(cur_vehicle)

            # need to record spenttime for each vehicle's agent in the set

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

                self.southGarage.vehicleEnterSpot(self.southGarage.spot_dict["666"], vehicle)




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
    model.run_session_plot_out(num_days=30)


main()
