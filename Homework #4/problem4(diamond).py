#21000348 AndreSeo
#problem4(diamond)


from cs1robots import *
load_world("./worlds/harvest2.wld")

hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.1)



#condition for initial movement
def move_to_bottom(robot):
    for i in range(5):
        robot.move()
    robot.turn_left()
    robot.move()


def turn_right(robot):
    for i in range(3):
        robot.turn_left()


#pick beepers all on a side
def move_and_pick(robot, n): 
    for i in range (n):
        robot.pick_beeper()
        robot.move()
        turn_right(robot)
        robot.move()
        robot.turn_left()


#move and pick on four side
def diamond(robot, n): 
    for i in range(4): 
        move_and_pick(robot, n)
        robot.turn_left()

#3 steps for 3 layer
def pick_beepers(robot):
    for i in range(3):
        n = 5-2*i #n is numbers of beepers on a side (5, 3, 1)
        diamond(robot, n)
        if n > 2: #codition for moving to next diamond
            robot.move()
            robot.move()


def harvest_all(robot):
    move_to_bottom(robot)#move to next bottom of smaller diamond
    pick_beepers(robot)#pick beepers shaping diamond
    


#main
##harvest_all(hubo)





