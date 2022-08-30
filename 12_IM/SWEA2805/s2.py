# 농작물 수확하기
# 중앙에서 n번 이동 안에 갈 수 있는 칸만 계산
import sys
sys.stdin = open('input.txt')

# 순서대로 상, 하, 좌, 우
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

t = int(input())

for tc in range(1,t+1):
    n = int(input())
    farm = [list(map(int,input())) for _ in range(n)]
    center = n // 2
    result = 0
    # 중앙에서 가로/세로로 (농장 변 길이 // 2 + 1)칸 만큼 떨어진 거리에 있는 농작물은 수확 가능
    for col in range(n):
        for row in range(n):
            if abs(center - col) + abs(center - row) < center + 1:
                result += farm[col][row]
    print(f'#{tc}',result)