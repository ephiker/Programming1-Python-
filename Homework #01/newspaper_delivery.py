#newspaper delivery
#21000348 Andre Seo


from cs1robots import *
load_world("worlds/newspaper.wld")

hubo = Robot(beepers = 1)
hubo.set_trace("green")



#defining functions
def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()    
    
def climb_up():
    hubo.set_trace("green")
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.move()

def climb_down():
    hubo.set_trace("red")
    hubo.move()
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()
    

#starting
hubo.move()
    
#climbing up stairs
for i in range(4):
    climb_up()

#drop down
hubo.drop_beeper()

#turning back
hubo.turn_left()
hubo.turn_left()

#climbing down stairs
for j in range(4):
    climb_down()

#ending
hubo.move()
hubo.turn_left()
hubo.turn_left()



