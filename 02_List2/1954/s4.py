# 달팽이 숫자

import sys

sys.stdin = open('input.txt')

t = int(input())

# 방향 전환 인덱스
# 우 - 하 - 좌 - 상 순서
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for tc in range(1, t + 1):
    n = int(input())
    graph = [[0] * n for _ in range(n)]

    # x = 현재 x 인덱스 값
    # y = 현재 y 인덱스 값
    # roll = 배열 안에 넣을 수
    x = 0
    y = 0
    roll = 0
    direction = 0

    # roll이 n**2가 될 때까지 반복문 수행
    while roll < n**2:
        # graph에 현재 roll 입력
        roll += 1
        graph[y][x] = roll

        
        # 이동할 좌표 설정
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 좌표의 유효성 검사
        if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 0:
            y, x = ny, nx

        # 다른 숫자가 있는 경우 방향 전환
        else:
            direction = (direction + 1) % 4
            x += dx[direction]
            y += dy[direction]


    print(f'#{tc}')
    for col in graph:
        print(*col)
