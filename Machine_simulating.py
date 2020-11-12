# Import libraries
import numpy as np

# set up variables


def machine_run():


    min_temp = 25
    normal_temp = 50
    steepness = 25  # results in 175 max temp


    times = [lifetime, last_repair]
    times[:] = [(number + 1) for number in times]  # adding 1h to time
    if (repair == 1): times[1] == 0  # check for repair
    if (replaced == 1): times[0] == 0  # check for replacement

    workload = wl + np.random.uniform(-0.05, 0.05) + np.random.normal(0, 0.009)
    if (workload < 0.7): # low workload
        temp = min_temp
        wear

    elif (workload > 1): # high workload
        temp = 50 + (steepness ** workload)  # exponential rise of temp
        wear


    else: # best usage
        temp = 25 + (normal_temp - min_temp) * workload
        wear




    return
