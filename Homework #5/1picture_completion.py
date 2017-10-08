#21000348 AndreSeo
#Picture Completion

from cs1graphics import *
paper = Canvas(400,200,"skyblue","400*200 village")
#검색 class Canvas
#class rectangle


def draw_grass(): #grass를 그리는 함수
    grass = Rectangle(400,80, Point(200, 160)) #객체생성
    grass.setFillColor("springgreen3") #색칠하기
    grass.setBorderColor("springgreen3") #테두리색정하기
    grass.setBorderWidth(10) #테두리두께정하기
    grass.setDepth(100) #깊이감 깊을수록 뒤에 배치된
    paper.add(grass) #아까그페이퍼에 add라는 함수가 있고 grass라는 객체를 삽입한다

def draw_sun():
    sun = Circle(25, Point(60, 45))
    sun.setFillColor("orangered")
    sun.setBorderColor("darkorange")
    paper.add(sun)

def draw_sunrays():
    sunray1 = Path(Point(90,45), Point(110,45)) #포인트1에서 포인트2로 직선
    sunray1.setBorderColor("darkorange")
    sunray1.setBorderWidth(3)
    paper.add(sunray1)

    sunray2 = Path(Point(80,65), Point(95,80))
    sunray2.setBorderColor("darkorange")
    sunray2.setBorderWidth(3)
    paper.add(sunray2)

    sunray3 = Path(Point(60,75), Point(60,95))
    sunray3.setBorderColor("darkorange")
    sunray3.setBorderWidth(3)
    paper.add(sunray3)

def draw_trees():
    tree1 = Polygon(Point(350, 100), Point(330, 150), Point(370, 150))
    tree1.setFillColor("darkolivegreen3")
    tree1.setDepth(80)
    paper.add(tree1)

    tree2 = tree1.clone()
    tree2.move(-40,-10)
    tree2.scale(0.9)
    tree2.setFillColor("forestgreen")
    tree2.setDepth(90)
    paper.add(tree2)

    tree3 = tree1.clone()
    tree3.move(-90,5)
    tree3.scale(1.1)
    tree3.setDepth(40)
    tree3.setFillColor("greenyellow")
    paper.add(tree3)
    
def draw_house():
    #캔버스 위에 바로 서로 다른 모양들을 그려 집을 만든 것
    # house = something 이라고 한마디로 선언할 수 없다.
    
    facade = Square(50, Point(140,110))
    facade.setFillColor("white")
    facade.setDepth(100)
    paper.add(facade)

    chimney = Rectangle(15, 20, Point(155,75))
    chimney.setFillColor("gray80")
    chimney.setBorderWidth(0)
    chimney.setDepth(70)
    paper.add(chimney)

    smoke = Path(Point(155,60), Point(150,55), Point(160,50), Point(155,45))
    smoke.setBorderColor("gray60")
    paper.add(smoke)

    roof = Polygon(Point(105,95),Point(175,95),Point(165,75),Point(115,75))
    roof.setFillColor("brown3")
    roof.setDepth(90)
    paper.add(roof)

    window = Polygon(Point(125,110),Point(125,130), Point(140,130), Point(140,110))
    window.setFillColor("skyblue")
    window.setDepth(80)
    window.setBorderWidth(0)
    paper.add(window)

def move(obj):

    for i in range(25):
        obj.move(1,0)

    for i in range(45):
        obj.move(5,0)

def draw_car(): 
    car = Layer()
    #투명 레이어 위에 그림을 그려 그것을 차를 만들어 사용

    
    tire1 = Circle(10, Point(-20, -10))
    tire1.setFillColor("gray40")
    tire1.setDepth(65)
    car.add(tire1) #레이어 위에 추가

    tire2 = Circle(10, Point(20,-10))
    tire2.setFillColor("gray40")
    tire2.setDepth(65)
    car.add(tire2)
    
    body = Rectangle(70, 30, Point(0,-25))
    body.setFillColor("navyblue")
    body.setDepth(70)
    car.add(body)
    
    car.moveTo(0,160) #레이어의 초기 위치(초기 좌표 설정)
    paper.add(car) #페이퍼에 레이어를 붙임
    move(car) #투명레이어를 움직임


#Drawing Picture
draw_grass()
draw_sun()
draw_sunrays()
draw_trees()
draw_house()
draw_car()




