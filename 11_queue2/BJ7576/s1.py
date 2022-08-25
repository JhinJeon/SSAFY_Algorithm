# 토마토
import sys
sys.stdin = open('input4.txt')

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs(tomato_queue, y, x):
    global day
    while tomato_queue:
        for _ in range(len(tomato_queue)):
            y, x = tomato_queue.pop(0)
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
starting_point = []
for i in range(n):
    tomatos.append(list(map(int,input().split())))
    if 1 in tomatos[i]:
        starting_point.append((i, tomatos[i].index(1)))

day = 0
for col in range(n):
    for row in range(n):
        bfs(starting_point, row, col)

for col in range(n):
    if 0 in tomatos[col]:
        day = -1
        break
else:
    print(day-1)