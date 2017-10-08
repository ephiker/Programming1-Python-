#hurdle
#21000348 AndreSeo


from cs1robots import *
load_world("worlds/hurdles1.wld")

hubo = Robot(beepers=1)
hubo.set_trace("green")


#defining functions
def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

def leap_over():
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()


#leaping over hurdles
for i in range(4):
    leap_over()

#picking up beeper
hubo.move()
hubo.pick_beeper()
turn_right()
