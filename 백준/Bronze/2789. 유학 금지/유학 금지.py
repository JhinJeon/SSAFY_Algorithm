forbidden = list('CAMBRIDGE')

word = list(input())

for w in range(len(word)):
    if word[w] in forbidden:
        word[w] = ''

    answer = ''.join(word)

print(answer.strip())