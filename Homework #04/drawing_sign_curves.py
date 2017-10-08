#21000348 AndreSeo
#drawing_sign_curves
import math





##사인그래프 규격 -1~1에서 0~80으로
##각도 0~2pi를 40으로 쪼개서 한줄씩 반복
##해당 각도를 sin에 넣고 그 값을 규격화,근사하여 출력

        

########################################
##############################################


##def compute(angle):
##    num = math.sin(angle)*40 + 40
##    return int(num)
##
##
##
##while True:
##    #Choosing type of graph        
##    n = input("1:Bar Graph, 2:Point Graph : ")
##
##
##    ##### 1.Bar Graph #####
##    if (n == '1'): 
##        for i in range (41): 
##            angle = 2*(math.pi)/40 * float(i) #angle of sine function
##            number = compute(angle) #number of '#'
##            print ('#'*number)
##
##        print ('\n'*3)
##        
##
##    ##### 2.Point Graph #####
##    elif (n == '2'):
##        for i in range (41):
##            angle = 2*(math.pi)/40 * float(i) #angle of sine function
##            number = compute(angle) #number of '#'
##                
##            if (0<i<20): 
##                print ((' '*39) + '|' + (' '*(number-41)) + '#')
##
##            elif (i == 20): #horizontal axis
##                print (('-'*39) + ('#') + ('-'*40))
##                
##            elif (20<i<40):
##                print ((' '*(number)) + '#' + (' '*(39-(number+1))) + '|')
##                
##            else: #when i is 0 and 40
##                print ((' '*39) + '#')
##
##        print ('\n'*3)
##        
##
##    ##### Re-enter number #####
##    else:
##        print ("Please enter 1 or 2") 



def compute_and_plot1(x):
    sharp = math.sin(x)*40 + 40
    sharp = int(sharp)
    print (sharp*'#')

def compute_and_plot2(x):
    blank = math.sin(x)*40 + 40
    blank = int(blank)

    if x<math.pi:
        print(" "*40 + "!" + " "*(blank-39) + "*") ## -39개인 이유는 39개+마지막 별표 한개를 해야 40이기 때문이다

    elif x == math.pi:
        print("="*40 + "*" + "="*40)

    else:
        print(" "*blank + "*" + " "*(39-blank) + "!")
    


while True:
    n = input("1:Bar Graph, 2:Point Graph : ")

    ##### 1.Bar Graph #####
    if (n == '1'):
        for i in range(0, 41):
            angle = (2*math.pi / 40) * float(i)
            compute_and_plot1(angle)


    ##### 2.Point Graph #####
    elif (n == '2'):
        for i in range(0, 41):
            angle = (2*math.pi / 40) * float(i)
            compute_and_plot2(angle)

            


