# ladder 1

import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1,t+1):
    ladder_graph = [list(map(int,input().split())) for _ in range(100)]
    
    # 좌, 상, 우 이동을 dx, dy로 표현
    # y가 세로(column), x가 가로(row)
    dx = [-1, 0, 1]
    dy = [0, -1, 0]
    for starting_point in range(100):
        if ladder_graph[99][starting_point] == 2:
            x = starting_point
            y = 99
            direction = 0
            while y > 0:
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0 <= nx < 100 and 0 <= ny and ladder_graph[ny][nx] == 1:
                    x, y = nx, ny
                    continue
                nx -= dx[direction]
                ny -= dy[direction]
                direction = (direction + 1) % 3


            print(f'#{tc} {x}')
            continue







