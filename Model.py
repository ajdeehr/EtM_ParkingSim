# -*- coding: utf-8 -*-
#==============================================================================
#                        General Documentation
"""
"""
#------------------------------------------------------------------------------
#                       Additional Documentation
# Modification History:
# - 2 Jun 2019:  Original by Dewey Nguyen, CSS458 A,
#   University of Washington Bothell.
# - Subsequent Revisions from Xavier Cheng, Adam Deehring, and Ardalan Ahanchi
#
# Notes:
# - Written for Python 3.5.2.
#==============================================================================

#---------------- Module General Import and Declarations ----------------------
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


class Model(object):
    """ The Central Object in our simulation. """

    def __init__(self, dt=0.25, trafficWeight=1):
        """ The default constructor for the Model """
        
        # self.test_agent = Agent.Agent()
        self.trafficWeight = trafficWeight

        self.gate = Gate.Gate()

        self.campus_way_road = Road.Road(2, 2, 3)

        self.south_garage = Garage.Garage("South Garage", num_spot=771,
                                         num_carpool_spot=23,
                                         num_handicapped_spot=20,
                                         num_bike_spot=12, garage_width = 31)

        self.school = School.School()

        self.num_days = 30
        self.dt = 0.15

        self.plot_figure = None
        self.plot_axis = None
        self.plot_image = None

        #Tracks utilization per time step.
        self.utilization = []

    def get_time_str(self, curr_t):
        '''A method which returns the string representation of time based 
			on curr step
			'''
        hour, min = self.get_time(curr_t)
        return str(hour) + ":" + str(min) + "\n"

    def get_time(self, curr_t):
        ''' A method which returns hour and minutes as integers '''
        hour = C.DATA_START_TIME + int(curr_t/ C.DATA_MINS_IN_HR)
        min = curr_t % C.DATA_MINS_IN_HR
        return hour, min

    def curr_stat(self):
        '''A method which returns the current statistics of the model at the 
			current time step.
		'''
        print("\n\nTimestep", self.step, 
				"**************************************", file=sys.stderr)
        print("\nTime is", self.get_time_str(self.step), "\n", 
				file=sys.stderr)
        print(self.gate, file=sys.stderr)
        print(self.campus_way_road, file=sys.stderr)
        print(self.south_garage, file=sys.stderr)
        print(self.school, file=sys.stderr)
        print("\n***************************************************\n", 
				file=sys.stderr)

    	
    def log(self, str):
        """ A method that prints a message with associated time step of when it 
        was written """
        print(str, " | ", self.step, file=sys.stderr)


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
				else:   #If not parking spots were found.
                        #Go back to the road to find parking.
                    self.campus_way_road.reenter_road(cur_vehicle, self.step)

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
            out_congestion = \
                N.random.randint(C.ROAD_FLOW_MIN, C.ROAD_FLOW_MAX)
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
            self.utilization.append(self.south_garage.utilization())

            #Plot the current data.
            self.curr_stat()

            if self.step is 0:
                 plt.ion()
                 self.plot_figure, self.plot_axis, self.plot_image = \
                     V.plot_campus(self)

            else:
                self.plot_figure, self.plot_axis, self.plot_image = \
                    V.plot_campus(self, use_obj=(self.plot_figure, 
								self.plot_axis, self.plot_image))

            #Wait for the animation.
            plt.pause(.001)


    def _run_session_grab_data(self, sigma):
        model = Model()
        model.run_session("Mon")
        print(model.gate.avg_time_to_leave(100))
        print(model.school.avg_time_to_arrive(100))


def main():
    model = Model()
    model.run_session("Mon")
    V.plot_credits(model)
    V.plot_average(model)

if __name__ is "__main__":
    main()
