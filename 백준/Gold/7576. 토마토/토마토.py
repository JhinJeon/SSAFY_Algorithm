from collections import deque


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs(tomato_queue, y, x):
    global day
    while tomato_queue:
        for _ in range(len(tomato_queue)):
            y, x = tomato_queue.popleft()
            for direction in range(4):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0 <= nx < m and 0 <= ny < n and tomatos[ny][nx] == 0:
                    tomato_queue.append((ny, nx))
                    tomatos[ny][nx] = 1
        day += 1
    return


m, n = map(int,input().split())
tomatos = []
starting_point = deque()
for col in range(n):
    tomatos.append(list(map(int,input().split())))
    for row in range(m):
        if tomatos[col][row] == 1:
            starting_point.append((col, row))

day = 0
bfs(starting_point, row, col)

for col in tomatos:
    if 0 in col:
        print(-1)
        break
else:
    print(day-1)