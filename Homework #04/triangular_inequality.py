#21000348 AndreSeo
#triangular inequality



#Defining functions
def user_input(side):
    while True:
        try: #preparing for exception
            message = "Enter the length side %3d: " %side
            number = input(message)
            converted_number = float(number)
            return converted_number
        
        except:
            print (number + "? " + "Please enter a number.")
            

def take_length():
    x = user_input(1)
    y = user_input(2)
    z = user_input(3)
    return x, y, z



def inequality(x, y, z): #checking triangular inequality and printing
    if (x+y>z and y+z>x and z+x>y):
        print (x, y, z, "Triangle!")
    else:
        print (x, y, z, "False!")


def main():
    while True:
        a, b, c = take_length()
        inequality(a, b, c)

        #condition for repeating or escaping
        answer = input("Go for a more check? (If you want, type 'yes') ")
        if answer != "yes":
            break 


#Main function
print ("This is Triangular-Inequality Program!\n")
main()
