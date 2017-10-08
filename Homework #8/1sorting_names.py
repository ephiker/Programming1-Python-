#Soirting Names
#21000348 Andre Seo

import string



##### F U N C T I O N S #####

def tiebreaker(firstandlast):
    first, last = firstandlast.split(" ")
    return first #split and compare first name

def spliting(firstandlast):
    first, last = firstandlast.split(" ")
    return last #split and compare last name

def com_names(a, b):
    if (spliting(a) > spliting(b)):
        return 1
    elif (spliting(a) == spliting(b)): #if two last names are tied
        if (tiebreaker(a) > tiebreaker(b)):
            return 1
        else:
            return 0
    else:
        return 0

#(len(L)-1) = number of list
def bubble (L,com_names):
    for i in range (len(L)-1):
        for j in range(len(L)-1-i):
            first = (len(L)-1)-(j+1)
            second = (len(L)-1)-(j)
            if com_names(L[first], L[second]): #if L[a]>L[b] is true
                L[first], L[second] = L[second], L[first] #맞교환
    return L #unsorted list to sorted list now


    

##### M A I N #####

#Big Choi and Changbum Choi and others
Names = ["Big Choi", "Chris Terman", "Tom Brady", "Eric Grimson", "Joseph Shin", "Changbum Choi"]

print ("\n\n\n")
print ("unsorted")
print (Names)

bubble(Names, com_names)

print ("\n\n\n")
print ("sorted")
print (Names)







