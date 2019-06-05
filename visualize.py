import numpy as N
import matplotlib
import matplotlib.pyplot as plt

import Garage
import Road
import Data
import Constants as C

import importlib

importlib.reload(C)

from datetime import timedelta, datetime

t = datetime(2019, 6, 3, hour=7)


def plot_credits(modelobj):
    # sigma = [4.0, 4.5, 5.0, 5.5, 6.0]
    sigma = [3, 4, 5, 6]
      
    credits_sa = []
    for i in range(len(sigma)):

        credits = []
        for agent in range(100000):
            credits.append(N.floor(sigma[i] * N.random.randn() + 15) )
        
        credits_sa.append(credits)
        # modelobj.gate.agents_list.clear()
        
    plt.figure(2)
    for i in range(len(credits_sa)):
        label = "Sigma of {}".format(sigma[i])
        plt.hist(credits_sa[i], label=label,histtype='step', bins = range(30), range=(0,31))
    # plt.hist(credits_sa, histtype='step')
    plt.legend()
    plt.xlabel("Number of Credits taken")
    plt.ylabel("Frequency")
    plt.title("Sensitivity Analysis of Different Sigma Values on Credit Generation")
    plt.savefig("EtM_PS_Credits_SA.png", dpi=300)
    plt.show()
    

        
def plot_util(modelobj, sigmain = 5):
    
    util_per = modelobj.south_garage.utilization / modelobj.south_garage.num_spot
    plt.figure(4)
    plt.plot(range(int(1440 / C.TIME_STEP)), util_per)
    plt.title("Utilization of the Parking Garage at Each Time at Sigma {}".format(sigmain))
    plt.xlabel("Time")
    plt.ylabel("Percent of Utilization")
    plt.savefig("EtM_PS_Util_at_S{}.png".format(sigmain), dpi=300)
    plt.show()
    
    # times = N.arange((int(1440 / C.TIME_STEP)))
    # util = modelobj.school.agents_arrived_at_t(times)
    # plt.figure(5)
    # plt.plot(range(int(1440 / C.TIME_STEP)), util)
    # plt.title("Number of Students Arriving at Each Time at Sigma {}".format(sigma))
    # plt.xlabel("Time (Hours)")
    # plt.ylabel("Number of Students Arriving")
    # plt.savefig("EtM_PS_Arrivals_at_S{}.png".format(sigma), dpi=300)
    # plt.show()
    # 
    # 
    # times = N.arange((int(1440 / C.TIME_STEP)))
    # leaving = modelobj.gate.num_leaving(times)
    # plt.figure(8)
    # plt.plot(range(int(1440 / C.TIME_STEP)), leaving)
    # plt.title("Number of Students Leaving at Each Time at Sigma {}".format(sigmain))
    # plt.xlabel("Time (Hours)")
    # plt.ylabel("Number of Students Leaving")
    # plt.savefig("EtM_PS_Leaving_at_S{}.png".format(sigmain), dpi=300)
    # plt.show()

    
    
    
    
    # times = []
    # plt.figure(4)
    # for agent in modelobj.gate.agents_list:
    #     agent.
    #     
        
    
def plot_totals(modelobj):
    plt.figure(3)
    days = ['Mon','Tue','Wed','Thu','Fri']
    time = (N.arange(0,len(Data.table)) * C.TIME_STEP) / 60
    
    for i in range(5):
        plt.plot(time[:], Data.table[:,i], label=days[i])
    plt.legend()
    plt.title("Number of Students Enrolled In A Class at Each Time")
    plt.xlabel("Time (Hours)")
    plt.ylabel("Number of Students enrolled in a Class")
    plt.savefig("EtM_PS_Stud_Enrolled.png", dpi=300)
    plt.show()
    
    plt.figure(7)
    times = (N.arange(0,96)) * 15
    agents = modelobj.gate.num_agents_per_t_list
    vehicles = modelobj.gate.num_vehicle_per_t_list
    plt.plot(times, agents[:, 0])
    plt.plot(times, vehicles[:, 0])
    plt.title("Total Vehicles and Agents Generated in the Simulation")
    plt.xlabel("Time")
    plt.ylabel("Total Vehicles and Agents Generated")
    plt.savefig("EtM_PS_Totals.png", dpi=300)
    # Updated, fix from code

