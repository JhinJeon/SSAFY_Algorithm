# 등산로 조성
import sys
sys.stdin = open('sample6_input.txt')
t = int(input())

# 좌표 이동 : 상, 우, 하, 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def dfs(graph, y, x, dc):
    digpath = []
    visited[y][x] = True
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
            if graph[ny][nx] < graph[y][x]:
                digpath.append(graph[y][x])
                dfs(graph, ny, nx, dc)
            else:
                if dc > 0:
                    for dig in range(k):
                        digpath.append(graph[y][x])
                        graph[ny][nx] -= k
                        dfs(graph, ny, nx, 0)
            return len(digpath)
    digpath.pop()
    visited[y][x] = False



for tc in range(1,t+1):
    # k = 한 번에 공사 가능한 최대 깊이
    n, k = map(int,input().split())
    dig_chance = 1
    higher_ground = 0
    graph = []
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        graph.append(list(map(int, input().split())))
        if max(graph[i]) > higher_ground:
            higher_ground = max(graph[i])

    max_length = 0
    for col in range(n):
        for row in range(n):
            if graph[col][row] == higher_ground:
                length = dfs(graph, col, row, dig_chance)
                if length > max_length:
                    max_length = length
    print(f'#{tc} {max_length}')