# 농작물 수확하기
import sys
sys.stdin = open('input.txt')

# 순서대로 상, 하, 좌, 우
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


# bfs 방식
def harvest(y, x, power):
    result = farm[y][x]
    farm[y][x] = 0
    for direction in range(4):
        for p in range(1,power+1):
            nx = x + dx[direction] * p
            ny = y + dy[direction] * p
            result += farm[ny][nx]
            farm[ny][nx] = 0
    return result


t = int(input())

for tc in range(1,t+1):
    n = int(input())
    farm = [list(map(int,input())) for _ in range(n)]
    center = n // 2
    print(f'#{tc}', harvest(center, center, center))