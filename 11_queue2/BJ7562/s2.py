# 나이트의 이동
import sys
sys.stdin = open('input.txt')
# 이동 위치 : 1시부터 시계방향으로

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(x, y):
    board[x][y] = 1
    knight_queue.append((x, y))
    while knight_queue:
        if x == end_x and y == end_y:
            return board[x][y] - 1
        x, y = knight_queue.pop(0)
        for direction in range(8):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                knight_queue.append((nx, ny))
    return 0


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    board = [[0] * n for _ in range(n)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    knight_queue = []
    print(bfs(start_x, start_y))