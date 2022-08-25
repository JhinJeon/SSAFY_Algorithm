# 단지번호붙이기
# bfs 사용

import sys
sys.stdin = open('input.txt')

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs(x, y):
    queue_status = [(x, y)]
    visited[y][x] = True
    value_count = 1

    while queue_status: # 큐에 값이 남아있는 동안 탐색 진행
        x, y = queue_status.pop(0)
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue_status.append((nx, ny))
                value_count += 1

    return value_count



n = int(input())
graph = [list(map(int,input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
result = []

for col in range(n):
    for row in range(n):
        if graph[col][row] == 1 and not visited[col][row]:
            result.append(bfs(row, col))

result.sort(reverse=True)

print(len(result))
print(*result, sep='\n')
