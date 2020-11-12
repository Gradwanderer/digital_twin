# Import libraries
import numpy as np

#todo: make clases to use different settings and different machines

# set up variables
random_crash = 0.0000001

def machine_run(lifetime, last_repair, wear_old, wl, last_period, random_crash, days_per_year, repair, replaced):

    # watt calculation to cool down
    min_watt = 100
    normal_watt = 200
    steepness_watt = 100  # -> 1100 w max at 150% usage

    # wear calculation
    hours_per_year = days_per_year * 24
    normal_wear = 1 / hours_per_year
    low_wear = normal_wear / 10
    steepness_wear = 5 #  -> 0.003 more wear max 3x more wear per hour

    # machine crash
    crash = 0
    if ((np.random.uniform(0,1) - random_crash) <= 0): crash = 1  #  random failure
    #print(crash)
    # uptime
    times = [lifetime, last_repair]
    times[:] = [(number + 1) for number in times]  # adding 1h to time
    if (repair == 1): times[1] == 0  # check for repair
    if (replaced == 1): times[0] == 0  # check for replacement

    # workload sampling, capped at 150%
    # here could occure a mistake if long time at 150% with many work to do
    workload = wl + last_period + np.random.uniform(-0.05, 0.05) + np.random.normal(0, 0.009)
    next_period = 0
    if (workload > 1.5): # workload cap at 150%
        next_period = workload - 1.5  # work for the next period -> longer periods at 150 if maxed out
        workload = 1.5

    # calculating 3 states low - normal - max
    if (workload < 0.7): # low workload
        watt = min_watt
        wear = wear_old + low_wear
        if (wear >= 1): crash = 1
        print(0)
        return (*times, watt, wear, workload, next_period, crash)

    elif (workload > 1): # max workload -> exp calculation
        watt = normal_watt + (steepness_watt ** workload) - steepness_watt
        wear = wear_old + normal_wear + ((steepness_wear ** workload - 1)) / 50000
        if (wear >= 1): crash = 1
        print(1, wear)
        return (*times, watt, wear, workload, next_period, crash)

    else: # best usage -> linear calculation
        watt = 25 + (normal_watt - min_watt) * workload
        wear = wear_old + (normal_wear - low_wear) * workload
        if (wear >= 1): crash = 1
        print(2, wear)
        return (*times, watt, wear, workload, next_period, crash)

    return



# testing
# (lifetime, last_repair, wear_old, wl, last_period, random_crash, days_per_year, repair, replaced)

for i in range(10):
    one_run = machine_run(1, 2, 0, 1, 0, random_crash, 360, 0, 0)
    print(one_run)
