
import calendar
import timeit

import n1 as n1


def leap_years_lst(n=1000000):
    leap_years = []
    for year in range(1, n+1):
        if calendar.isleap(year):
            leap_years.append(year)
    return leap_years

# generator
def leap_years_gen(n=1000000):
    for year in range(1, n+1):
        if calendar.isleap(year):
            yield year
starttime = timeit.default_timer()
print("The start time is :",starttime)
leap_years_lst()
print("The time difference is :", timeit.default_timer() - starttime)

starttime = timeit.default_timer()
print("The start time is :",starttime)
leap_years_gen()
print("The time difference is :", timeit.default_timer() - starttime)
