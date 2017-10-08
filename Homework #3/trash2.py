#tarsh2
#21000348 AndreSeo


from cs1robots import *
import random

x=random.randint(5,15)
y=random.randint(5,15)

#Making my world
#create_world(avenues = x, streets = y)
#edit_world()
#save_world("./worlds/myworld.wld")
#load_world("./worlds/myworld.wld")

#Other world
#load_world("./worlds/myworld2.wld")
load_world("./worlds/myworld3.wld")


hubo=Robot()
hubo.set_trace("Green")



def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

def back_starting_point():
    
    hubo.turn_left()

    while hubo.front_is_clear():
        hubo.move()
    hubo.turn_left()

    while hubo.front_is_clear():
        hubo.move()    
    
def picking_up_garbage():
    while True:
        
        while hubo.front_is_clear():
            while hubo.on_beeper():
                hubo.pick_beeper()
            hubo.move()

        hubo.turn_left()
        while hubo.on_beeper():
            hubo.pick_beeper()
            
        if not hubo.front_is_clear():
            break
        
        hubo.move()
        hubo.turn_left()

        while hubo.front_is_clear():
            while hubo.on_beeper():
                hubo.pick_beeper()
            hubo.move()

        turn_right()
        while hubo.on_beeper():
            hubo.pick_beeper()

        if not hubo.front_is_clear():
            break
        
        hubo.move()
        turn_right()


#Starting
picking_up_garbage()
back_starting_point()


        







    
