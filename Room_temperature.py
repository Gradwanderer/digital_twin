# Import libraries



# set up variables

le = 30
wi = 20
hi = 5
floormeter = le * wi
floorcubic = floormeter * hi

def calc_room_temp(floorcubic, warmth, cool, temp):
    room_energy = floorcubic * temp
    room_energy_new = room_energy + warmth - cool
    return room_energy_new


