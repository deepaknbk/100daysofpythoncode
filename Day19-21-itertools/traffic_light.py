from time import sleep
import itertools
import random

colors =['Red','Green','Amber']
rotation =itertools.cycle(colors)

def rg_timer():
    return random.randint(3,7)

def light_rotation(rotation):
    for color in rotation:
        if color=='Amber':
            print(f'Caution! The light is {color}')
            sleep(3)
        elif color=='Red':
            print(f'STOP! The light is {color}')
            sleep(rg_timer())
        else:
            print(f'Go! The light is {color}')
            sleep(rg_timer())


if __name__=='__main__':
    light_rotation(rotation)

