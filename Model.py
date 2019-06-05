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

    def get_time_str(self):
        '''A method which returns the string representation of time based on curr step'''
        return str(C.DATA_START_TIME + int(self.step / C.DATA_TIME_STEP)) \
                    + ":" + str(self.step % C.DATA_TIME_STEP) + "\n"

    def curr_stat(self):
        '''A method which returns the current statistics of the model at the current time step.'''
        print("\n\nTimestep", self.step, "**************************************", file=sys.stderr)
        print("\nTime is", self.get_time_str(), file=sys.stderr)
        print(self.gate, file=sys.stderr)
        print(self.campus_way_road, file=sys.stderr)
        print(self.south_garage, file=sys.stderr)
        print(self.school, file=sys.stderr)
        print("\n***************************************************\n", file=sys.stderr)

    def run_session(self, day):

        for self.step in range(Data.get_num_steps()):
            # generate vehicle and agents in vehicle
            # every min
            self.gate.estimate_vehicles(Data.get_rate(day, self.step))
            self.gate.vehicle_gen(self.step)

            #Generate a congestion multiplier randomly within the range.
            in_congestion = N.random.randint(C.ROAD_FLOW_MIN, C.ROAD_FLOW_MAX)
            for i in range( in_congestion * self.campus_way_road.lanes_in):
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
                    self.campus_way_road.enter_road(cur_vehicle, self.step)

            # checking when is time to leave
            leaving_agent = self.school.leave(self.step)
            while leaving_agent != None:
                self.south_garage.find_car(leaving_agent)
                leaving_agent = self.school.leave(self.step)

            # Go though all the lanes, and leave garage.
            #Generate a congestion multiplier randomly within the range.
            out_congestion = N.random.randint(C.ROAD_FLOW_MIN, C.ROAD_FLOW_MAX)
            for i in range(out_congestion * self.campus_way_road.lanes_out):
                # leaving garage
                cur_vehicle = self.south_garage.leave_garage()
                if cur_vehicle != None :
                    # enter road
                    self.campus_way_road.leave_garage(cur_vehicle, self.step)

                # leaving road
                cur_vehicle = self.campus_way_road.exit_road(self.step)
                if cur_vehicle is not None:
                    # enter gate
                    self.gate.enter_gate(cur_vehicle)

            #Remove the vehicle from the gate and get avg.
            self.gate.exit_gate(self.step)

            self.curr_stat()


    def run_session_plot_out_graphs(self, sigma):
        V.plot_credits(self)
        V.plot_util(self, sigma)
        
    def run_session_plot_out(self, day):

        for self.step in range(Data.get_num_steps()):
            
            # generate vehicle and agents in vehicle
            # every min
            self.gate.estimate_vehicles(Data.get_rate(day, self.step))
            self.gate.vehicle_gen(self.step)

            #Generate a congestion multiplier randomly within the range.
            in_congestion = N.random.randint(C.ROAD_FLOW_MIN, C.ROAD_FLOW_MAX)
            for i in range( in_congestion * self.campus_way_road.lanes_in):
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
                    self.campus_way_road.enter_road(cur_vehicle, self.step)

            # checking when is time to leave
            leaving_agent = self.school.leave(self.step)
            while leaving_agent != None:
                self.south_garage.find_car(leaving_agent)
                leaving_agent = self.school.leave(self.step)

            # Go though all the lanes, and leave garage.
            #Generate a congestion multiplier randomly within the range.
            out_congestion = N.random.randint(C.ROAD_FLOW_MIN, C.ROAD_FLOW_MAX)
            for i in range(out_congestion * self.campus_way_road.lanes_out):
                # leaving garage
                cur_vehicle = self.south_garage.leave_garage()
                if cur_vehicle != None :
                    # enter road
                    self.campus_way_road.leave_garage(cur_vehicle, self.step)

                # leaving road
                cur_vehicle = self.campus_way_road.exit_road(self.step)
                if cur_vehicle is not None:
                    # enter gate
                    self.gate.enter_gate(cur_vehicle)

            #Remove the vehicle from the gate and get avg.
            avg_leaving, num_leaving = self.gate.exit_gate(self.step)

            self.curr_stat()
            if self.step is 0:
                plt.ion()
                self.plot_figure, self.plot_axis, self.plot_image = \
                    V.plot_campus(self)
                # self.plot_figure, self.plot_axis = V.plot_garage(self)
                # plt.show()

            elif self.step is 200:
                # pass
                self.plot_figure, self.plot_axis, self.plot_image = \
                    V.plot_campus(self, use_obj=(self.plot_figure, self.plot_axis, self.plot_image))
                
            # plt.pause(.001)


def main1():
    # model = Model()
    sigma = [3, 4, 5, 6]
    
    # garage_diff = [-200, -100, 0, 100, 200]
    garage_diff = [0]
    for i in range(len(sigma)):
        model = Model(garage_diff=garage_diff[0], sigma=sigma[i])
        model.run_session_plot_out("Mon")
        model.run_session_plot_out_graphs(sigma[i])

def main2():
    model = Model()
    model.run_session("Mon")
    print(model.gate.avg_time_to_leave(100))
    print(model.school.avg_time_to_arrive(100))
    #model.run_session_plot_out(num_days=30)


main1()
main2()
