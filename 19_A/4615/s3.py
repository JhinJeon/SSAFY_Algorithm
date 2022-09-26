# 재미있는 오셸로 게임
# 플레이하는 좌표를 매 턴마다 받는 거였나?

import sys
sys.stdin = open('sample_input.txt')


# 순서대로 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())

    # 기본 배치
    board = [[0] * n for _ in range(n)]
    # 4 * 4 는 1, 2
    # 6 * 6 은 2, 3
    # 8 * 8 은 3, 4
    standard = n // 2
    board[standard][standard] = 'W'
    board[standard-1][standard-1] = 'W'
    board[standard][standard-1] = 'B'
    board[standard-1][standard] = 'B'

    # 매 시기마다
    for player_turn in range(m):
        y, x, turn = map(int, input().split())
        # 인덱스 값 보정
        y -= 1
        x -= 1
        # color = 어떤 색깔로 채울 것인지 결정
        # 1이면 흑돌, 2면 백돌
        color = 'W' if turn == 2 else 'B'

        # 돌을 둘 수 있는 경우 해당 위치에 돌 두기
        if not board[y][x]:
            board[y][x] = color

            # 돌을 둔 위치의 주변 탐색(색깔 바꿀 돌 탐색)
            for direction in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]

                change_color = []   # 색깔을 바꿀 돌들의 좌표
                while True:
                    # 근처 좌표가 유효한 경우만 검사
                    if 0 > nx or nx >= n or 0 > ny or ny >= n or not board[ny][nx]:
                        change_color = []
                        break
                    # 바꿀 자리가 빈 칸인 경우 바꾸는 돌들을 초기화하고 반복 종료
                    if not board[ny][nx]:
                        change_color = []
                        break
                    # 바꿀 자리가 같은 색깔인 경우 반복 종료
                    if board[ny][nx] == color:
                        break
                    change_color.append([ny, nx])
                    nx += dx[direction]
                    ny += dy[direction]
                    # 색 전환 반영
                for change_y, change_x in change_color:
                    board[change_y][change_x] = color

    # 모든 시기 종료 후 결과 정산
    blackcount = 0
    whitecount = 0
    for col in range(n):
        for row in range(n):
            if board[col][row] == 'W':
                whitecount += 1
            elif board[col][row] == 'B':
                blackcount += 1

    print(f'#{tc}', blackcount, whitecount)
