# 단지번호붙이기
import sys

sys.setrecursionlimit(10000000)

n = int(input())

graph = [list(map(int, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

# dx, dy = 순서대로 상/하/좌/우 이동
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y):
    global wide
    visited[y][x] = 1
    wide += 1
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0 and graph[ny][nx] == 1:
            dfs(nx, ny)


area_info = []
for col in range(n):
    for row in range(n):
        if visited[col][row] == 0 and graph[col][row] == 1:
            wide = 0
            dfs(row, col)
            area_info.append(wide)

area_info.sort(reverse=False)

print(len(area_info))
for r in area_info:
    print(r)
