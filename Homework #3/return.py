#return
#21000348 AndreSeo

from cs1robots import *
import random

create_world()


#Initial Position
x = random.randint(1,10)
y = random.randint(1,10)


#Initial Orientation
num = random.randint(1,4)
if num==1:
    o="E"
elif num==2:
    o="W"
elif num==3:
    o="S"
else:
    o="N"



hubo = Robot(beepers=100, orientation = o, avenue = x, street = y)
hubo.set_trace("Green")


#Defining Functions
def turn_back():
    hubo.turn_left()
    hubo.turn_left()

def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()
    
def first_step_and_facing_west():
    hubo.set_pause(1)

    if o=="N":
        if hubo.front_is_clear():
            hubo.move()
            hubo.turn_left()
            
        else:
            turn_back()
            hubo.move()
            turn_right()

        
    elif o=="E":
        if hubo.front_is_clear():
            hubo.move()
            turn_back()
        
        else:
            turn_back()
            hubo.move()

        
    elif o=="S":
        if hubo.front_is_clear():
            hubo.move()
            turn_right()
        
        else:
            turn_back()
            hubo.move()
            hubo.turn_left()

        
    elif o=="W":
        if hubo.front_is_clear():
            hubo.move()
        
        else:
            turn_back()
            hubo.move()
            turn_back()


def returning():
    hubo.set_pause(0.2)
    while hubo.front_is_clear():
        hubo.move()

    hubo.turn_left()

    while hubo.front_is_clear():
        hubo.move()

    hubo.turn_left()

    

#Starting
first_step_and_facing_west()
returning()





