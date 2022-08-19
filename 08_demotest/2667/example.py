# 단지번호붙이기
# 실습 예시

n = int(input())
board = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
result = []
# dx, dy = 순서대로 상/하/좌/우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    global total
    visited[x][y] = True
    total += 1

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == 1:
            dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if not visited[i][j] and board[i][j] == 1:
            total = 0
            dfs(i, j)
            result.append(total)


print(len(result), *sorted(result), sep='\n')
