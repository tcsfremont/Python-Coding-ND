import sys

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

args = sys.argv[1:]

for arg in args:

    print(arg)

text = ' '.join(sys.argv[1:])
lowercase_letter = text[0].lower()

print(lowercase_letter)

lowercase_text = [letter.lower() for letter in text]

print(lowercase_text)

lowercase_text = ''.join(lowercase_text)
print(lowercase_text)
frequencies = {}

lowercase_text = [letter if letter in ALPHABET else '' for letter in lowercase_text]

print(lowercase_text)

lowercase_text = ''.join(lowercase_text)

for letter in ALPHABET:
    frequencies[letter] = 0

for letter in lowercase_text:


    frequencies[letter] += 1

print (frequencies)

for letter in ALPHABET:
    
    count = frequencies[letter]
    
    print(letter, end='')

    for c in range (count):
        
        print('|', end='')

    print()
