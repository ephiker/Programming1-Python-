#21000348 Andre Seo
#Data Plotting


import cs1media

x_step = 5
min_y = 700
max_y = 2000
y_step = 0.5

years = range(1994,2010) #making list of 1994 ~ 2009


#Defining Functions
def read_year(yr):
    fname = "data/%d.txt" %yr #making names of files to open
    f = open(fname, "r")
    data = []
    for line in f: #reformatting the data
        date1, value1 = line.split()#unpacking line by line
        value = float(value1)
        value = int(1.0/value) #exchage to KRW
        ys, ms, ds = date1.split("/")
        date = 10000*int(ys) + 100*int(ms) + int(ds) #reformatting
        data.append((date, value)) #appending as tuple type
    f.close()
    return data


def find_minmax(yr):
    minmax = [(9999,0)]*12 #making list of 12 tuples
    data = read_year(yr)
    for d, v in data:
        month = int((d/100) % 100 - 1)
        minr, maxr = minmax[month]
        if v < minr:
            minr = v
        if v > maxr:
            maxr = v
        minmax[month] = minr, maxr
    return minmax


def main():
    w = len(years) * 12 * x_step
    h = int((max_y - min_y) * y_step)
    p = cs1media.create_picture(w,h,cs1media.Color.white)
    #vertical line for every january
    for yr in years:
        x = (yr - years[0]) *12 * x_step
        for y in range(h):
            p.set(x, y, cs1media.Color.gray)
    #horizontal line per 100 won
    for won in range(min_y, max_y, 100):
        y = int((won - min_y) * y_step)
        for x in range(w):
            p.set(x,y,cs1media.Color.gray)
    for yr in years:
        #monthly minmax list of tuples
        minmax = find_minmax(yr)
        for m in range(12):
            x = ((yr-years[0]) * 12+m)*x_step
            y1 = int((minmax[m][0]- min_y) * y_step)
            y2 = int((minmax[m][1]- min_y) * y_step)
            for y in range(h - y2, h - y1 + 1): #flip
                #two lines make it visible well
                p.set(x,y, cs1media.Color.red)
                p.set(x+1, y, cs1media.Color.red)
    p.show()
    p.save_as("krw.png")
    
main()


