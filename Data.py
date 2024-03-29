# -*- coding: utf-8 -*-
# ==============================================================================
#                        General Documentation
"""
"""
# ------------------------------------------------------------------------------
#                       Additional Documentation
# Modification History:
# - 3 Jun 2019:  Original by Ardalan Ahanchi, CSS458 A,
#   University of Washington Bothell.
# - Subsequent Revisions from Xavier Cheng, Adam Deehring, and Dewey Nguyen
#
# Notes:
# - Written for Python 3.5.2.
# ==============================================================================

# ---------------- Module General Import and Declarations ----------------------
import numpy as N
import matplotlib.pyplot as plt
import sys
import Constants as C

# Read the raw table from the DATA_FILE_NAME file.
raw_table = N.genfromtxt(C.DATA_FILE_NAME, delimiter=',', dtype=int)

# Define and calculate the divider.
div = int(C.DATA_TIME_STEP / C.TIME_STEP)

# Repeat the rows for each time stamp duration, and divide by size of time step.
table = N.repeat(raw_table, div, axis=0) // div


# N.savetxt("Full_Table.csv", table, delimiter=",")

def get_num_steps():
    ''' A function to get the total number of steps '''
    return table.shape[0]


def get_rate(day, timestep):
    ''' A function which returns the rate for the given day and time step.
    day should be an integer defined in Constants file (C.DAYS) and timestep
    should be the t which we're looking for.

    Sample usage is: print( get_rate("Mon", 148) ) '''

    # Check if the day is valid.
    if day not in C.DAYS:
        print("Error: Data: get_rate: Invalid Day:", day, file=sys.stderr)
        return None

    # Check if timestep is invalid.
    if timestep >= table.shape[0]:
        print("Error: Data: get_rate: Invalid timestep: ", timestep,
              file=sys.stderr)
        return None

    # Get the current rate from the table.
    return table[timestep, C.DAYS[day]]
