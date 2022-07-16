words = 'abcdefghijklmnop'
for i, letter in enumerate(words):
    if i > 0 and i % 6 == 0:
        print()
    print(letter,end='')