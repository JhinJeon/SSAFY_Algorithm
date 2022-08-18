# 유학 금지

# replace() 활용 버전

# 입력받은 단어
word = input()

# 입력받은 단어의 개별 문자가 금지할 문자열 리스트 안에 포함되어 있는지 확인
for w in 'CAMBRIDGE':
    # 만약 금지어라면 해당 문자를 공백으로 대체
    if w in word:
        word = word.replace(w,'')

print(word)