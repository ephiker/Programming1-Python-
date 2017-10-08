#21000348 AndreSeo
#adding beepers

from cs1robots import *
load_world("./worlds/add34.wld")

hubo = Robot()
hubo.set_trace("Green")
hubo.set_pause(10)


#Top-down programming
#Defining functions
def collect_first():
    while hubo.on_beeper():
        hubo.pick_beeper()

def collect_second():
    while hubo.on_beeper():
        hubo.pick_beeper()

def turn_back():
    hubo.turn_left()
    hubo.turn_left()

def go_up():
    hubo.turn_left()
    hubo.move()
    
def go_down():
    turn_back()
    hubo.move()
    hubo.turn_left()

def drop_down():
    while hubo.carries_beepers():
        hubo.drop_beeper()

def collect_and_drop():
    collect_first()
    go_up()
    collect_second()
    go_down()
    drop_down()

def go_next():
    hubo.move()
    
def come_back():
    turn_back()
    while hubo.front_is_clear():
        hubo.move()
    turn_back()
    
def add_beepers():
    while hubo.front_is_clear():
        collect_and_drop()
        go_next()

    collect_and_drop()#at last column
    come_back()#finishing



#Starting
add_beepers()


