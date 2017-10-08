##21000348 Andre Seo
##Displaying Cards


import random
import time
from cs1graphics import*

class Table():
    def __init__(self): #table 이라는 클래스에 등록하면 아래 변수들이 생성되어 연결된다
        self.canvas = Canvas(1000, 600, "dark green", "Black Jack")  #canvas라는 변수를 Canvas라는 클래스에 등록
        ##테이블 레이아웃 잡느 
        self.x0 = 250 #x 시작점
        self.depth0 = 50 # 기본 깊이
        self.delta_x = 50 #x좌표의 변화값, 50씩 오른쪽으로 덮힌다
        self.delta_d = -5 #깊이의 변화값, 5씩 더 앞으로(-) 깊이가 얕아져 튀어나온다

        self.x = self.x0 #x좌표
        self.y = 80 #y좌표
        self.d = self.depth0 #깊이
        self.images = [] #이미지들을 담는 리스트 생성

    #Table 클래스에 등록되면 활용할 수 있는 함수들
    def display_card(self, card, x, y, d): #디스플레이 함수가 어디서 실행되는지 보면
        # card 한 장씩, 그리고 그 카드가 가져야 하는 x, y, d를 인수로 받음
        image = card.image #card라는 instance가 갖는 image라는 변수가 image에 저장되고, 
        self.images.append(image) #위의 images 리스트에 각각의 이미지가 저장된다
        image.setDepth(d) #뎁스 세팅
        image.moveTo(x,y) #x, y 좌표 반영
        self.canvas.add(image) #캔버스에 올려주기 
        time.sleep(0.3) #0.3초 간격 재면서 올려주기

    def show_label(self, where, label): ##플레이어 이름 보여주기
        text = Text() #Text라는 클래스의 text라는 개체 선언해주고
        y = 80+ where*120 #라벨의 위치 세팅 : 카드 위치의 중간
        text.setFontColor("white") # 폰트
        text.setFontSize(20) #사이
        text.moveTo(100,y) #위치 세팅
        text.setMessage(label) #텍스트에 레이블 달기
        self.canvas.add(text) #캔버스에 애드
        

    def increment_y(self): #호출되면 y 좌표를 120만큼 올리는 함수
        self.y += 120

    def clear(self):
        for image in self.images:
            self.canvas.remove(image)
        self.x = 100
        self.y = 80
        self.images = []
          

##카드 클래스
class Card(object): ##모든 모양과 숫자 리스트 생성. 리스트 타입의 클래스 변수
    #Card 클래스가 가지고 있는 멤버변수들 2개 (클래스에 등록하면 바로 쓸 수 있는)
    suit_name = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_name = [None, "Ace", "2", "3", "4", "5", "6", "7", "8",
                 "9", "10", "Jack", "Queen", "King"]

    
##    rank_name = [None, "Ace", "Two", "Three", "Four", "Five",
##                 "Six", "Seven", "Eight",
##                 "Nine", "Ten", "Jack",
##                 "Queen", "King"]


    ##Card 클래스에 등록하면 함께 실행되는 함수
    ##card = Card(모양, 숫자) 변수. card.rank card.suit 생성
    def __init__(self, suit = 0, rank = 1): #Card 객체는 두 가지 변수를 받는데,
        self.rank = rank
        self.suit = suit
        self.image = Image("BlackJack/" + Card.suit_name[suit] + "_" +
                           Card.rank_name[rank] + ".png")
        #줄여쓰면 Image("BlackJack/Space_Ace.png")와 같은 파일명
        

    ##print card시 클래스 변수에 접근하여 숫자와 of 모양 출력
    def __str__(self):
        return "%s of %s" % (Card.rank_name[self.rank],
                             Card.suit_name[self.suit])

    ##모양 먼저 비교, 숫자 비교
    def __lt__(self, other):
        if self.suit < other.suit:
            return True
        if self.suit > other.suit:
            return False
        if self.rank < other.rank:
            return True
        return False



##덱 클래스
class Deck(object):
    def __init__(self):
        self.cards = [] ##다섯개의 카드가 저장될 리스트
        for suit in range(4):
            for rank in range(1, 14):
                ##모든 숫자와 모양이 Card 클래스로부터 불려와 deck.cards 리스트에 저장
                card = Card(suit, rank)
                self.cards.append(card)

    ##print deck시 result라는 리스트에 
    def __str__(self):
        res = [] #공리스트
        for card in self.cards: #모든 카드들이 들어있는 리스트에서 하나의 카드씩 꺼내어
            res.append(str(card)) #해당 카드의 
        ##엔터를 사이사이에 끼워넣어 리턴
        return "\n".join(res)

    ##덱에서 맨마지막요소꺼내기(없애기)
    def pop_card(self):
        return self.cards.pop()

    ##덱에 카드 추가하기
    def add_card(self, card):
        self.cards.append(card)

    ##덱 리스트 요소 섞기
    def shuffle(self):
        random.shuffle(self.cards)

    ##덱에서 꺼낸 카드 핸드에 추가하기
    ##5장의 카드 hand에 추가(셔플하여 마지막에 있는 카드 5장)
    def move(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card()) #p마지막 카드 5장을 pop시켜서 a

    ##4명의 손에 5장의 카드 
    def deal_hands(self, num_hands, num_cards):
        hands = []
        for i in range(num_hands):
            hand = Hand()
            ##move메소드가 나와야 비로소 5장 갖게 된다
            self.move(hand, num_cards)
            ##hands라는 중첩리스트 안에 5장씩 가진 손들이 추가된다
            hands.append(hand)
        return hands

    def show_cards(self, table):
        x = table.x0
        y = table.y
        d = table.depth0
        for card in self.cards:
            table.display_card(card, x, y, d) #카드 한장씩 넘어가고, x좌표와 깊이가 업데이트 된다
            x += table.delta_x
            d += table.delta_d
        table.increment_y()

        

##Deck 클래스 상속
class Hand(Deck):
    ##cards와 레이블을 받음
    def __init__(self, label=" "):
        self.cards = []
        self.label = label
        
    def print_label(self):
        print (self.label)








def main():
    table = Table() #Table이라는 클래스에 table 등록


    ##전체 deck 생성(52장)
    deck = Deck() #Deck이라는 클래스에 deck 등록


    ##셔플
    deck.shuffle() 
    
    labels = []
    for i in range(4):
        label = "Card Player %1d" %(i+1) #레이블 작성
        table.show_label(i, label) #레이블 보이기
        hand = Hand(label) #hand 클래스 객체 생성 
        deck.move(hand, 5) #Deck의 move 함수... hand로 5개의 카드를 옮겨옴
        hand.show_cards(table) #hand에 있는 카드를 보여줌
        time.sleep(1)
##    table.clear()
    
##    ##4명에서 5장씩 딜링(리스트)
##    hands = deck.deal_hands(4,5)
##    for hand in hands:
##        print "\n", hand



##메인프로그램
main()





    






    
