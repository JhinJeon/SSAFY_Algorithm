# 달팽이 숫자

# 델타값(인덱스 이동) 정의
# 나선 모양으로 진행하므로 시계 방향으로 정의하는 것이 좋음
# 인덱스 번호 기준 0 = 우, 1 = 하, 2 = 좌, 3 = 상
import sys
sys.stdin = open('input.txt')

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for tc in range(1, int(input())+1):
    n = int(input())
    graph = [[0] * n for _ in range(n)]
    x, y = 0, 0
    direction = 0

    for i in range(1, n**2 + 1):
        graph[y][x] = i
        ny = y + dy[direction]
        nx = x + dx[direction]

        # 범위를 벗어나지 않는 경우 계속 이동
        if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 0:
            y, x = ny, nx

        # 다른 숫자가 있는 경우 방향 전환
        else:
            direction = (direction + 1) % 4
            x += dx[direction]
            y += dy[direction]

    print(f'#{tc}')
    for line in graph:
        print(*line)
