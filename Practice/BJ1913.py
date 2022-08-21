# 달팽이

# 순서대로 하, 우, 상, 좌
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

n = int(input())
num = int(input())
graph = [[0] * n for _ in range(n)]

y = 0
x = 0
direction = 0
for roll in range(n**2, 0, -1):
    graph[y][x] = roll
    nx = x + dx[direction]
    ny = y + dy[direction]
    if roll == num:
        answer = [y+1, x+1]
    if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 0:
        x = nx
        y = ny
    else:
        direction = (direction + 1) % 4
        x = x + dx[direction]
        y = y + dy[direction]

for g in graph:
    print(*g)
print(*answer)