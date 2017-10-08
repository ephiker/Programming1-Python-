#21000348 AndreSeo
#re-implement adding beepers


############################################
####Create a world
##from cs1robots import *
##create_world()
##edit_world()
##save_world("./worlds/all_columns.wld")
############################################


from cs1robots import *
load_world("./worlds/all_columns.wld")
hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(1)



#Defining Functions
def turn_around():
    hubo.turn_left()
    hubo.turn_left()
    
def pick_beeper():
    while hubo.on_beeper():
        hubo.pick_beeper()

def add_beeper():
    while hubo.carries_beepers():
        hubo.drop_beeper()

def more_column():
    if hubo.front_is_clear():
        return True
    else:
        return False

def go_down_and_add():
    turn_around()
    while hubo.front_is_clear():
    #added while-statement in order to pick "all beepers" on world
        hubo.move()
    hubo.turn_left()
    add_beeper()

def go_up_and_pick():
    hubo.turn_left()
    while hubo.front_is_clear():
    #added while-statement in order to pick "all beepers" on world
        hubo.move()
        pick_beeper()

def collect_beeper_in_a_column():
    go_up_and_pick()
    go_down_and_add()
    if hubo.front_is_clear():
        hubo.move()

def go_back_home():
    turn_around()
    while hubo.front_is_clear():
        hubo.move()
    turn_around()

def process_all_column():
    while more_column():
        collect_beeper_in_a_column()
    collect_beeper_in_a_column()#at last column
    go_back_home()#finishing



process_all_column()



