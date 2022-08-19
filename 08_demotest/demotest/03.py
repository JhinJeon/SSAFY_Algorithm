# 통역사 성경이
import sys
import re

sys.stdin = open('s3_input.txt')

t = int(input())

numbers = [str(i) for i in range(10)]
for tc in range(1,t+1):
    n = int(input())
    sentences = re.split('[!?.]', input())

    answer = []
    for i in range(n):
        sentence_test = list(sentences[i])
        name_count = 0
        for word in sentence_test:
            name_invalid = True
            if word.title() == word:
                for num in numbers:
                    if num in word:
                        break
                else:
                    name_invalid = False
            if not name_invalid:
                name_count += 1
        answer.append(name_count)

    print(f'#{tc}', *answer)