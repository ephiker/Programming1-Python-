#rain1
#21000348 AndreSeo


from cs1robots import *
load_world("./worlds/rain1.wld")

hubo = Robot(beepers=99, avenue=2, street=6, orientation='E')
hubo.set_trace("Green")
hubo.set_pause(0.5)



#Defining Functions
def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()


def turn_back():
    hubo.turn_left()
    hubo.turn_left()




#Starting
hubo.move()
hubo.drop_beeper()
turn_right()
hubo.move()


while True:
    
    while hubo.front_is_clear(): 
        hubo.move()
        
        if hubo.on_beeper():
            break
        
        turn_right()
        
        if not hubo.front_is_clear(): #wall!
            hubo.turn_left()
            
        else: #windows!
            hubo.drop_beeper()
            hubo.turn_left()


    hubo.turn_left()#cornering
    if hubo.on_beeper():
        break


#Finishing
hubo.pick_beeper()
turn_back()





