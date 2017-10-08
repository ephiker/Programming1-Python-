#21000348 Andre Seo
#Chromakey

from cs1media import *
import math
campus = load_picture("./photos/trees1.jpg")
statue = load_picture("./photos/statue1.jpg")


#Euclidian distance in (r,g,b) color space
def dist(color, bckgrnd):
    r1, g1, b1 = color
    r2, g2, b2 = bckgrnd
    return(math.sqrt((r1-r2)**2 + ( g1-g2)**2 + (b1-b2)**2))


def chroma(x1, y1, keypoint, threshold):
    w, h = statue.size()
    for y in range(h):
        for x in range(w):
            point = statue.get(x,y)
            if dist(point, keypoint) > threshold:
                campus.set(x1+x, y1+y, point)#overlay statue on campus

def reflection(img):
    w, h = img.size()
    for y in range(0,h):
        for x in range (0, int(w/2)):
            left = img.get(x, y)
            right = img.get(w-1-x, y)
            img.set(x,y, right) #right to left
            img.set(w-1-x,y, left) # left to right

def main():
    reflection(statue)
    keypixel = (41,75,146)
    threshold = 70
    chroma(200, 50, keypixel, threshold) #(200, 50) is starting pixel
    

main()
campus.show()
