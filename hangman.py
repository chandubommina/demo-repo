import random
words = ['anna','pope','mime','chandu','abacabac']
word = random.choice(words)
print(word)
blanks = []
for i in range(len(word)):
    blanks.append('_ ')
print(blanks)

end_of_game = False

while not end_of_game:
    guess = input().lower()
    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            blanks[position] = letter
            print(blanks)
    if '_ ' not in blanks:
        end_of_game = True
        print(blanks)



        