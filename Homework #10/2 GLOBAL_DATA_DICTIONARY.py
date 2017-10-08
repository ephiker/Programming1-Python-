#21000348 Andre Seo
#Global Data Dictionary


#Function Defining
def dic_search(dict, code):
    if code in dict:
        return True
    else:
        return False
    
def creating_dic():
    f = open("average-latitude-longitude-countries.csv", "r")
    count = 0;
    for line in f:
        if (count == 0):
            count += 1
        ##sepatating data element
        else:
            line = line.strip("\n")
            elements = line.split(",")
            code = elements[0].strip('"')
            elements[1] = elements[1].strip('"')
            if len(elements) == 4:
                name = elements[1]
                lati = float(elements[2])
                longi = float(elements[3])
                dic[code] = (name, lati, longi)##appending
            else:
                elements[2] = elements[2].strip('"')
                name = elements[2] + elements[1]
                lati = float(elements[3])
                longi = float(elements[4])
                dic[code] = (name, lati, longi)##appending



##1-1 Creating and Sorting and Printing List
print ("\n\n\n1-1 Creating and Sorting and Printing List")

dic ={}
creating_dic()

##print country chart
for key in dic:
    (name, lati, longi) = dic[key]
    print ("Code =", key, "/ Name =", name, "/ Latitude =", lati, "/ Longitude =", longi)
    



##1-2 Listing Countries in South of Equator
print ("\n\n\n1-2 Listing Countries in South of Equator")

for key in dic:
    (name, lati, longi) = dic[key]##unpacking tuple element
    if lati < 0:##if latitude < 0
        print (name)##print country name

    

##1-3 Input Code : Output Name  
print ("\n\n\n1-3 Input Code : Output Name")
while (1):
    input_code = input("Input Code : ")
    flag = dic_search(dic, input_code)##finding key in dictionary
    if flag:
        for key in dic:
            if input_code == key:
                (name, lati, longi) = dic[key]##unpacking tuple element
                print ("Country name is", name)
        break
    else:
        print ("Enter precise country code, please")



