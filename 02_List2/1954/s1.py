# # 달팽이 숫자
import sys
sys.stdin = open('input.txt')

t = int(input())

# 우, 하, 좌, 상 인덱스 이동 표시
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
# key : 0부터 위, 오른쪽, 아래, 왼쪽


for tc in range(1, t+1):
    n = int(input())
    print(f'#{tc}')
    graph = [[0] * n for _ in range(n)]
    x = 0
    y = 0
    direction = 0
    for roll in range(1, n**2+1):
        graph[y][x] = roll
        x += dx[direction]
        y += dy[direction]

        if x >= n or x < 0 or y < 0 or y >= n or graph[y][x] != 0:
            x -= dx[direction]
            y -= dy[direction]

            direction = (direction+1) % 4

            x += dx[direction]
            y += dy[direction]

    for i in graph:
        print(*i)


'''
지그재그 순회

for i in range(n):
    for j in range(m):
        Array[i][j + (m-1-2*j) * (i%2)]
'''
