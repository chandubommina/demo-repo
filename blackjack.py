import random

def deal_card():
    """returns one random card from deck when called"""
    deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(deck)

player = []
dealer = []
is_deal = True

# deal 2 random cards each to dealer and player
for i in range(2):
    player.append(deal_card())
    dealer.append(deal_card())
    
print(f"dealer {dealer}")
print(f"player {player}")
print(f"dealer first hand card {dealer[0]}")

def cal_scores(cards):
    """takes list of cards and returns sum of cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    return sum(cards)

dealer_score = cal_scores(dealer)
player_score = cal_scores(player)

#print(dealer_score)
#print(f"your cards : {player} and score : {player_score}")

def compare(p,d):
    """takes two scores and compares them"""
    if d == 0 :
        print("u lost! dealer black jack")
    elif p == 0 and d != 0 :
        print("win! black jack")
    elif p > 21:
        print("you went over and lost")
    elif d > 21:
        print("win! dealer went over and lost")
    elif p > d:
        print("win")
    elif p == d:
        print("draw")
    elif d > p :
        print("lost")

    
while is_deal:
    print(f"your cards are {player} and current score {player_score}")
    deal = input("deal card 'y' yes or 'n' for no : ").lower()
    if deal == 'y':
        player.append(deal_card())
        player_score = cal_scores(player)

    else:
        is_deal = False

while dealer_score < 17:
    dealer.append(deal_card())
    dealer_score = cal_scores(dealer)
    
print(f"your cards are {player} and final score {player_score}")
print(f"dealer cards are {dealer} and final score {dealer_score}")
compare(player_score,dealer_score)
    