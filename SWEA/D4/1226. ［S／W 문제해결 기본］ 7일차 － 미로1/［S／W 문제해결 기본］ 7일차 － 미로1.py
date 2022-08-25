# 순서대로 상, 우, 하, 좌 이동
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs(start_col, start_row):
    visited[start_col][start_row] = True
    queue_status = [(start_col, start_row)]
    exit = 0

    while queue_status:
        x, y = queue_status.pop(0)
        for direction in range(4):
            n_col = x + dy[direction]
            n_row = y + dx[direction]
            if 0 <= n_row < 16 and 0 <= n_col < 16:
                if miro[n_col][n_row] == 3:
                    exit = 1
                    break
                if not visited[n_col][n_row] and miro[n_col][n_row] == 0:
                    queue_status.append((n_col, n_row))
                    visited[n_col][n_row] = True
        if exit == 1:
            break

    return exit


for _ in range(1,11):
    tc = int(input())
    miro = [list(map(int,input())) for _ in range(16)]
    visited = [[False] * 16 for _ in range(16)]
    for col in range(16):
        for row in range(16):
            if miro[col][row] == 2:
                print(f'#{tc}', bfs(col, row))