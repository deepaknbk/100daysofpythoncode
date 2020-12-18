cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    for key,value in cars.items():
        if key=='Jeep':
            #print(value)
            # jeep=[]
            # for model in value:
            #     #print(model)
            #     jeep.append(model)
            # #print(jeep)
            return ', '.join(value)


def get_first_model_each_manufacturer():
    """return a list of matching models (original ordering)"""
    first_model=[]
    for value in cars.values():
        first_model.append(value[0])
    return first_model


def get_all_matching_models(grep='Trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    trail=[]
    # if grep == '':
    #     grep='Trail'
    for value in cars.values():
        for model in value:
            if grep.upper() in model.upper():
                trail.append(model)

    return sorted(trail)


def sort_car_models():
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    sorted_cars = {k: sorted(cars[k]) for k in sorted(cars)}
    #print(sorted_cars)
    # for key, value in cars.items():
    #     print(key,':',sorted(value))
    return sorted_cars

print(get_all_jeeps())
print(get_first_model_each_manufacturer())
print(get_all_matching_models('CO'))
print(sort_car_models())