#harvest
#21000348 Andre Seo



from cs1robots import *
load_world("worlds/harvest1.wld")
hubo = Robot()


#defining functions
def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

def pick_six():
    for i in range(5):
        hubo.pick_beeper()
        hubo.move()
    hubo.pick_beeper()

def odd():
    pick_six()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()

def even():
    pick_six()
    turn_right()
    hubo.move()
    turn_right()
    


#starting
hubo.move()

for i in range(3):
    odd()
    even()


#ending    
turn_right()









