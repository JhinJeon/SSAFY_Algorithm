# 단지번호붙이기
# dfs 복습

import sys
sys.stdin = open('input.txt')

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def dfs(x, y):
    global value_count
    graph[y][x] = 0
    value_count += 1
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 1:
            dfs(nx, ny)


result.sort(reverse=False)

n = int(input())
graph = [list(map(int,input())) for _ in range(n)]
result = []

for col in range(n):
    for row in range(n):
        if graph[col][row] == 1:
            value_count = 0
            dfs(row, col)
            result.append(value_count)

print(len(result))
print(*result, sep='\n')
