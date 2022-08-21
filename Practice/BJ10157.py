# 자리 배정

width, height = map(int,input().split())
search_seat = int(input())

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
stage = [[0] * width for _ in range(height)]

x = 0
y = 0
direction = 0

for val in range(1,width * height+1):
    stage[y][x] = val
    ny = y + dy[direction]
    nx = x + dx[direction]
    if val == search_seat:
        print(x+1, y+1)
        break
    if 0 <= ny < height and 0 <= nx < width and stage[ny][nx] == 0:
        y = ny
        x = nx
    else:
        direction = (direction + 1) % 4
        x = x + dx[direction]
        y = y + dy[direction]
else:
    print(0)
