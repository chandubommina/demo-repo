alphabets = [chr(i) for i in range(97,123)]+[chr(i) for i in range(97,123)]
direction = input('Type "encode" to encode and "decode" to decode \n').lower()
text = input('Type ur message \n').lower()
shift = int(input('enter shift number \n'))

#to handle any shift lenght
shift = shift % 26

flag = True
while flag:
    def caesar(text,shift,direction):
        caesar_text = ''
        for i  in text:
            #to handle symbols,numbers,spaces,etc
            if i in alphabets:
                position = alphabets.index(i)
                if direction == 'encode':
                    new_position = position+shift
                    new_letter = alphabets[new_position]
                    caesar_text += new_letter
                else:
                    new_position = position-shift
                    new_letter = alphabets[new_position]
                    caesar_text += new_letter
            else:
                caesar_text += i
        print(caesar_text)
        
    caesar(text,shift,direction) 

    #to play continuously
    play = input("do u want to play again ? type 'yes' or 'no'").lower()
    if play == 'yes':
        direction = input('Type "encode" to encode and "decode" to decode \n').lower()
        text = input('Type ur message \n').lower()
        shift = int(input('enter shift number \n'))
        flag = True
    else:
        flag = False
        print("good bye!")