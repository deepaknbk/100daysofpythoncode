import research

def main():

    print('Weather Data Analysis start')
    research.init()
    #To Do: Read CSV file

    days=research.get_hottest_days()
    # Get top 5 hottest days
    for idx,day in enumerate(days[:5]):
        print(f'{idx+1}. {day.date} is hottest day with {day.actual_max_temp} F')

    print()
    days=research.get_coldest_days()
    for idx,day in enumerate(days[:5]):
        print(f'{idx+1}. {day.date} is coldest day with {day.actual_max_temp} F')
    #Get top 5 clod days
    pass

    #get_wet_days()
    #Get top 5 wet days




if __name__ == '__main__':
    main()