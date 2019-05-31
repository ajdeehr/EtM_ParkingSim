import numpy as N
import random as R

import Agent
import Vehicle
import Road
import Garage
import Gate
import School
import Constants as C

limit = 30

class Model(object):

    def __init__(self, dt=0.25, trafficWeight=1):

        self.trafficWeight = trafficWeight

        #self.northGarage = Garage.Garage("North Garage", 300, 20, 20, 0, 1)
        self.southGarage = Garage.Garage("South Garage", 200, 10, 10, 0, 1)

        self.campusWayRoad = Road.Road(adjacentGarage=self.southGarage, adjacentGarage2=None, trafficWeight = 1)

        #self.northGarage.outsideRoad = self.campusWayRoad
        self.southGarage.outsideRoad = self.campusWayRoad

        self.numberGarage = 2

        self.gate = Gate.Gate()

        self.school = School.School()

        self.num_days = 30
        self.dt = 0.15


    def run_session(self, num_days=30):

        minute_in_a_day = 1440
        no_steps = minute_in_a_day * num_days 

        for step in range(1, no_steps+1):

            #generate vehicle and agents in vehicle
            #every 30 mins
            if (step % 30 == 0):
                gate.vehicle_gen(400) #400 is just place holder

            #need to record starttime for each vehicle's agent in the set


            #added to park spot

            #enter road
            if (step % 2 == 0): #every ~2 mins
                cur_vehicle = gate.queueGoingIn.get()

                campusWayRoad.queueGoingIn.put(cur_vehicle)

                cur_vehicle = campusWayRoad.queueGoingIn.get()

            #enter garage
            if (step % 4 == 0): #every ~4 mins 
                southGarage.vehicleEnterGarage(cur_vehicle)

                cur_vehicle = southGarage.queueGoingIn.get()
                southGarage.findParkingSpot(cur_vehicle)

                #need to record spenttime for each vehicle's agent in the set

            #checking when is time to leave
            for agent in school.agent_list:
                
                if (agent.stay_hours * 60 == step):
                    #move to lot
                    #need to record starttime for each vehicle's agent in the set
                    
                    school.move_to_lot(agent) #need to make this method
                    school.agent_list.remove(agent)

            #check if all agents at the car yet
            for spot in southGarage.spotList:
                
                if (spot.vehicleOccupied.num_of_agents == len(spot.vehicleOccupied.agents)):
                    #need to record leaving time
                    #ready to move out
                    southGarage.vehicleLeavingSpot(spot)


            #leaving garage
            cur_vehicle = southGarage.vehicleLeavingGarage()

            #enter road
            campusWayRoad.queueGoingOut.put(cur_vehicle)
            
            #leaving road
            cur_vehicle = campusWayRoad.queueGoingOut.get()

            #enter gate
            gate.queueGoingOut.put(cur_vehicle)
            
            #need to record spenttime for each vehicle's agent in the set




def main():
    model = Model()
    
main()