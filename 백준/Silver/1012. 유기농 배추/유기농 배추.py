import sys
sys.setrecursionlimit(10000000)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(graph, x, y):
    graph[y][x] = 0
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
            dfs(graph, nx, ny)



t = int(input())

for tc in range(1, t + 1):
    m, n, k = map(int, input().split())
    farm = [[0] * m for _ in range(n)]
    for position in range(k):
        row, col = map(int, input().split())
        farm[col][row] = 1
    bug_count = 0
    for col in range(n):
        for row in range(m):
            if farm[col][row] == 1:
                dfs(farm, row, col)
                bug_count += 1
    print(bug_count)