#21000348 AndreSeo
#Winter Olympic


from functools import cmp_to_key

#Raw Information(a list)
information = [
"United States", 9, 15, 13,
"Germany", 10, 13, 7,
"Canada", 14, 7, 5,
"Norway", 9, 8, 6,
"Austria", 4, 6, 6,
"Russia", 3, 5, 7,
"South Korea", 6, 6, 2,
"China", 5, 2, 4,
"Sweden", 5, 2, 4,
"France", 2, 3, 6,
"Switzerland", 6, 0, 3,
"Netherlands", 4, 1, 3,
"Czech Republic", 2, 0, 4,
"Poland", 1, 3, 2,
"Italy", 1, 1, 3,
"Japan", 0, 3, 2,
"Finland", 0, 1, 4,
"Australia", 2, 1, 0,
"Belarus", 1, 1, 1,
"Slovakia", 1, 1, 1,
"Croatia", 0, 2, 1,
"Slovenia", 0, 2, 1,
"Latvia", 0, 2, 0,
"Great Britain", 1, 0, 0,
"Estonia", 0, 1, 0,
"Kazakhstan", 0, 1, 0]



##Making list of countries
countries = []
for i in range(int(len(information)/4)):
    countries.append(information[i*4])

##Making list of medals
golds = []
for i in range(int(len(information)/4)):
    golds.append(information[i*4+1])

silvers = []
for i in range(int(len(information)/4)):
    silvers.append(information[i*4+2])

bronzes = []
for i in range(int(len(information)/4)):
    bronzes.append(information[i*4+3])



##Defining Functions
def create_list(): #(nation, total, gold, silver, bronze)
    mdals = []
    totals = []
    for i in range(len(countries)):
        totals = golds[i]+silvers[i]+bronzes[i]
        mdals.append([countries[i], totals, golds[i], silvers[i], bronzes[i]])
    return mdals

##    total = []
##    for i in range(len(countries)):
##        totals.append((countries[i], gold[i], silvers[i], bronzes[i]))
##    return totals

def print_list(mdals):
    print ("%-16s" %'Countries' + "Total Number of Medals")
    for i in range(len(countries)):
        print ("%-16s" %(mdals[i][0]) + "%d"%(mdals[i][1]))
        m = sum(medals[i][1:])
##        print ("{0!s:15s}{1:5d}".format(medals[i][0],m))

def cmp(a, b):
    if a<b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

def compare(item1, item2):
    medals1 = sum(item1[1:])
    medals2 = sum(item2[1:])
    return cmp(medals1, medals2)

def sort_list(mdals):
    mdals.sort(key=cmp_to_key(compare))
    return mdals
       
def build_table(mdals):
    t=[0]*13                          
    for i in range(len(t)):
        for j in range(len(mdals)):
            if (i*3)<=(mdals[j][1])<((i+1)*3): #mdals[j][1] = totals
                t[i] += 1
    return t
  
def plot_table(t):
    print ("# of medals\t" + "# of countries")
    for i in range(13):
        print ("%d" %(3*i) + "~" + "%d" %(3*i+2) + ":\t\t" + "*"*t[i])
    

##Main Functions
medals = create_list()
print_list(medals)
print ("\n\n")


sort_list(medals)
print_list(medals)


print ("\n\n")
table = build_table(medals)#count number of countries
print (table)
plot_table(table) #marking with star(*)


