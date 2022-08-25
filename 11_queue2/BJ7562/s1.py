# 나이트의 이동
import sys
sys.stdin = open('input.txt')
# 이동 위치 : 1시부터 시계방향으로

dy = [-2, -1, 1, 2, 2, 1, -1, -2]
dx = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(x, y):
    board[y][x] = 1
    knight_queue = [(x, y)]
    move = 0
    while knight_queue:
        move += 1
        for move in range(len(knight_queue)):
            next_move = knight_queue.pop(0)
            for direction in range(8):
                nx = next_move[0] + dx[direction]
                ny = next_move[1] + dy[direction]
                if 0 <= nx < n and 0 <= ny < n and board[ny][nx] == 0:
                    board[ny][nx] = 1
                    knight_queue.append((nx, ny))
            if nx == end_x and ny == end_y:
                return move
    return move


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    board = [[0] * n for _ in range(n)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    print(bfs(start_x, start_y))