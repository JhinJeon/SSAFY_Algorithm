# 달팽이 숫자

import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    graph = [[0] * n for _ in range(n)]

    # x = 현재 x 인덱스 값
    # y = 현재 y 인덱스 값
    # roll = 배열 안에 넣을 수
    x = 0
    y = 0
    roll = 1

    # roll이 n**2가 될 때까지 반복문 수행
    while roll < n**2:
        # 오른쪽으로 이동, 오른쪽 위 모서리 또는 0이 아닌 값을 만나기 직전까지 반복
        while x >= 0 and x < n - 1 and graph[x+1][y] == 0:
            graph[y][x] = roll
            roll += 1
            x += 1
        # 아래쪽으로 이동, 오른쪽 아래 모서리 또는 0이 아닌 값을 만나기 직전까지 반복
        while y >= 0 and y < n - 1 and graph[x][y+1] == 0:
            graph[y][x] = roll
            roll += 1
            y += 1
        # 왼쪽으로 이동, 왼쪽 아래 모서리 또는 0이 아닌 값을 만나기 직전까지 반복
        while x >= 0 and x < n - 1 and graph[x-1][y] == 0:
            graph[y][x] = roll
            roll += 1
            x -= 1
        # 위쪽으로 이동, 왼쪽 위 모서리 또는 0이 아닌 값을 만나기 직전까지 반복
        while y >= 0 and y < n - 1 and graph[x][y-1] == 0:
            graph[y][x] = roll
            roll += 1
            y -= 1

    print(f'#{tc}')
    for col in graph:
        print(*col)
