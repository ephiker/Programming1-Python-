#hurdles3
#21000348 Andre Seo

from cs1robots import *
#load_world("./worlds/hurdles1.wld")
#load_world("./worlds/hurdles2.wld")
load_world("./worlds/hurdles3.wld")

hubo = Robot()
hubo.set_trace("Green")

                    

#Defining Functions
def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()


def jumping(): 
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()


#Moving or Jumping and Breaking
while not hubo.on_beeper():

    while hubo.front_is_clear():
        hubo.move()

    if hubo.on_beeper():
        break

    jumping()



    


