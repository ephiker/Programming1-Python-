#three_color_poster
#21000348 AndreSeo


from cs1media import *
img = load_picture("./martian.jpg")


#Original Image
img.show() 


#Converting
w,h = img.size()
for y in range(h):
    for x in range(w):
        r, g, b=img.get(x,y)
        v=(r+g+b)/3.0
        if v > 130:
            img.set(x,y,(80,65,70))
        elif v < 65:
            img.set(x,y,(200,190,180))
        else:
            img.set(x,y,(180,135,100))


#Three Color Poster
img.show()
