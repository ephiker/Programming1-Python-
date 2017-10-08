##21000348 Andre Seo
##Generalizing


import random, time, sys
from cs1graphics import *


suit_name = ["Clubs", "Diamonds", "Hearts", "Spades"]

rank_name = { "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8,
              "9":9, "10":10, "Jack":10, "Queen":10, "King":10, "Ace":11}

canvas = Canvas (1000, 600, 'dark green','Black Jack')


##테이블 클래스
class Table():
    def __init__(self):
        self.x0 = 300
        self.depth0 = 100
        self.delta_x = 50
        self.delta_d = -5
        self.player_x = []#플레이어 수
        self.player_d = []#플레이어 수

        self.dealer_y = 80
        self.player_y =200

        ##메시지와 퀘스트 배치
        self.message = Text()#텍스트 클래스의 인스턴스 생성
        self.message.setFontColor('red')
        self.message.setFontSize(20)
        self.message.moveTo(canvas.getWidth() / 2 - 50, canvas.getHeight() -80) #중심 위치 : 중앙에서 왼편, 맨 아랫쪽 살짝 위
        canvas.add(self.message)
        
        self.question = Text()#텍스트 클래스의 인스턴스 생성
        self.question.setFontColor('white')
        self.question.setFontSize(20)
        self.question.moveTo(canvas.getWidth() / 2 - 50, canvas.getHeight() - 40) #중심 위치 : 중앙에서 왼편, 맨 아랫쪽 살짝 위
        canvas.add(self.question)

        self.PLAYERS = self.set_game()
        

        for i in range(self.PLAYERS): #플레이어 수
            self.player_x.append(self.x0)
            self.player_d.append(self.depth0)

        self.scores = []
        self.labels = []
        self.hands = []

        self.question.setMessage(" ")

        
        for i in range(self.PLAYERS):
            ##라벨 이름
            if i == self.PLAYERS-1: #플레이어 수
                label = "Dealer"
            else:
                label = "Player %1d" %(i + 1)

            ##라벨 위치
            if i == self.PLAYERS-1:
                y = 80
            else:
                y = 200+i*120
                
            self.display_label(label, y)
            

            ##스코어
            score = Text() ##텍스트 클래스 인스턴스 생성
            score.setFontColor('white')
            score.setFontSize(20)
            score.moveTo(canvas.getWidth() - 100, y)
            canvas.add(score)
            self.scores.append(score)

            ##플레이어별 패
            hand = Hand() ##핸드 클래스 인스턴스 생성
            self.hands.append(hand)

    def set_game(self):
        self.question.setMessage("How many persons? ")
        while True:
            event = canvas.wait()
            response = event.getDescription()
            if response == "canvas close":
                sys.exit(1)
            if response == "keyboard":
                key = event.getKey()
                if key > "1" and key < "5":
                    self.question.setMessage("number of players: " + key)
                    key = int(key)
                    return key
                else:
                    self.question.setMessage(key + "? Type in a number between 2 and 4 inclusively.")

    def display_label(self, label, y):
        player_label = Text()
        player_label.setFontColor("white")
        player_label.setFontSize(20)
        player_label.moveTo(100, y)
        canvas.add(player_label)
        player_label.setMessage(label)
        self.labels.append(player_label) #리스팅

    def clear_label(self):
        for label in self.labels:
            label.setMessage(" ") #공백으로 변환

    def clear_texts(self):
        canvas.remove(self.message)
        canvas.remove(self.question)

    def set_score(self, score, who):
        text = "%3d" % score
        self.scores[who].setMessage(text)

    def show_message(self, text):
        self.message.setMessage(text)
        time.sleep(3)

    def ask_response(self, prompt):
        self.question.setMessage(prompt)
        while True:
            event = canvas.wait()
            response = event.getDescription()
            if response == "canvas close":
                sys.exit(1)
            key = "An unexpected event"
            if response == "keyboard":
                key = event.getKey()
                if key == 'y':
                    self.question.setMessage(" ")
                    return True
                if key == 'n':
                    self.question.setMessage(" ")
                    return False
                else:
                    self.question.setMessage(key + "? I beg your pardon.")
            else:
                self.question.setMessage(key)

    def start_new(self, prompt):
        self.question.setMessage(prompt + "(y/n)")
        while True:
            event = canvas.wait()
            response = event.getDescription()
            if response == "canvas close":
                sys.exit(1)
                #return False
            if response == "keyboard":
                key = event.getKey()
                if key == 'y':
                    self.question.setMessage(" ")
                    return True
                elif key == 'n':
                    self.question.setMessage(" ")
                    return False
##                else:
                    
            self.question.setMessage(key + "I beg your pardon.")

    def clear(self):
        for i in range(self.PLAYERS):#플레이어 수
            self.player_x[i] = self.x0
            self.player_d[i] = self.depth0
            self.scores[i].setMessage(" ")
            for image in self.hands[i].images:
                canvas.remove(image)
            self.hands[i].images = []
            self.hands[i] = Hand()

    def show_card(self, card, who):
        if who == self.PLAYERS-1: #플레이어 수
            image = self.display_card(card, self.player_x[self.PLAYERS-1], self.dealer_y, self.player_d[self.PLAYERS-1])#플레이어 수
        else:
            y = self.player_y + who * 120
            image = self.display_card(card, self.player_x[who], y, self.player_d[who])
        self.player_x[who] += self.delta_x
        self.player_d[who] += self.delta_d
        self.hands[who].images.append(image)

    def open_hcard(self, hand):
        card = hand.cards[0]
        card.update_state(False)
        image = self.display_card(card, self.x0, self.dealer_y, self.player_d[self.PLAYERS-1])#플레이어 수
        self.hands[self.PLAYERS-1].images.append(image)#플레이어 수
        return card

    def display_card(self, card, x, y, d):
        if card.hidden:
            image = Image("./BlackJack/" + "Back.png")
        else:
            image = card.image
        image.setDepth(d)
        image.moveTo(x, y)
        canvas.add(image)
        time.sleep(1)
        return image

    def close(self):
        canvas.close()

