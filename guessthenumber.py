import random

print("welcome to number guessing game")
print("i m thinking of number between 1 to 100.")

number = random.randint(1,100)

level = input("choose difficulty level! easy,hard : ")

if level == 'hard':
    attempts = 5
else:
    attempts = 10
    
print(f"you have {attempts} attempts to guess the number ")

def compare(x,y):
    global attempts
    if x == y:
        print(f"won number is {number}")
        attempts = 0
    elif x > y :
        attempts -= 1
        if attempts >0:
            print("too high! guess again")
            print(f"you have {attempts} attempts remaining")
        else:
            print(f"u lost! number is {number}")
            print(f"you have {attempts} attempts remaining")            
    elif x < y :
        attempts -= 1
        if attempts > 0:
            print("too low! guess again")
            print(f"you have {attempts} attempts remaining")
        else:
            print(f"u lost! number is {number}")
            print(f"you have {attempts} attempts remaining")
    
while attempts > 0:
    guess_number = int(input("Make a guess : "))
    compare(guess_number,number)    