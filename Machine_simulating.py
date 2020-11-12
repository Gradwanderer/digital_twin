# Import libraries
import numpy as np

# set up variables
random_crash = 0.0000001

def machine_run():

    # watt calculation to cool down
    min_watt = 100
    normal_watt = 200
    steepness_watt = 100  # -> 1000 w max at 150% usage
    # wear calculation
    hours_per_year = days_per_year * 24
    normal_wear = 1 / hours_per_year
    low_wear = normal_wear / 10
    steepness_wear = 5 #  -> 0.011 more wear max

    crash = 0
    if ((np.random.uniform(0,1) - random_crash) <= 0): crash = 1  #  random failure

    times = [lifetime, last_repair]
    times[:] = [(number + 1) for number in times]  # adding 1h to time
    if (repair == 1): times[1] == 0  # check for repair
    if (replaced == 1): times[0] == 0  # check for replacement

    workload = wl + np.random.uniform(-0.05, 0.05) + np.random.normal(0, 0.009)
    if (workload > 1.5): # workload cap at 150%
        next_period = workload - 1.5  # work for the next period -> longer periods at 150 if maxed out
        workload = 1.5


    if (workload < 0.7): # low workload
        watt = min_watt
        wear = wear_old + low_wear
        if (wear >= 1): crash = 1

    elif (workload > 1): # high workload -> exp calculation
        watt = normal_watt + (steepness_watt ** workload) - steepness_watt
        wear = wear_old + normal_wear + (steepness_wear ** workload) - steepness_wear
        if (wear >= 1): crash = 1

    else: # best usage -> linear calculation
        watt = 25 + (normal_watt - min_watt) * workload
        wear = wear_old + (normal_wear - low_wear) * workload
        if (wear >= 1): crash = 1



    return



# testing

