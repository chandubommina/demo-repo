import random
from gamedata import data
import hllogo
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print(hllogo.logo)
score = 0
should_continue = True

    
def format_acc(account):
    account_name = account['name']
    account_dis = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_dis}, from {account_country}"
    

def check_ans(guess,a_follwers,b_follwers):
    if a_follwers > b_follwers :
        return guess == 'a'
    else :
        return guess == 'b'

b = random.choice(data)
while should_continue:
    a = b
    b = random.choice(data)
    if a == b:
        b = random.choice(data)

    print(f"compare A : {format_acc(a)}")
    print(hllogo.vs)
    print(f"against B : {format_acc(b)}")

    guess = input("who has more followers? type 'A' or 'B' : ").lower()
    #print(guess)
    #print(a['follower_count'])
    #print(b['follower_count'])
    a_follwers = a['follower_count']
    b_follwers = b['follower_count']
    #print(check_ans(guess,a_follwers,b_follwers))
    clear()
    print(hllogo.logo)
    is_correct = check_ans(guess,a_follwers,b_follwers)
    if is_correct :
        score += 1
        print(f"you are Right ! current score : {score}")
    else:
        should_continue = False
        print(f"you are Wrong ! final score : {score}")
