#21000348 AndreSeo
#Sun Amimation


from cs1graphics import *
import math


#Defining Functions
def interpolate_color(t, color1, color2):
    r1, g1, b1 = Color(color1).getColorValue()
    r2, g2, b2 = Color(color2).getColorValue()
    if t<0:
        a = (int((t+1)*r1-t*r2), int((t+1)*g1-t*g2), int((t+1)*b1-t*b2))
        print(Color(a).getColorValue())
        return (int((t+1)*r1-t*r2), int((t+1)*g1-t*g2), int((t+1)*b1-t*b2))
    else:
        return (int((1-t)*r1+t*r2), int((1-t)*g1+t*g2), int((1-t)*b1+t*b2))

##
def animate_sunrise(sun):
    w = paper.getWidth()
    h = paper.getHeight()
    r = sun.getRadius()
    x0 = w/2.0
    y0 = h+r
    max_x = w/2.0-r
    max_y = h

    #0도에서 180도까지 움직이면서 해의 위치가 한칸씩 
    for angle in range(360):
        rad=(angle/180) * math.pi
        
        x = x0 - max_x * math.cos(rad)
        y = y0 - max_y * math.sin(rad)
        
        sun.moveTo(x,y)
        
        bgcolor = interpolate_color(math.sin(rad), "midnightblue", "lavender")
##        bgcolor = (0, 0, 255)
        paper.setBackgroundColor(bgcolor)
        

##        suncolor = interpolate_color(math.sin(rad), "red", "orange")
##        sun.setFillColor(suncolor)



#Animation
paper = Canvas(400,300)
paper.setBackgroundColor("skyblue")

sun = Circle(25, Point(0,150))
sun.setFillColor("orangered")
sun.setBorderColor("darkorange")

paper.add(sun)        
animate_sunrise(sun)


