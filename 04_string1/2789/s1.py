# 유학 금지

# 금지할 문자열 리스트
forbidden = list('CAMBRIDGE')

# 입력받은 단어
word = list(input())

# 입력받은 단어의 개별 문자가 금지할 문자열 리스트 안에 포함되어 있는지 확인
for w in range(len(word)):
    # 만약 금지어라면 해당 문자를 공백으로 대체
    if word[w] in forbidden:
        word[w] = ''

    # 공백을 붙여서 출력
    answer = ''.join(word)

print(answer.strip())