class Card(object):
    def __init__(self, suit="Clubs", rank = "2"):
        self.rank = rank
        self.suit = suit
        self.value = rank_name[rank]
        self.image = Image("./BlackJack/" + suit + "_" + rank + ".png")
        self.hidden = False

    def __str__(self):
        article = "a "
        if self.rank in ("8", "Ace"):
            article = "an "
        return article + self.rank + " of " + self.suit

    def update_state(self, hidden):
        self.hidden = hidden

class Deck(object):
    """A deck of cards."""
    def __init__(self):
        """Create a deck of 52 cards and shuffle them."""
        self.cards = []
        for suit in suit_name:
            for rank in rank_name:
                card = Card(suit, rank)
                self.cards. append(card)

    def shuffle(self):
        random.shuffle(self.cards)
        return(self)

    def draw(self):
        card = self.cards.pop()
        return card

    def move_card(self, hand, hidden = False):
        card = self.draw()
        hand.add(card, hidden)
        return card


class Hand(Deck):
    def __init__(self):
        self.cards = []
        self.images = []

    def add(self, card, hidden):
        if hidden:
            card.update_state(hidden)
        self.cards.append(card)

    def hand_value(self):
        value = 0
        for card in self.cards:
            value += card.value
        return value

    def clear(self):
        for item in self.card:
            self.cards.remove(item)

def first_two_cards(deck, table):
    for j in range(2):
        for i in range(table.PLAYERS):#플레이어 수
            hand = table.hands[i]
            if j == 0 and i == table.PLAYERS-1:#플레이어 수
                card = deck.move_card(table.hands[i], True)
            else:
                card = deck.move_card(table.hands[i])
            table.show_card(card, i)
                





def players_turn(deck, table):
    tval = [0]*table.PLAYERS#플레이어 수
    all_lost = True
    for i in range(table.PLAYERS-1):#플레이어 수
        tval[i] = table.hands[i].hand_value()
        table.set_score(tval[i], i)
        while tval[i] <21:
            msg = "Player %1d, " %(i+1) + "would you like to have another card? (y/n) "
            if not table.ask_response(msg):
                break
            card = deck.move_card(table.hands[i])
            table.show_card(card, i)
            tval[i] += card.value
            table.set_score(tval[i], i)

        if tval[i] > 21:
            msg = "Player %1d, " %(i+1) + "you went over 21! You lost!"
            table.show_message(msg)
            msg = " "
            table.show_message(msg)
        else:
            all_lost = False
        time.sleep(1)
    return tval, all_lost


def dealers_turn(deck, tval, table):
    card = table.open_hcard(table.hands[table.PLAYERS-1])#플레이어 수
    tval[table.PLAYERS-1] = table.hands[table.PLAYERS-1].hand_value()#플레이어 수
    table.set_score(tval[table.PLAYERS-1], table.PLAYERS-1)#플레이어 수
    while tval[table.PLAYERS-1] < 17 and tval[table.PLAYERS-1] <= min(tval[0:3]):#플레이어 수
        card= deck.move_card(table.hands[table.PLAYERS-1])#플레이어 수
        table.show_card(card, table.PLAYERS-1)#플레이어 수
        tval[table.PLAYERS-1] += card.value#플레이어 수
        table.set_score(tval[table.PLAYERS-1], table.PLAYERS-1)#플레이어 수
    return tval


def conclude_the_game(tval, table):
    for i in range(table.PLAYERS-1): #플레이어 수
        if tval[i] > 21:
            msg = "you went over 21! You Lost!"
        elif tval[table.PLAYERS-1] > 21: #플레이어 수
            msg = "the dealer went over 21! You won!"
        elif tval[table.PLAYERS-1] < tval[i]:#플레이어 수
            msg = "you won!"
        elif tval[table.PLAYERS-1] > tval[i]:#플레이어 수
            msg = "you lost!"
        else:
            msg = "You had a tie!"
        msg = "Player %1d, " %(i+1) + msg
        table.show_message(msg)
    table.clear()

    
def blackjack(table):
    deck = Deck()
    deck.shuffle()
    first_two_cards(deck, table)
    tval, all_lost = players_turn(deck, table)
    if all_lost:
        table.clear()
        return
    dealers_turn(deck, tval, table)
    conclude_the_game(tval, table)


def game_loop():
    table = Table()
    while True:
        blackjack(table)
        if table.ask_response("Play another round? (y/n) "):
            pass
        else:
            table.clear_label()
            if table.start_new("Start with new persons?"):
                table.clear_texts()
                table = Table()
            else:
                break
            
    table.close()


##테이블 클래스에 인스턴스 생성

game_loop()






















