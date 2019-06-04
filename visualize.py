import numpy as N
import matplotlib
import matplotlib.pyplot as plt

import Garage
import Road

from datetime import timedelta, datetime

t = datetime(2019, 6, 3, hour=7)

def plot_garage(aGarage):
    garage_size = aGarage.number_of_spot + aGarage.blank_spots
    # data = N.zeros((N.sqrt(garage_size),N.sqrt(garage_size),3), dtype='f')
    data = N.zeros((garage_size, 3), dtype='f')
    cmap = ['y', 'c', 'b', 'g', 'r', 'k']
    convert = matplotlib.colors.ColorConverter()

    if len(aGarage.spot_dict) != 0:
        for i in range(1, garage_size):
            spot = aGarage.spot_dict[str(i)]
            temp = N.array(convert.to_rgb(cmap(spot.get_parking_type())))
            data[i - 1, :] = temp[:]
    else:
        pass

    data = N.reshape(data, (N.sqrt(garage_size), N.sqrt(garage_size), 3))

    fig, ax = plt.subplot(1, 1)

    ax.imshow(data, interpolation='none', \
              extent=[0, N.sqrt(garage_size), 0, N.sqrt(garage_size)], zorder=0)
    ax.axis('off')
    
    plt.show()

    return fig, ax


def plot_campus(modelobj, use_obj=None):
    global t
    # fig, axs, imgs = None, None, None
    garage_size = int(N.power(N.ceil(N.sqrt(modelobj.southGarage.number_of_spot)), 2))
    
    cmap_spots = ['y', 'c', 'b', 'g', 'r', 'k']
    cmap_garage = ['y', 'c', 'b', 'g', 'r', 'k', '0.0']
    cmap_road = ['y', 'c', 'b', 'g', 'r', 'k', '0.8']
    # garage_size = modelobj.southGarage.number_of_spot

    # print(modelobj.southGarage.spot_dict)
    if use_obj == None:
        fig = plt.figure(figsize=(6,6))
        axs = []
        imgs = []

        l_southG = N.sqrt(garage_size)
        w_southG = N.sqrt(garage_size)
        
        l_road = modelobj.campusWayRoad.length
        w_road = modelobj.campusWayRoad.width
        
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


    if len(modelobj.southGarage.spot_dict) != 0:
        for i in range(1, garage_size):
            spot = modelobj.southGarage.spot_dict[str(i)]
            temp = N.array(convert.to_rgb(cmap_garage[spot.get_parking_type()]))
            data[i - 1, :] = temp[:]
    else:
        pass

    ln, wd = int(N.sqrt(garage_size)), int(N.sqrt(garage_size))
    data = N.reshape(data, (ln, wd, 3))

    if use_obj == None:
        ax = axs[0]
        imgs.append(ax.imshow(data, interpolation='none', \
                              extent=[0, int(N.sqrt(garage_size)), 0,
                                     int(N.sqrt(garage_size))], zorder=0))

        ax.axis('off')

    else:
        img = imgs[0]
        img.set_data(data)
        plt.draw()
        
    data_r = N.ones((modelobj.campusWayRoad.length,modelobj.campusWayRoad.width, 3), dtype='f') * float(cmap_road[-1])
    
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
