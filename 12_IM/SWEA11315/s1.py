# 오목 판정
import sys
sys.stdin = open('sample_input.txt')

# 순서대로 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]


def o_mok(graph, y, x):
    global omok_count
    visited[y][x] = True
    for direction in range(8):
        for power in range(1, 5):
            nx = x + dx[direction] * power
            ny = y + dy[direction] * power
            if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 'o':
                omok_count += 1
                o_mok(graph, ny, nx)


t = int(input())

for tc in range(1,t+1):
    n = int(input())
    board = [list(input()) for _ in range(n)]
    omok_count = 1
    answer = 'NO'
    for col in range(n):
        for row in range(n):
            if board[col][row] == 'o':
                visited = [[False] * n for _ in range(n)]
                o_mok(board, col, row)
                if omok_count == 5:
                    answer = 'YES'
                    break
                else:
                    omok_count = 1
        if answer == 'YES':
            print(f'#{tc} {answer}')
            break
    else:
        print(f'#{tc} {answer}')
