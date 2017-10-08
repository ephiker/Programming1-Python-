##Blackjack Game
##21000348 Andre Seo
##Black1

from cs1graphics import*
import random, time

RANKS = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8,
         "9" : 9, "10" : 10, "Jack" : 10, "Queen" : 10, "King" : 10, "Ace" : 11}
SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

class Table(object):
    def __init__(self):
        self.canvas = Canvas(600,400,'dark green','Black Jack')
        self.x0 = 100
        self.dealer_y = 100
        self.player_y = 300
        self.delta_x = 50
        self.dealer_x = self.x0
        self.player_x = self.x0
        self.delta_x
        self.depth0 = 100
        self.delta_d = -5
        self.dealer_d = self.depth0
        self.player_d = self.depth0

        self.dealer_s = Text()
        self.dealer_s.setFontColor('white')
        self.dealer_s.setFontSize(10)
        self.dealer_s.moveTo(self.canvas.getWidth()-100, self.dealer_y)
        self.canvas.add(self.dealer_s)

        self.player_s = Text()
        self.player_s.setFontColor('white')
        self.player_s.setFontSize(10)
        self.player_s.moveTo(self.canvas.getWidth()-100, self.player_y)
        self.canvas.add(self.player_s)

        self.images = []

    def set_score(self, score, dealer = False):
        text  = "%3d" % score
        if dealer:
            self.dealer_s.setMessage("Dealer's score: " + text)
        else:
            self.dealer_s.setMessage("Your score: " + text)

    def show_card(self, card, dealer = False):
        if dealer:
            card.display_card(self, self.dealer_x, self.dealer_y, self.dealer_d)
            self.dealer_x += self.delta_x
            self.dealer_d += self.delta_d
        else:
            card.display_card(self, self.player_x, self.player_y, self.player_d)
            self.player_x += self.delta_x
            self.player_d += self.delta_d

    def clear(self):
        """Close the table to end playing."""
        self.dealer_x = self.x0
        self.player_x = self.x0
        self.dealer_d = self.depth0
        self.player_d = self.depth0
        self.dealer_s.setMessage("")
        self.player_s.setMessage("")
        for image in self.images:
            self.canvas.remove(image)
        self.images = []


class Card(object):
    def __init__(self, rank, suit):
        assert(rank in RANKS and suit in SUITS)
        img_path = "./BlackJack/"
        self.rank = rank
        self.suit = suit
        self.value = RANKS[rank]
        self.image = Image(img_path + suit + "_" + rank + ".png")
        self.hidden = False

    def __str__(self):
        article = "a "
        if self.rank in ("8", "Ace"):
            article = "an "
        return article + self.rank + " of " + self.suit

    def update_state(self, hidden):
        self.hidden = hidden

    def display_card(self, table, x, y, d):
        if self.hidden:
            image = Image("./BlackJack/" + "Back.png")
        else:
            image = self.image
        image.setDepth(d)
        image.moveTo(x, y)
        table.canvas.add(image)
        table.images.append(image)
        time.sleep(1)
        return image

class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)
        return(self)

    def draw(self):
        card = self.cards.pop()
        return card

    def move_card(self, other, dealer = False):
        card = self.draw()
        hidden = False
        if dealer and len(other.cards) == 0:
            hidden = True
        other.add(card, hidden)
        return card


class Hand(Deck):
    def __init__(self, dealer = False):
        self.cards = []
        self.dealer = dealer

    def add(self, card, hidden = False):
        if hidden:
            card.update_state(hidden)
        self.cards.append(card)

    def open_hcard(self, table):
        card = self.cards[0]
        card.update_state(False)
        card.display_card(table,table.x0, table.dealer_y, table.dealer_d)
        time.sleep(1)
        return card

    def hand_value(self):
        value = 0
        for card in self.cards:
            value += card.value
        return value

def take_response(prompt):
    while True:
        user_input = input(prompt)

        if user_input =="y":
            return True
        elif user_input == "n":
            return False
        else:
            print ("I beg your pardon! Enter (y/n)")

def initial_two_cards(deck, player, dealer, table):
    card = deck.move_card(player)
    table.show_card(card)
    print ("You are dealt", card)

    card = deck.move_card(dealer, True)
    table.show_card(card, True)
    print ("Dealer is dealt a hidden card")

    card = deck.move_card(player)
    table.show_card(card)
    print ("You are dealt"), card

    card = deck.move_card(dealer, True)
    table.show_card(card, True)
    table.set_score(player.hand_value())
    print ("Dealer is dealt"), card
    print ("Your total is"), player.hand_value()

def players_turn(deck, player, table):
    while player.hand_value() < 21:
        if not take_response("Would you like another card? (y/n)"):
            break
        card = deck.move_card(player)
        table.show_card(card)
        table.set_score(player.hand_value())
        print ("You are dealt", card)
        print ("Your total is", player.hand_value())
        
    if player.hand_value() > 21:
        print ("You went over 21! You lost!")
        return True
    return False

def dealers_turn(deck, player, dealer, table):
    card = dealer.open_hcard(table)
    print ("Dealer's hidden card was", card)
    print ("Dealer's total is", dealer.hand_value())
    table.set_score(dealer.hand_value(), True)
    while dealer.hand_value() < 17 and dealer.hand_value() <= player.hand_value():
        card = deck.move_card(dealer, True)
        table.show_card(card, True)
        table.set_score(dealer.hand_value(), True)
        print ("Dealer are dealt", card)
        print ("Dealer's total is", dealer.hand_value())

def conclude_the_game(player, dealer):
    player_total = player.hand_value()
    dealer_total = dealer.hand_value()
    if player_total > 21:
        return
    if dealer_total > 21:
        print ("The dealer went over 21! You win!")
        return
    print ("\nYour total is", player_total)
    print ("The dealer's total is", dealer_total)

    if player_total > dealer_total:
        print ("You win!")

    elif player_total < dealer_total:
        print ("You lost!")
    else:
        print ("You have a tie!")

def blackjack(table):

    deck = Deck()
    deck.shuffle()
    dealer = Hand(True)
    player = Hand()

    initial_two_cards(deck, player, dealer, table)
    already_lost = players_turn(deck, player, table)
    if not already_lost:
        dealers_turn(deck, player, dealer, table)
    conclude_the_game(player, dealer)

def game_loop():
    print ("Welcome to Blackjack!")
    table = Table()
    while True:
        blackjack(table)
        time.sleep(7)
        table.clear()
        if not take_response("\nPlay another round? (y/n) "):
            break

game_loop()



    
        










            
