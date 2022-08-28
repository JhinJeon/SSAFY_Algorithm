# 개미(IM대비)
import sys
sys.stdin = open('sample_input.txt')

w, h = map(int,sys.stdin.readline().split())     # w = 가로, h = 세로
x, y = map(int,sys.stdin.readline().split())     # x = 가로, y = 세로
t = int(sys.stdin.readline())

# 좌/우, 상/하로 움직이는지 확인
dx = [1, -1]
dy = [-1, 1]

move = 0
dir_x = 0   # x좌표의 이동 방향
dir_y = 0   # y좌표의 이동 방향

while move < t:
    nx = x + dx[dir_x]
    ny = y + dy[dir_y]
    # 위쪽 또는 아래쪽 벽에 부딪히는 경우
    if ny < 0 or ny >=  h + 1:
        dir_y = (dir_y + 1) % 2
        x = nx
        y += dy[dir_y]
        move += 1
    # 왼쪽 또는 오른쪽 벽에 부딪히는 경우
    elif nx < 0 or nx >= w + 1:
        dir_x = (dir_x + 1) % 2
        x += dx[dir_x]
        y = ny
        move += 1
    # 정상적인 경우 정해진 방향에 따라 좌표 이동
    else:
        move += 1
        y = ny
        x = nx

print(x, y)