# Import libraries



# set up variables
days_per_year = 360
longest_day_hours = 16 * 60
shortest_day_hours = 8 * 60
offset = 10  # if the shortest day shouldn't be the first day
high_intensity = 1
low_intensity = 0.8

# calculating sun movement

def sunmove_day(d, ld, sd, hi, li, o, today):
    """
    Calculates the max ammount of hour the sun could shine and the intensity of the sun. The decrease or increase for
    both is linear. Also the longest day is always the 1/2 the days away from the shortest day. Therefore use only
    even numbers for d. Calculating the sunrise and sunset based on the 1/2 hours of sunshin substracted or added to 12.
    All calculation are based on a 24h circle.
    :param d: days per year
    :param ld: hours of the longest day of the year
    :param sd: hours of the shortest day of the year
    :param hi: highest intensity of the sun of the year
    :param li: lowestst intensity of the sun of the year
    :param o: offset of the shortest day if it shouldn't be the first one
    :param today: day one would like to calculate
    :return: sun intensity, sunrise and sunset of choosen day
    """

    longest_day = o + d / 2
    diff_time = abs(ld - sd) / (d / 2)
    diff_intens = abs(hi - li) / (d / 2)
    if ((today < longest_day) & (today > o)) or (today < o):  # winter to summer
        sun_hours = (abs(today - o) * diff_time) + sd
        sun_intens = (abs(today - o) * diff_intens) + li
        sunrise = 12 - (sun_hours / 120)  # 120 to get minutes to hours * 2
        sunset = 12 + (sun_hours / 120)
        return (sun_intens, sunrise, sunset)

    elif (today == o):
        sunrise = 12 - (sd / 120)
        sunset = 12 + (sd/ 120)
        return (li, sunrise, sunset)

    else:  # summer to winter
        sun_hours = ld - (abs(today - longest_day) * diff_time)
        sun_intens = hi - (abs(today - longest_day) * diff_intens)
        sunrise = 12 - (sun_hours / 120)
        sunset = 12 + (sun_hours / 120)
        return (sun_intens, sunrise, sunset)

    return

def sunmove_hour(itl, ith, sr, ss, hd):
    """
    Calculate the intensity of the sun. Full intensity at the middle between sunrise and sunset
    :param itl: low intensity of the day
    :param ith: high intensity of the day (noon)
    :param sr: sunrise time for 24 hour circle
    :param ss: sunset time for 24 hour circle
    :param hd: the time you want to calculate (for 11:30 o'clock take 11.5)
    :return:
    """

    hoursofday = ss - sr
    halfday = ss + (hoursofday / 2)
    intensdiff = ith - itl
    intenschange = intensdiff / (hoursofday / 2)

    if (hd < sr) or (hd > ss):  # nighttime
        return 0

    else:  # daytime
        if (hd < halfday):  # first hours of day
            hour_intense = ((hd - sr) * intenschange) + itl
            return hour_intense

        else:  # last hours of day
            hour_intense = ((ss - hd) * intenschange) + itl
            return hour_intense

    return


# testing
today = 250
sunday = sunmove_day(days_per_year,
              longest_day_hours, shortest_day_hours,
              high_intensity, low_intensity,
              offset, today)
print(sunday)
sunhour = sunmove_hour(0.6, *sunday, 11)
print(sunhour)
