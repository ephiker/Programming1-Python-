#harvest4
#21000348 Andre Seo

from cs1robots import *
#load_world("./worlds/harvest1.wld")
#load_world("./worlds/harvest3.wld")
load_world("./worlds/harvest4.wld")


hubo = Robot()
hubo.set_trace("green")
hubo.set_pause(1)


#Defining Functions
def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

    
def harvesting():
    while hubo.front_is_clear():
        hubo.move()
        if hubo.on_beeper():
            hubo.pick_beeper()


#turning and picking
def left_u_turn(): 
    hubo.turn_left()
    hubo.move()
    
    while hubo.on_beeper():
            hubo.pick_beeper() 
            
    hubo.turn_left()


#turning and picking
def right_u_turn():
    turn_right()
    hubo.move()
    
    while hubo.on_beeper():
            hubo.pick_beeper() 
            
    turn_right()


    
#Starting harvesting
for i in range (3):
    
    harvesting()

    left_u_turn()

    harvesting()

    right_u_turn()
    



    

    

    
    
    
