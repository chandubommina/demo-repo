import random

EASY_LEVEL_TURNS = 10
HARDL_LEVEL_TURNS = 5

def check_answer(number,guess,turns):
    if guess > number :
        print("to high !")
        return turns-1
    elif guess < number :
        print("to low !")
        return turns-1
    else:
        print(f"you got it ! number is {number}")
        
def set_difficulty():
    level = input("choose difficulty. hard or easy ? ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARDL_LEVEL_TURNS
    
    
def game():    
    
    print("welcome number guessing game!")
    print("i am thinking of number between 1 and 100 .")
    number = random.randint(1,100)
    print(f"number {number}")
    turns = set_difficulty()
    guess = 0

    while guess != number:
        print(f"u have {turns} attempts remaining to guess the number")
        guess = int(input("make a guess : "))
        turns = check_answer(number,guess,turns)
        if turns == 0:
            print("u ran out of guesses, u lose.")
            return
        elif guess != number :
            print("guess again.")

game()        