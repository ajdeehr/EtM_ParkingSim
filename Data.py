
import numpy as N
import matplotlib.pyplot as plt
import Constants as C

# data from Parking Utilization Memo 002, page 7
#starting at 10 am to 3 pm, last number is 7pm
demandbyhourNorth = [413, 402, 416, 393, 384, 369, 169]
demandbyhourSouth = [691, 731, 748, 706, 690, 607, 309]
demandbyhourSurface = [589, 714, 727, 697, 689, 591, 244]

# data from time table. 2-d array 1 to 96 line, 15 min interval, mon-friday
table = N.genfromtxt('2DonCampus.csv', delimiter=',')
table = table.astype(int)



def get_morning_hour_demand(lst, index):
    low = lst[index] - C.PLUS_MINUS # 30 for rn

    #range_of_demand_hour is a array of +-30 range of demandbyhour[index]
    range_of_demand_hour = N.arange(C.PLUS_MINUS * 2 + 1) + low

    return range_of_demand_hour[N.random.randint(0, C.PLUS_MINUS * 2 + 1)]
