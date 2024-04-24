alphabets = [chr(i) for i in range(97,123)]+[chr(i) for i in range(97,123)]
direction = input('Type "encode" to encode and "decode" to decode \n').lower()
text = input('Type ur message \n')
shift = int(input('enter shift number \n'))

def encrypt(text,shift):
    encrypt_text = ''
    for i in text:
        position = alphabets.index(i)
        new_position = position+shift
        new_letter = alphabets[new_position]
        encrypt_text += new_letter
    print(encrypt_text)

if direction == 'encode':
    encrypt(text,shift)