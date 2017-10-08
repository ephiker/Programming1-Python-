##21000348 Andre Seo
## Procedural Journey of Chicken

from cs1graphics import*

canvas = Canvas(1000, 300)
canvas.setBackgroundColor("light blue")
canvas.setTitle("Journey of Chicken")
canvas.wait()

#Create the ground
def create_ground():
    ground = Rectangle(1000,100)
    ground.setFillColor("light green")
    ground.move(500,250)
    canvas.add(ground)

#Create the sun
def create_sun():
    sun = Circle(50)
    sun.setFillColor("red")
    sun.setBorderColor("red")
    sun.move(25,25)
    canvas.add(sun)


#Draw a chicken
def make_chicken(hen = False):
    layer = Layer()
    make_body(layer, hen)
    wing = make_wing(layer, hen)
    make_eye(layer, hen)
    make_beak(layer, hen)
    make_dots(layer, hen)
    return layer, wing


######################################################


#Make a body
def make_body(layer, hen = False):
    if hen:
        body = Ellipse(70, 80)
        body.setFillColor("white")
    else:
        body = Ellipse(40, 50)
        body.setFillColor("yellow")
        body.move(0,10)
    body.setBorderColor("yellow")
    body.setDepth(20)
    layer.add(body)


#Draw a wing
def make_wing(layer, hen = False):
    if hen:
        wing = Ellipse(60, 40)
        wing.setFillColor("white")
        wing.setBorderColor("yellow")
        wing.move(15,20)
    else:
        wing = Ellipse(30,20)
        wing.setFillColor("yellow")
        wing.setBorderColor("orange")
        wing.move(10,20)
        wing.adjustReference(-5, -5)
    wing.setDepth(19)
    layer.add(wing)
    return wing


#Draw and eye
def make_eye(layer, hen = False):
    if hen:
        eye = Circle(3)
        eye.move(-15,-15)
    else:
        eye = Circle(2)
        eye.move(-5, 0)
    eye.setFillColor("black")
    eye.setDepth(18)
    layer.add(eye)

#Draw a beak
def make_beak(layer, hen = False):
    if hen:
        beak = Square(8)
        beak.move(-36, 0)
    else:
        beak = Square(4)
        beak.move(-22, 10)
        beak.rotate(45)
    beak.setFillColor("orange")
    beak.setBorderColor("orange")
    beak.setDepth(21)
    layer.add(beak)


#Draw dots
def make_dots(layer, hen = False):
    if hen:
        head1 = Ellipse(5,8)
        head1.setFillColor("red")
        head1.setBorderColor("red")
        head1.move(600,158)
        head1.setDepth(22)
        layer.add(head1)

        head2 = Ellipse(5,8)
        head2.setFillColor("red")
        head2.setBorderColor("red")
        head2.move(594,458)
        head2.setDepth(22)
        layer.add(head2)

######################################################

        
#Draw the group
def make_group():##mother hen + baby chicken1
    group = Layer()
    mother_hen, wing = make_chicken(True)
    group.add(mother_hen)
    (chicken1, wing1) = make_chicken()
    chicken1.move(120, 0)
    group.add(chicken1)
    group.move(600,200)
    return group


def make_family():
    group = make_group()
    chicken2, wing2 = make_chicken()
    chicken2.move(800,200)
    canvas.add(group)
    canvas.add(chicken2)
    return group, chicken2, wing2


#Create the scene
def create_scene():
    create_ground()
    create_sun()
    group, chicken2, wing2 = make_family()
    return group, chicken2, wing2


def move_group(group):
    for i in range(80):
        group.move(-5,-2)
        group.move(-5,2)
        if i == 30:
            text1 = Text("OH!", 20)
            text1.move(800, 160)
            canvas.add(text1)
        elif i == 40:
            canvas.remove(text1)
            text2 = Text("WHERE IS MY MOMMY GOING?", 30)
            text2.move(500, 110)
            canvas.add(text2)
        elif i == 55:
            canvas.remove(text2)


def move_chicken2(chicken2, wing2):
    for i in range(10):
        text3 = Text("Waif for ME~", 25)
        text3.move(500, 110)
        canvas.add(text3)
        for k in range(5):
            chicken2.move(-10, -20)
            wing2.rotate(-10)
        for k in range(5):
            chicken2.move(-10, 20)
            wing2.rotate(10)


def animate_chicken_family():
    group, chicken2, wing2 = create_scene()
    move_group(group)
    move_chicken2(chicken2, wing2)


def main():
    animate_chicken_family()
    canvas.wait()
    canvas.close()


main()






    
