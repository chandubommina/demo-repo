import random
words = ['anna','pope','mime','chandu','abacabac']
word = random.choice(words)

blanks = []
for i in range(len(word)):
    blanks.append('_ ')
print(f"{' '.join(blanks)}")
lives = 5
end_of_game = False
while not end_of_game:
    guess = input().lower()
    if guess in blanks:
        print(f'u already guessed {guess}')
    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            blanks[position] = letter
            print(f"{' '.join(blanks)}")
            
    if guess not in word:
        print(f'{guess} not in word, you lost a life.')
        lives = lives-1
        if lives == 0:
            end_of_game = True
            print('you lost')
            print(f'word is {word}')
    if '_ ' not in blanks:
        end_of_game = True
        print('you win')
        print(f"{' '.join(blanks)}")
