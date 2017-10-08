#21000348 Andre Seo
#Monthly Teperature in London


##Function Defining
def creating_excel(data):
    f = open("tpmon.csv", "w")
    
    for i in range(len(data)):
        year = str(i+1723)
        f.write(year)
        for j in range(12):
            f.write(","),
            f.write(data[i][j],)
        f.write("\n")
    f.close()


    
    ##Confirming
    f = open("tpmon.csv", "r")
    for line in f:
        print (line, end="")
    f.close()


##def wintersummer(data):
##    count = -1
##    for year in data:
##        count +=1
##        ##Unpacking elements in a year
##        mon1, mon2, mon3, mon4, mon5, mon6, mon7, mon8, mon9, mon10, mon11, mon12 = year
##        ##Average Temperature 
##        winter_avrg = (float(mon1)+float(mon2))/2
##        summer_avrg = (float(mon7)+float(mon8))/2
####        print ((1737+count),":\t\t",winter_avrg,"/",summer_avrg)
##        print ("{0:4d}:{1:15.1f}/{2:0.1f}".format((1737+count),winter_avrg,summer_avrg ))
##    
        

def creating_chart():
    f = open("tpmon.txt", "r")
    data = []
    montem = []
    count = 0
    for line in f:
        if count==0:
            count +=1
        ##Separating elements
        else:
            elements = line.split("   ")
            elements = line.split(" ")
            for temp in elements:
                if len(temp)>1:
                    montem.append(temp)

        if (len(montem)==12):
            data.append(montem)##Appending
        montem = []##Reset
    return data
            

                    
data = creating_chart()
##print(data)

print ("\n\nWinter/Summer\n\n")
##wintersummer(data)
print ("\n\n\nExcel\n")
creating_excel(data)



f=open("tpmon.txt","r")# load file
count=0 # count start 
year = 0 # year start

for line in f: # file in the line
    year+=1 # count the year and add :year step by step
    if count==0: 
        count+=1 # except first line
        
    else: 
        line.strip()  
        month=line.split() # new_line
##        print(line)
        for i in range(len(month)): # every month
            month1,month2,month3,month4,month5,month6,month7,\
            month8,month9,month10,month11,month12 = month # the month 
            winter=(float(month1)+float(month2))/2 # winter temperature
            summer=(float(month7)+float(month8))/2 # summer temperature

