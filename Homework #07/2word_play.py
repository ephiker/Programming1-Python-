#21000348 Andre Seo
#Word Play




##############################
####1.SELECTING LONG WORDS####
##############################
print "SELECTING LONG WORDS"
print "===================="
file = open("words.txt", "r")
count = 0
for word in file:
    word = word.strip()#strip whitespace
    if len(word)>18:
        count += 1
        print word
print "no. of words = ", count
file.close()
print "===================="
print "SELECTING LONG WORDS"
print "\n\n\n"





##############################
####2.FINDING PALINDROMES#####
##############################
#Defining a Function
def is_palindrome(word):
    start = 0
    end = len(word)-1
    for i in range (len(word)/2):
        if word[start] != word[end]:#condiiton of palindrome
            return False
        else:
            start +=1
            end -=1
    return True



print "FINDING PALINDROMES"
print "==================="
file = open("words.txt", "r")
count = 0
for line in file:
    word = line.strip()#strip whitespace
    if is_palindrome(word):
        print word
        count += 1
print "no. of words = ", count
file.close()
print "==================="
print "FINDING PALINDROMES"
print "\n\n\n"






##############################
####3.FINDING WORD WITHOUT E##
##############################
#Defining a Function
def is_have_e(word):
    for i in range(len(word)):
        if word[i] == 'e': #finding word *with* e
            return True


print "FINDING WORD WITHOUT E"
print "======================"



#number of all line - number of line with e
file = open("words.txt", "r")
all_line = 0
count = 0
for line in file:
    all_line += 1
    word = line.strip()#strip whitespace
    if is_have_e(word):
        count += 1
file.close()
print "no. of words = ", (all_line - count) 
print "======================"
print "FINDING WORD WITHOUT E"
print "\n\n\n"





##############################
####4.FINDING TRIPLE LETTERS##
##############################
#Defining a Function
def have_triple(word):
    counting = {}
    for letter in word:
        if letter not in counting:
            counting[letter] = 1
        else:
            counting[letter] += 1

    for letter in word:
##        if (counting[letter] == 3): #three of the same letter*****
        if (counting[letter] >= 3): #more than three of the same letter*****
            return True


print "FINDING TRIPLE LETTERS"
print "======================"
file = open("words.txt", "r")
count = 0
for line in file:
    word = line.strip()#strip whitespace
    if have_triple(word):
        count += 1
file.close()
print "no. of words = ", count
print "======================"
print "FINDING TRIPLE LETTERS"
print "\n\n\n"






##############################
####5.ABECEDARIAN#############
##############################
#Defining a Function
def is_abecede(word):
    letters_list = []
    for letter in word:
        letters_list.append(letter)
    
    for i in range (len(word)-1):
        
        if letters_list[i]<=letters_list[i+1]:
            flag = True
        else:
            return False
    return flag
    
print "FINDING ABECEDARIAN"
print "==========="
file = open("words.txt", "r")
count = 0
for line in file:
    word = line.strip()#strip whitespace
    if is_abecede(word):
        count += 1
        print word
file.close()
print "no. of words = ", count
print "==========="
print "FINDING ABECEDARIAN"
print "\n\n\n"

