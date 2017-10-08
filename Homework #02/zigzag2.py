#zigzag2
#21000348 AndreSeo


from cs1robots import *
import random


#creating random-size world
x = random.randint(2,20)
y = random.randint(2,20)
create_world(avenues = x, streets = y)

hubo = Robot()
hubo.set_trace("Green")



#Defining Functions
def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()



#Starting zigzaging
hubo.turn_left()

while True: 

    #going north
    while hubo.front_is_clear():
        hubo.move()


    #at the top-most, hubo looks eastward
    turn_right()

    if hubo.front_is_clear():
        hubo.move()
        turn_right()
        
    else: 
        break #if front is not clear, hubo stops..


    #going south
    while hubo.front_is_clear():
        hubo.move()


    #at the down-most, hubo looks eastward
    hubo.turn_left() 

    if hubo.front_is_clear():
        hubo.move()
        hubo.turn_left()
        
    else: 
        break #if front is not clear, hubo stops..
    

    #going north
    #at the top-most, hubo looks eastward
    #going south
    #at the down-most, hubo looks eastward






    
