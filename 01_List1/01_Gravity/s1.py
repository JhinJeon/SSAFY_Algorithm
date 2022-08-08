# 낙차 : 상자의 맨 꼭대기만 따지면 됨
import sys
sys.stdin = open("input.txt")

t = int(input())

for k in range(1,t+1):
    # 방 너비(가로)
    room = int(input())
    # 상자 현황(상자가 쌓인 개수 입력)
    boxes = list(map(int,input().split()))
    # 높이가 같거나 더 높은 상자를 만날 때까지 낙차 더하기
    result = 0
    for b in range(room):
        max_height = 0
        for i in range(b + 1, room):
            if boxes[b] > boxes[i]:
                max_height += 1

        # 낙차가 기존 최고 기록보다 크다면 최고 기록 갱신
        if result < max_height:
            result = max_height

    print(f'#{k} {result}')