# Import libraries
import numpy as np

# set up variables


def machine_run():

    # temp calculation
    min_temp = 25
    normal_temp = 50
    steepness_temp = 25  # -> 175 max temp
    # wear calculation
    hours_per_year = days_per_year * 24
    normal_wear = 1 / hours_per_year
    low_wear = normal_wear / 10
    steepness_wear = 5 #  -> 0.011 more wear max


    times = [lifetime, last_repair]
    times[:] = [(number + 1) for number in times]  # adding 1h to time
    if (repair == 1): times[1] == 0  # check for repair
    if (replaced == 1): times[0] == 0  # check for replacement

    workload = wl + np.random.uniform(-0.05, 0.05) + np.random.normal(0, 0.009)
      # workload cap at 150%
    if (workload < 0.7): # low workload
        temp = min_temp
        wear = wear_old + low_wear

    elif (workload > 1): # high workload -> exp calculation
        temp = normal_temp + (steepness_temp ** workload) - steepness_temp
        wear = normal_wear + (steepness_wear ** workload) - steepness_wear


    else: # best usage -> linear calculation
        temp = 25 + (normal_temp - min_temp) * workload
        wear = wear_old + (normal_wear - low_wear) * workload




    return
