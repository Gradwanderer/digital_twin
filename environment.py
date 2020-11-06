# Import libraries



# set up variables
days_per_year= 360
longest_day_hours = 16 * 60
shortest_day_hours = 8 * 60
offset = 10 # if the longest day shouldn't be the first day
high_intensity = 1
low_intensity = 0.5

# calculating sun movement

def sunmove(d, ld, sd, hi, li, o, today):
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
    return (sun_hours, sun_intens)

today = 250

print(sunmove(days_per_year,
              longest_day_hours, shortest_day_hours,
              high_intensity, low_intensity,
              offset, today))

