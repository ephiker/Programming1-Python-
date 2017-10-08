##21000348 Andre Seo
##Object-Oriented Journey of Chicken 

from cs1graphics import*

canvas = Canvas(1000, 300)
canvas.setBackgroundColor("light blue")
canvas.setTitle("Journey of Chicken")
canvas.wait()


class Ground(object):
    def __init__(self):
        ground = Rectangle(1000,100)
        ground.setFillColor("light green")
        ground.move(500,250)
        canvas.add(ground)

class Sun(object):
    def __init__(self):
        sun = Circle(50)
        sun.setFillColor("red")
        sun.setBorderColor("red")
        sun.move(25,25)
        canvas.add(sun)

class Group(object):
    def __init__(self):
        self.hen = Chicken(True)
        self.chick1 = Chicken()
        self.chick1.layer.move(120,0)
        self.layer = Layer()
        self.layer.add(self.hen.layer)
        self.layer.add(self.chick1.layer)
        self.layer.move(600,200)

#############################################

class Body(object):
    def __init__(self, layer, hen):
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


class Wing(object):
    def __init__(self, layer, hen):
        self.layer = Layer()#
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


class Eye(object):
    def __init__(self, layer, hen):
        if hen:
            eye = Circle(3)
            eye.move(-15,-15)
        else:
            eye = Circle(2)
            eye.move(-5, 0)
        eye.setFillColor("black")
        eye.setDepth(18)
        layer.add(eye)


class Beak(object):
    def __init__(self, layer, hen):        
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


class Dots(object):
    def __init__(self, layer, hen):
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
        
class Chicken(object):
    def __init__(self, hen = False):
        self.layer = Layer()
        self.body = Body(self.layer, hen)
        self.wing = Wing(self.layer, hen)
        self.eye = Eye(self.layer, hen)
        self.beak = Beak(self.layer, hen)
        self.dots = Dots(self.layer, hen)


#############################################

class Family(object):
    def __init__(self):
        self.group = Group()
        self.chick2 = Chicken()
        self.chick2.layer.move(800,200)
        canvas.add(self.group.layer)
        canvas.add(self.chick2.layer)

    def move(self,x,y):
        self.group.layer.move(x,y)

    def rotate(self, z):
        self.chick2.layer.rotate(z)

    def move_chick2(self,x,y):
        self.chick2.layer.move(x,y)


                 
def group_move(scene):
    for i in range(80):
        scene.family.group.layer.move(-5,-2)
        scene.family.group.layer.move(-5,2)
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
            

def chicken2_move(scene):
    for i in range(10):
        text3 = Text("Waif for ME~", 25)
        text3.move(500, 110)
        canvas.add(text3)
        for k in range(5):
            scene.family.chick2.layer.move(-5, -10)
            scene.family.chick2.layer.move(-5, -10)

        for k in range(5):
            scene.family.chick2.layer.move(-5, 10)
            scene.family.chick2.layer.move(-5, 10)



class Scene(object):
    def __init__(self):
        self.ground = Ground() #씬은 땅이라는 객체를 가짐
        self.sun = Sun() #씬은 썬이라는 객체를 가짐
        self.family = Family() #씬은 빼밀리이라는 객체를 가짐

    def move(self,x,y):
        self.family.move(x,y)

    def move_chick2(self,x,y):
        self.family.move_chick2(x,y)

    def rotate(self, z):
        self.family.rotate(z)

def animate_chickens(scene):
    group_move(scene)
    chicken2_move(scene)


        

   
def main():
    scene = Scene()
    animate_chickens(scene)
    canvas.wait()



main()


    
