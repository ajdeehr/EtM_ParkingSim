import numpy as N
import random as R

import Agent
import Vehicle
import Road
import Garage
import Gate
import School
import Constants as C
import visualize as V
import matplotlib.pyplot as plt

import importlib

importlib.reload(V)
importlib.reload(Agent)

limit = 30


class Model(object):

    def __init__(self, dt=0.25, trafficWeight=1):

        self.trafficWeight = trafficWeight

        # self.northGarage = Garage.Garage("North Garage", 300, 20, 20, 0, 1)
        self.southGarage = Garage.Garage("South Garage", numberofSpot=771,
                                         numberofCarpoolSpot=23,
                                         numberofHandicappedSpot=20,
                                         numberofEVSpot=12, trafficWeight=1)

        self.campusWayRoad = Road.Road(adjacentGarage=self.southGarage,
                                       adjacentGarage2=None, trafficWeight=1)

        # self.northGarage.outsideRoad = self.campusWayRoad
        self.southGarage.outsideRoad = self.campusWayRoad

        self.numberGarage = 2

        self.gate = Gate.Gate()

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
            # every 30 mins
            if (self.step % 30 == 0):
                self.gate.vehicle_gen(400)  # 400 is just place holder

            # need to record starttime for each vehicle's agent in the set

            # added to park spot

            # enter road
            if (self.step % 2 == 0):  # every ~2 mins
                cur_vehicle = self.gate.queueGoingIn.get()

                self.campusWayRoad.queueGoingIn.put(cur_vehicle)

                cur_vehicle = self.campusWayRoad.queueGoingIn.get()

            # enter garage
            if (self.step % 4 == 0):  # every ~4 mins
                self.southGarage.vehicleEnterGarage(cur_vehicle)

                cur_vehicle = self.southGarage.queueGoingIn.get()
                self.southGarage.findParkingSpot(cur_vehicle)

                # need to record spenttime for each vehicle's agent in the set

            # checking when is time to leave
            for agent in self.school.agent_list:

                if (agent.stay_hours * 60 == self.step):
                    # move to lot
                    # need to record starttime for each vehicle's agent in the set

                    self.school.move_to_lot(agent)  # need to make this method
                    self.school.agent_list.remove(agent)

            # check if all agents at the car yet
            for spot in self.southGarage.spotList:

                if (spot.vehicleOccupied.num_of_agents == len(
                        spot.vehicleOccupied.agents)):
                    # need to record leaving time
                    # ready to move out
                    self.southGarage.vehicleLeavingSpot(spot)

            # leaving garage
            cur_vehicle = self.southGarage.vehicleLeavingGarage()

            # enter road
            self.campusWayRoad.queueGoingOut.put(cur_vehicle)

            # leaving road
            cur_vehicle = self.campusWayRoad.queueGoingOut.get()

            # enter gate
            self.gate.queueGoingOut.put(cur_vehicle)

            # need to record spenttime for each vehicle's agent in the set

    def run_session_plot_out(self, num_days=1):

        minute_in_a_day = 1440
        no_steps = minute_in_a_day * num_days

        for self.step in range(1, no_steps + 1):
            print(self.step)
#             # generate vehicle and agents in vehicle
#             # every 30 mins
#             if (self.step % 30 == 0):
#                 print("car gen")
#                 self.gate.vehicle_gen(400)  # 400 is just place holder
# 
#             # need to record starttime for each vehicle's agent in the set
# 
#             # added to park spot
# 
#             # enter road
#             if (self.step % 2 == 0):  # every ~2 mins
#                 print("enter road")
#                 cur_vehicle = self.gate.queueGoingIn.get()
# 
#                 self.campusWayRoad.queueGoingIn.put(cur_vehicle)
# 
#                 cur_vehicle = self.campusWayRoad.queueGoingIn.get()
# 
#             # enter garage
#             if (self.step % 4 == 0):  # every ~4 mins
#                 print("enter garage")
#                 self.southGarage.vehicleEnterGarage(cur_vehicle)
# 
#                 cur_vehicle = self.southGarage.queueGoingIn.get()
#                 self.southGarage.findParkingSpot(cur_vehicle)
# 
#                 # need to record spenttime for each vehicle's agent in the set
# 
#             # checking when is time to leave
#             for agent in self.school.agent_list:
#                 print("time to leave?")
#                 if (agent.stay_hours * 60 == self.step):
#                     # move to lot
#                     # need to record starttime for each vehicle's agent in the set
# 
#                     self.school.move_to_lot(agent)  # need to make this method
#                     self.school.agent_list.remove(agent)
# 
#             # check if all agents at the car yet
#             for spot in self.southGarage.spotList:
#                 print("all agents")
#                 if (spot.vehicleOccupied.num_of_agents == len(
#                         spot.vehicleOccupied.agents)):
#                     # need to record leaving time
#                     # ready to move out
#                     self.southGarage.vehicleLeavingSpot(spot)
# 
#             # leaving garage
#             print("leave garage")
#             cur_vehicle = self.southGarage.vehicleLeavingGarage()
#             if cur_vehicle is None:
#                 continue
# 
#             # enter road
#             print("enter road")
#             self.campusWayRoad.queueGoingOut.put(cur_vehicle)
# 
#             # leaving road
#             print("leave road")
#             cur_vehicle = self.campusWayRoad.queueGoingOut.get()
# 
#             # enter gate
#             print("enter gate")
#             self.gate.queueGoingOut.put(cur_vehicle)

            # need to record spenttime for each vehicle's agent in the set
            if self.step is 1:
                agent = Agent.Agent()
                print(agent)
                vehicle = Vehicle.Vehicle()
                vehicle.add_agent(agent)
                
                self.southGarage.vehicleEnterSpot(self.southGarage.spotDict["666"], vehicle)
                
                
                
            
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
