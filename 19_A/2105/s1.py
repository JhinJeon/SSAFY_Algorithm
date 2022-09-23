# 디저트 카페
import sys
sys.stdin = open('sample_input.txt')


# 순서대로 우상, 우하, 좌하, 좌상
dy = [-1, 1, 1, -1]
dx = [1, 1, -1, -1]


def cafe_tour(start_y, start_x, y, x, score, depth):
    global answer
    if start_y == y and start_x == x and depth > 0:
        if answer < score:
            answer = score
        return
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
            cafe_tour(start_y, start_x, ny, nx, score + cafe_map[y][x], depth + 1)


t = int(input())

for tc in range(1,t+1):
    n = int(input())
    cafe_map = [list(map(int,input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    answer = 0
    for col in range(1, n-1):
        for row in range(1, n-1):
            cafe_tour(col, row, col, row, cafe_map[col][row], 0)
    print(f'#{tc}', answer)