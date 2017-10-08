#21000348 Andre Seo
#Playing With Palindromes


def new_line():
    print ("\n", "%25s" %' ', end = " ")
    
def display(lst, length):
    print (lst)
    count = 0 
    print ("%4s" %length, "%10s" %len(lst), "%10s" %' ', end = " ") ##첫줄

    for i in range(len(lst)):
        
        if 35 <= count:
            new_line()
            print (lst[i], end =" ")
            count = 0
        else:
            print (lst[i], end=" ")
            count += (length + 1) #(space of length + space of whitespace)
        
    print ("\n")


def print_summary(list):
    length = 0
    lst = []
    print ("%-10s" %"Length", "%-15s" %"Frequency", "%s" %"Palindromes")
    print ("\n")
    flag = True
    for leng, word in list:
        if length != leng:
            if flag == True:
                flag = False
            else:
                display(lst, length)
            lst = [word]
            length = len(word)
        else:
            lst.append(word)
    display(lst, length)
    
    

def is_palindrome(word):
    start = 0
    end = len(word)-1
    for i in range (int(len(word)/2)):
        if word[start] != word[end]:#condiiton of palindrome
            return False
        else:
            start +=1
            end -=1
    return True


##def palin(word):
##    start = 0
##    end = len(word)-1
##    if word[start] == word[end]:
##        palin
##    for i in range (int(len(word)/2)):
##        if word[start] != word[end]:#condiiton of palindrome
##            return False
##        else:
##            start +=1
##            end -=1
##    return True



def create_list():
    list = []
    file = open("words.txt", "r")
    for line in file:
        word = line.strip()#strip whitespace
##        if palin(word):
        if is_palindrome(word):
            list.append((len(word),word))
##    print (list)
    return list


def main():
    pal_list = create_list()
    pal_list.sort() #not a,b,c order but increasing order
    print_summary(pal_list)


main()
