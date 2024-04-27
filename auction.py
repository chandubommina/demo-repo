#auction
bids = {}
bidding_finished = False

def highest_bidder(bidding_record):
    
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        bidding_amount = bidding_record[bidder]
        if bidding_amount > highest_bid:
            highest_bid = bidding_amount
            winner = bidder
    print(f"winner is {winner} with bidding amount {highest_bid}")

while not bidding_finished:
    name = input("enter your name: ")
    bid = int(input("enter your bid: "))
    bids[name] = bid
    other_bidders = input("are there any other bidders type yes or no ?")
    if other_bidders == "no":
        bidding_finished = True
        highest_bidder(bids)


