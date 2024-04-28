import random

def deal_card():
    """returns one random card from deck when called"""
    deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(deck)
   
def cal_scores(cards):
    """takes list of cards and returns sum of cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


#print(dealer_score)
#print(f"your cards : {player} and score : {player_score}")

def compare(p,d):
    """takes two scores and compares them"""
    if p > 21 and d > 21 :
        print("u went over and lost")
    if p == d :
        print("draw")
    elif d == 0 :
        print("u lost! dealer black jack")
    elif p == 0 and d != 0 :
        print("win! black jack")
    elif p > 21:
        print("you went over and lost")
    elif p > d:
        print("win")
    else :
        print("win")

def is_play(): 
    player = []
    dealer = []
    is_game_over = False

# deal 2 random cards each to dealer and player
    for i in range(2):
        player.append(deal_card())
        dealer.append(deal_card())
    while not is_game_over:
        dealer_score = cal_scores(dealer)
        player_score = cal_scores(player)
        
        print(f"your cards are {player} and current score {player_score}")
        print(f"dealer first hand card {dealer[0]}")
            
        if dealer_score == 0 or player_score == 0:
            is_game_over = True
        else:
            deal = input("deal card 'y' yes or 'n' for no : ").lower()
            
            if deal == 'y':
                player.append(deal_card())
                player_score = cal_scores(player)
            else:
                is_game_over = True

    while dealer_score < 17 and dealer_score != 0:
        dealer.append(deal_card())
        dealer_score = cal_scores(dealer)

    print(f"your cards are {player} and final score {player_score}")
    print(f"dealer cards are {dealer} and final score {dealer_score}")
    compare(player_score,dealer_score)
    

while input(" do u want play black jack ? type 'y' or 'n' : ") == 'y':
    is_play()
    