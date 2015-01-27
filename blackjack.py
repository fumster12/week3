# Game of Blackjack by Funmi Dosunmu 1/27/15

## Get a deck of cards

import random

SUITS = "\u2663 \u2665 \u2666 \u2660".split()
FACES = "A 2 3 4 5 6 7 8 9 10 J Q K".split()

deck = []
for suit in SUITS:
  for face in FACES:
    deck.append(face+suit)

## Shuffle the deck

random.shuffle(deck)

def calculate_score(cards):
  value = 0
  for card in cards:
    face = card[:-1]
    if face in ['J', 'Q', 'K']:
      points = 10
    elif face == 'A':
      points = 11
    else:
      points = int(face)
    value += points
  return value

## Deal the first two cards to user

hand = [deck.pop(0), deck.pop(0)]
score = calculate_score(hand)

print("Your hand is:", " ".join(hand), "\nYou have:", score, "points")


## User can choose to take cards as long as score < 21

while score < 21 and input("Do you want another card? (yes/no)") == "yes":
  hand.append(deck.pop(0))
  score = calculate_score(hand)
  print("Your hand is:", " ".join(hand), "\nYou have:", score, "points")
  
## If user goes over 21, game is over.
  
if score > 21:
  print("You're busted!")


## If user reaches 21, game is over.


elif score == 21:
  print("You Won!")


## If user stands with less than 21, then it's the dealer's turn:
  
else:
  print("You have:", score, "points")
  print()
  

##    Computer takes two cards
  
  dealer = [deck.pop(0), deck.pop(0)]
  dealer_score = calculate_score(dealer)
  print("Dealer's hand", " ".join(dealer), "\nDealer has:", dealer_score, "points")

##    Computer must take more cards while computer score < 17
  
  while dealer_score < 17:
    print("Dealer will take another card")
    dealer.append(deck.pop(0))
    dealer_score = calculate_score(dealer)
    print("Dealer's new hand is:", " ".join(dealer), "\nDealer has", dealer_score, "points")

##    If computer score reached 21, computer wins.
    
  if dealer_score == 21:
    print("Dealer Won.") 
  
  
##    If computer score goes over 21, computer loses.
    
  elif dealer_score  > 21:
    print("Dealer Busted, You Won!")
    
##    If computer score is 17 to 20, winner is determined by higher score.
    
  elif dealer_score > score:
    print("Dealer Won")
    

  elif dealer_score == score:
    print("It's a tie.")
    
  else:
    print("Dealer has:", dealer_score, "points. \nYou Won")
  
           
      
    

