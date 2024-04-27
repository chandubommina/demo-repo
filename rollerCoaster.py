#nested if else:roller coaster

ht = int(input("ur age in cm? "))
if ht >= 120:
    print("u can ride roller coaster")
    age = int(input("ur age? "))
    bill = 0
    if age < 18:
        bill = 5
        print("child tickets are 5")
    elif age >= 45 and age <= 55:
        print("u are going through mid life crisis.have a free ticket")      
    else:
        bill = 10
        print("adult tickets are 10")
    photo = input("do u want photo ? type y or n ")
    if photo == 'y':
        bill = bill + 3
    print(f"ur final bill is {bill}")
else:
    print("sorry! u can not ride")