import numpy as N
import queue

# Ardalan Ahanchi
# June 2, 2019

class Road(object):
    """Create a road object which holds the cars for the weight amount of time.
    """

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        '''A method to get a string representation of a class'''

        out = "Road: Dump *******************************" + "\n"
        out += "Road: Number in going in Queue == " + str(len(self.q_going_in)) + "\n"
        out += "Road: Number in going out Queue == " + str(len(self.q_going_out)) + "\n"
        out += "******************************************"
        return out

    def __init__(self, lanesin = 1, lanesout = 1, min_t_to_pass = 3):
        """ Default constructor, it holds lanes_in and lanes_out so the calling
        object can keep track of how many times it needs to call enter, arrive,
        leave, or exit. Additionally, min_t_to_pass keeps track of the minimum
        timesteps which are required to pass the road (Related to length) """

        self.q_going_in = []      #Used lists instead of queue to allow peeking.
        self.q_going_out = []

        self.lanes_in = lanesin   #Track this for external objects.
        self.lanes_out = lanesout

        self.min_t_to_pass = min_t_to_pass

    def enter_road(self, vehicle, curr_t):
        """ A method for adding the vehicle to the road. It specifically is
        called when the vehicle arrives in the road and before reaching school"""
        self.q_going_in.append((vehicle, curr_t))

    def arrive_garage(self, curr_t):
        """ A method which returns the vehicle which has arrived to garage. If
        No vehicle is ready to arrive (To Garage), it just returns None """

        #If there are no vehicles in the road, return None.
        if len(self.q_going_in) == 0:
            return None

        #If the time passed since enterance is less than min_t_to_pass return None.
        elif curr_t - self.q_going_in[0][1] >= self.min_t_to_pass:
            return None

        #If vehicle is available to exit to the parking lot, remove and return it.
        else:
            return (self.q_going_in.pop(0))[0]

    def leave_garage(self, vehicle, curr_t):
        """A method which is called when the vehicle is done parking and is trying
        to enter the road in order to leave"""
        self.q_going_out.append((vehicle, curr_t))

    def exit_road(self, curr_t):
        """ A method which returns the vehicle which has arrived to gate. If
        No vehicle is ready to exit (To Gate), it just returns None """

        #If there are no vehicles in the road, return None.
        if len(self.q_going_out) == 0:
            return None

        #If the time passed since leaving garage is less than min_t_to_pass return None.
        elif curr_t - self.q_going_out[0][1] >= self.min_t_to_pass:
            return None

        #If vehicle is available to exit to the gate, remove and return it.
        else:
            return (self.q_going_out.pop(0))[0]
