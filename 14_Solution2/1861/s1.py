# import sys
# sys.stdin = open('input.txt')
# sys.setrecursionlimit(50000)

# pycharm에서 실행할 때는 시간이 너무 오래 걸리는데 SWEA에서는 정상적으로 pass가 됨

# 순서대로 상, 우, 하, 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def search(y, x):
    global count
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < n and 0 <= ny < n and room[ny][nx] == room[y][x] + 1:
            count += 1
            search(ny, nx)

t = int(input())

for tc in range(1,t+1):
    n = int(input())
    room = [list(map(int,input().split())) for _ in range(n)]
    room_min = n ** 2
    move_count = 1

    for col in range(n):
        for row in range(n):
            room_no = room[col][row]        # 방 번호 최솟값
            count = 1                       # 한 번에 연결 가능한 개수
            search(col, row)
            # 최댓값 갱신인 경우 값과 방 번호 모두 수정
            if count > move_count:
                move_count = count
                room_min = room_no
            # 같은 값인데 방 번호만 작아지는 경우 방 번호만 수정
            elif count == move_count and room_no < room_min:
                room_min = room_no


    print(f'#{tc}', room_min, move_count)