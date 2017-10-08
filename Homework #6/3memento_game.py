#21000348 AndreSeo
#Memento Game

from cs1graphics import *
import random, time

canvas = Canvas(540, 480)
canvas.setBackgroundColor("orange")
canvas.setTitle("Memento Games")


#Making Empty List
photos = []
cards = []
board = []





#Defining Functions
def initialize_cards_and_board(): #making setting of game
    for photo_id in range(12):
        if photo_id < 10:
            filename = "faces/face0" + str(photo_id) + ".jpg"
        else:
            filename = "faces/face" + str(photo_id) + ".jpg"
        photos.append(filename)# one photo id : two cards
        cards.append(photo_id)
        cards.append(photo_id)
    random.shuffle(cards) #shuffle factors in list (name=cards)
    for i in range(24):
        hidden = True
        board.append([cards[i], hidden]) #make list(name = board) with cards and condition(hidden or not)
        
def show_initial_screen(): #making game screen and cards with number 
    x0=50 #adding white space
    y0=60 #adding white space
    for index in range(24):
        i= int(index / 6)
        j=index % 6
        card = Rectangle(90,120)
        card.moveTo(x0 + 90*j, y0 + 120*i)
        canvas.add(card)
        number = Text(str(index))
        number.moveTo(x0 + 90*j, y0 + 120*i) #number is on center of card
        canvas.add(number)

def get_a_card(new): #taking number of card
    while True:
        if new == 1: #first card number
            card = input("Enter the 1st card number: ")
        else:
            card = input("Enter the 2nd card number: ")
        try: #checking if the type of entered number is integer
            card = int(card)
            return card
        except: #if not, next below line is printed
            print (card, ": invalid input")
        

def is_hidden(card):
    photo_id, hidden = board[card]
    return hidden


def is_valid(card1, card2): #checking the number entered is valid(scope, condition)
    if card1 < 0 or card1 > 23:
        return False #if the number is out of scope, the number is invalid
    elif card2 < 0 or card2 > 23:
        return False #if the number is out of scope, the number is invalid

    if is_hidden(card1) and is_hidden(card2): 
        return True
    return False


def add_to_layer(card, photo_id, layer): #showing image
    x0 = 50 # samesetup
    y0 = 60
    i = int(card / 6)
    j = card % 6
    filename = photos[photo_id] 
    photo = Image(filename) #image loading
    photo.move(x0 + 90*j, y0 + 120*i)
    layer.add(photo)
    return photo

def update_board(card): #no more hidden
    board[card][1]=False
##    photo_id, hidden = board[card]
##    board[card] = [photo_id, False]

def round_suffix(rnd): #input suffix after number of round
    if rnd ==1:
        return "st" #1st
    elif rnd ==2:
        return "nd" #2nd
    elif rnd ==3:
        return "rd" #3rd
    else:
        return "th" #4th


def main() :
    correct_pairs = 0
    round = 0 #count number of trials
    layer = Layer()
    layer.setDepth(40)
    canvas.add(layer)
    initialize_cards_and_board()
    show_initial_screen()

    while(correct_pairs <12):
        card1 = get_a_card(1) #taking number of card
        card2 = get_a_card(2) #taking number of card
        if card1 == card2: #if input same number
            print (card1, card2, "You choose the same card! Retry.")
        elif is_valid(card1, card2): #if valid is true, next statement is coming into action
            if check_cards(card1, card2, layer):
                print ("Great You got it.")
                correct_pairs +=1 #counting the number of correct pairs
            else:
                print ("Sorry! Try again.")
        else:
            print (card1, "or", card2, "is invalid.")

        round += 1
        print ("the " + str(round) + round_suffix(round) + " round" + ": ", correct_pairs, "correct pairs")

    print ("You are done! Your number of trials are ", round, ".")
            
   
#Staring Game
main()











