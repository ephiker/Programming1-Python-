#21000348 Andre Seo
#USD-KRW Exchange Rate

years = range(1994,2010) #making list of 1994 ~ 2009

#Defining Functions
def read_year(yr, data):
##    fname = "data/%d.txt" %yr #making names of files to open
    fname = "data/{}.txt".format(yr)
##    print fname
    f = open(fname, "r")
    for line in f: #reformatting the data
        date1, value1 = line.split()#unpacking line by line
        value2 = float(value1)
        value = int(1.0/value2) #exchage to KRW
        ys, ms, ds = date1.split("/")
        date = 10000*int(ys) + 100*int(ms) + int(ds) #reformatting
        data.append((date, value)) #appending as tuple type
    f.close()
    return data

def create_list_with_files():
    data = []
    for yr in years:
        data = read_year(yr, data)
    return data


#Main 
data = [] # list of (date, rate) tuples
data = create_list_with_files()



print ("\n")
print ("len(data) is ", len(data))
print ("(365*16) + (1*4) = ", (365*16) + (1*4))

print ("\n")
print ("data[0] :", data[0])
print ("data[1000] :", data[1000])
print ("data[2000] :", data[2000])
print ("data[3000] :", data[3000])
print ("data[4000] :", data[4000])
print ("data[5000] :", data[5000])
print ("data[5843] :", data[5843])


