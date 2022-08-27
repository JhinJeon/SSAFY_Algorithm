# 농작물 수확하기
import sys
sys.stdin = open('input.txt')


t = int(input())

for tc in range(1,t+1):
    n = int(input())
    farm = [list(map(int,input())) for _ in range(n)]
    center = n // 2
    result = 0
    # 중앙에서 가로/세로로 (농장 변 길이 // 2 + 1)칸 만큼 떨어진 거리에 있는 농작물은 수확 가능
    for col in range(n):
        for row in range(n):
            if col >= center:
                y = col - center
            else:
                y = center - col
            if row >= center:
                x = row - center
            else:
                x = center - row
            if y + x <= center:
                result += farm[col][row]
    print(f'#{tc}',result)