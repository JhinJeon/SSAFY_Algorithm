# 순열 문제

import sys
sys.stdin = open("input.txt")

t = int(input())

for k in range(1,t+1):
    # answer : run이나 triplet이 몇 개 발견되는지 세는 영도
    answer = 0
    # 입력받은 값이 6개의 숫자가 붙어서 나와서 cards 리스트에 하나씩 떼서 저장
    deck = input()
    cards = []
    for d in deck:
        cards.append(int(d))
    
    # a, b가 같거나 연속되는 수인지 확인
    for a in range(len(cards)):
        for b in range(a+1,len(cards)):
            if cards[a] == cards[b] or abs(cards[a] - cards[b]) == 1:
                
                # a, b가 조건을 만족한다면 a,b,c가 같이 묶였을 때도 조건을 충족하는지 확인
                for c in range(b+1, len(cards)):
                    if (cards[c] + cards[b] + cards[a]) / 3 in [cards[a],cards[b],cards[c]]:
                        answer += 1
    
    # 23~25번째 줄 코드 실행 과정에서 triplet 2개/run 2개인 경우 answer가 2보다 큰 짝수가 됨
    # 이 문제를 해결하기 위해 answer가 0보다 크면서 2로 나누었을 때 나머지가 0인 경우를 조건으로 작성
    if answer > 0 and answer % 2 == 0:
        result = 1
    # run과 triplet이 발견되지 않거나, 둘 다 합쳐서 한 번만 발견되는 경우 0 반환
    else:
        result = 0

    print(f'#{k} {result}')