# Import libraries



# set up variables
days_per_year= 360
longest_day_hours = 16 * 60
shortest_day_hours = 8 * 60
offset = 10 # if the shortest day shouldn't be the first day
high_intensity = 1
low_intensity = 0.5

# calculating sun movement

def sunmove(d, ld, sd, hi, li, o, today):
    """
    Calculates the max ammount of hour the sun could shine and the intensity of the sun. The decrease or increase for
    both is linear. Also the longest day is always the 1/2 the days away from the shortest day. Therefore use only
    even numbers for d.
    :param d: days per year
    :param ld: hours of the longest day of the year
    :param sd: hours of the shortest day of the year
    :param hi: highest intensity of the sun of the year
    :param li: lowestst intensity of the sun of the year
    :param o: offset of the shortest day if it shouldn't be the first one
    :param today: day one would like to calculate
    :return: hours of the day and sun intensity
    """

    longest_day = o + d / 2
    diff_time = abs(ld - sd) / (d / 2)
    diff_intens = abs(hi - li) / (d / 2)
    if (today < longest_day) & (today > o):  # winter to summer
        sun_hours = (abs(today - o) * diff_time) + sd
        sun_intens = (abs(today - o) * diff_intens) + li
        return (sun_hours, sun_intens)
    elif (today == o):
        return (sd, li)
    else:  # summer to winter
        if (today < o):  #first days of year
            sun_hours = (abs(today - o) * diff_time) + sd
            sun_intens = (abs(today - o) * diff_intens) + li
            return (sun_hours, sun_intens)
        else:  # 2. half of year
            sun_hours = ld - (abs(today - longest_day) * diff_time)
            sun_intens = hi - (abs(today - longest_day) * diff_intens)
            return (sun_hours, sun_intens)
    return

today = 250

print(sunmove(days_per_year,
              longest_day_hours, shortest_day_hours,
              high_intensity, low_intensity,
              offset, today))

