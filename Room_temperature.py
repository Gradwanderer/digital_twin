# Import libraries



# set up variables

le = 30  # length
wi = 20  # width
hi = 5  # height
ma = 0  # room space blocked (cubic)

def calc_room_temp(le, wi, hi, ma,  warmth, cool, temp):
    """
    Calculating the temperature of a room given the diameter.
    :param le: length of the room
    :param wi: width of the room
    :param hi: height of the room
    :param ma: room space blocked for example machines
    :param warmth: energy (temperature * cubic) to heat the room
    :param cool: energy (temperature * cubic) to cool the room
    :param temp: measured temperature of the room
    :return: new temperature of the room
    """

    floormeter = le * wi
    floorcubic = floormeter * hi - ma
    room_energy = floorcubic * temp
    room_energy_new = room_energy + warmth - cool

    return room_energy_new

# testing
