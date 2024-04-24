alphabets = [chr(i) for i in range(97,123)]+[chr(i) for i in range(97,123)]
direction = input('Type "encode" to encode and "decode" to decode \n').lower()
text = input('Type ur message \n')
shift = int(input('enter shift number \n'))

def caesar(text,shift,direction):
    caesar_text = ''
    for i  in text:
        position = alphabets.index(i)
        if direction == 'encode':
            new_position = position+shift
            new_letter = alphabets[new_position]
            caesar_text += new_letter
        else:
            new_position = position-shift
            new_letter = alphabets[new_position]
            caesar_text += new_letter            
    print(caesar_text)
caesar(text,shift,direction) 