def plot_times(modelobj):
    times = (N.arange(0,len(Data.table)) * C.TIME_STEP) / 60
    time = N.arange((int(1440 / C.TIME_STEP) ))
    
    avg_time = modelobj.school.avg_time_to_arrive(time)
    plt.figure(6)
    plt.plot(times, avg_time)
    plt.title("Average Time to Arrival at Each Time")
    plt.xlabel("Time")
    plt.ylabel("Average Time to Arrival")
    plt.savefig("EtM_PS_Avg_Arrival.png", dpi=300)

    
    

def plot_campus(modelobj, use_obj=None):
    global t
    
    garage_size = int((N.ceil(modelobj.south_garage.num_spot / modelobj.south_garage.garage_width)) * modelobj.south_garage.garage_width)
    
    cmap_garage = ['b', 'g', 'c','y', 'r', 'k', '0.0']
    cmap_road = ['y', 'c', 'b', 'g', 'r', 'k', '0.8']

    if use_obj == None:
        fig = plt.figure(figsize=(6,6))
        axs = []
        imgs = []

        l_southG = garage_size / modelobj.south_garage.garage_width
        w_southG = modelobj.south_garage.garage_width
        
        l_road = modelobj.campus_way_road.length
        w_road = modelobj.campus_way_road.width
        
        tot_horiz = float(w_southG + 6)
        tot_vert = float(l_southG + l_road + 2)
        
        axs.append(
            fig.add_axes((0.05, (l_road + 1)/tot_vert, \
                        w_southG/tot_horiz, l_southG/tot_vert), frameon=False))
                        
                        
        axs.append(fig.add_axes((.0, .0, w_road/tot_horiz, l_road/tot_vert), frameon=False))
        
        axs.append(fig.add_axes((.7, .93, .2, .1),frameon=False))

    else:
        fig = use_obj[0]
        axs = use_obj[1]
        imgs = use_obj[2]

    data = N.ones((garage_size, 3), dtype='f') * float(cmap_garage[-1])
    
    convert = matplotlib.colors.ColorConverter()


    
    if len(modelobj.south_garage.spot_dict) != 0:
        it = 0
        
        for dict_type in C.VEHICLE_TYPES.keys():
            print(dict_type)
            for spot in modelobj.south_garage.spot_dict[C.VEHICLE_TYPES[dict_type]].values():
                print(spot)
                temp = N.array(convert.to_rgb(cmap_garage[spot.get_parking_type()]))
                data[it, :] = temp[:]
                it = it + 1
    else:
        pass

    ln, wd = int(garage_size / modelobj.south_garage.garage_width), int(modelobj.south_garage.garage_width)
    data = N.reshape(data, (ln, wd, 3))

    if use_obj == None:
        ax = axs[0]
        imgs.append(ax.imshow(data, interpolation='none', \
                              extent=[0, wd, 0, ln], zorder=0))

        ax.axis('off')

    else:
        img = imgs[0]
        img.set_data(data)
        plt.draw()
        
    data_r = N.ones((modelobj.campus_way_road.length,modelobj.campus_way_road.width, 3), dtype='f') * float(cmap_road[-1])
    
    if use_obj == None:
        ax = axs[1]
        imgs.append(axs[1].imshow(data_r, interpolation='none', \
                              extent=[0, w_southG, 0, l_southG],aspect="auto", zorder=0))

        ax.axis('off')

    else:
        img = imgs[1]
        img.set_data(data_r)
        plt.draw()
        
    if use_obj == None:
        ax = axs[2]
        imgs.append( axs[2].text( .005, .5, "t = " + str(t + timedelta(minutes=(modelobj.step))) + " mins"))
        ax.axis('off')
    else:
        ax = axs[2]
        imgs[2].remove()
        imgs[2] = axs[2].text( .005, .5, "t = " + str(t + timedelta(minutes=(modelobj.step))) + " mins")
        ax.axis('off')
        plt.draw()
        
        

    return fig, axs, imgs
