#plant1
#2100348 AndreSeo


from cs1robots import *
#create_world()
load_world("./worlds/harvest1.wld")
#load_world("./worlds/harvest3.wld")


hubo = Robot(beepers=100)
hubo.set_trace("Green")


#Defining Functions
def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()


def planting():
    while hubo.front_is_clear():
        if not hubo.on_beeper():
            hubo.drop_beeper()
        hubo.move()
        
    #double checking
    if not hubo.on_beeper():
            hubo.drop_beeper()


def left_u_turn():
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()


def right_u_turn():
    turn_right()
    hubo.move()
    turn_right()



#Starting planting
for i in range(3):
    planting()

    left_u_turn()

    planting()

    right_u_turn()



