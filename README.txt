#==============================================================================
# README
#
# June 5, 2019
# Simulation of the UW Bothell's Parking
#
#==============================================================================

#==============================================================================
# Downloading the code:
#
#   git clone https://github.com/ajdeehr/EtM_ParkingSim/tree/master
#
#==============================================================================


#==============================================================================
# Execution Steps:
#
#   1. Navigate to the root directory of the program.
#   2. Have your terminal open in that directory.
#   3. (Optional) Modify the simulation variables (Explained bellow)
#   4. run the model:
#           python3 Model.py
#
#==============================================================================


#==============================================================================
# Changing Model Variables:
#
#   1. The data that the model is basing itself on can be changed by changing 
#       the constants in the Constants.py file which have the "DATA_" prefix
#
#   2. All the other simulation constants (Flow rate, len of time steps, etc.)
#       can be also modified in the Constants.py file.
#
#   3. The output path for the visualization data, and the input path for 
#       the data can be modified in the Constants.py file (Platform independent)
#
#==============================================================================


#==============================================================================
# Files and Directories:
#
#   1. "data" directory includes all the input data we used through simulation.
#
#   2. "test" directory includes all the unit testing we have done for the code.
#
#   3. "visualization" directory includes all the graphs and figures we created.
#
#   4. "Simulation_Report.pdf" file is the report which analyzes the simulation.
#
#   5. All the other files are the source code of the program:
#
#       * Agent.py > represents a person (Student, Teacher, etc.)
#       * Constants.py > all the simulation variables and constants.
#       * Data.py > the functions which are used to parse the data.
#       * Garage.py > Represents a garage full of parking spots (Different types)
#       * Gate.py > Represents an exit/entrance gate which generates the cars.
#       * Model.py > Out main model which includes the simulation and main()
#       * Road.py > Represents a road between garage(s) and the gate.
#       * School.py > Represents where the students go after parking their cars.
#       * Visualize.py > Inlcudes all the visualization code used to create plots.
#       * Vehicle.py > Represents a vehicle and it is populated with 
#                      One or more passengers. 
#
#==============================================================================



