import random

letters = [chr(i) for i in range(97,123)]+[chr(i) for i in range(65, 91)]
numbers = [str(i) for i in range(0,10)]
symbols = ['!','#','$','%','&','(',')','*','+']

print("welcome to password generartor! ")

num_letters = int(input("how many letter would u like in ur password? "))
num_numbers = int(input("how many numbers ? "))
num_symbols = int(input("how many symbols ? "))

rand_letters = random.sample(letters,num_letters)
rand_numbers = random.sample(numbers,num_numbers)
rand_symbols = random.sample(symbols,num_symbols)

password_list = rand_letters+rand_numbers+rand_symbols

rand_password = random.sample(password_list,len(password_list))


password = ''  
for i in rand_password:
    password = password+i
print(f"ur password is :  {password}")
