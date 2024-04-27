#automate pizza order

print("thank u for choosing python pizza")
size = input("pizza ? s or m or l: ")
add_pepporini = input("add pepporini ? y or n: ")
add_cheese = input(" add extra cheese? y or n: ")
bill = 0
if size == 's':
    bill += 15
    if add_pepporini == 'y':
        bill = bill + 2
    if add_cheese == 'y':
        bill = bill + 1
elif size == 'm':
    bill += 20
    if add_pepporini == 'y':
        bill = bill + 3
    if add_cheese == 'y':
        bill = bill + 1
else:
    bill += 25
    if add_pepporini == 'y':
        bill = bill + 3
    if add_cheese == 'y':
        bill = bill + 1    
print(f"ur final bill is {bill}")
