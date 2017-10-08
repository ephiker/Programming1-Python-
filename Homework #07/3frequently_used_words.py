#21000348 Andre Seo
#Frequntly Used Words



import string

wordsfile = open("words.txt", "r")
emmafile = open("emma.txt", "r")


#'word' means a word in words.txt
#'words' means a list having words as element
#'wrd' meas a word in emma.txt
#'emmawords' means a list having words in emma.txt as element


#Defining a Function
def is_in_dic(wrd):
    if wrd in dic:
        return True
    else:
        return False
        
    
#Creating a dictionary
dic = {}
words = []

for line1 in wordsfile:
    word = line1.strip()
    if (5<=len(word)) and (len(word)<=10):
        words.append(word)

for i in range(len(words)):
    dic[words[i]]=0



#Skipping the header
for line2 in emmafile:
    if line2.startswith('*END*THE SMALL PRINT!'):
        break


    
#Spliting, Striping, Counting
for line2 in emmafile:
    for wrd in line2.split():
        wrd = wrd.strip(string.punctuation + string.whitespace)
        wrd = wrd.lower()
        if is_in_dic(wrd):
            dic[wrd] += 1

emmawords = []
emmawords = dic.items()


#Shifting element's location
emmawords2 = []
for i in range(len(emmawords)):
    shift = [emmawords[i][1], emmawords[i][0]]
    emmawords2.append(shift)



#Solting    
emmawords2.sort(reverse = True)




#Extracting 20 words
print '%8s' %"Ranking"+ ' : Word'
print "===================="
for i in range(20):
    print "%8d :" %(i+1),emmawords2[i][1]
print "===================="



    
