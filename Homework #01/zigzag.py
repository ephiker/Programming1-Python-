#zigzag
#21000348 Andre Seo

from cs1robots import *
create_world()

hubo = Robot()
hubo.set_trace("green")


#defining functions
def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()


#starting
for i in range(5):
    hubo.turn_left()

    #going up
    for j in range(9): 
        hubo.move()

    #linking
    turn_right()
    hubo.move()
    turn_right()
    
    #going down
    for k in range(9): 
        hubo.move()


    #escaping condition
    if (i!=4):
        hubo.turn_left()
        hubo.move()
    

        









