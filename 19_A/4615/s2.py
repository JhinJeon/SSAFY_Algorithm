# 재미있는 오셸로 게임
import sys
sys.stdin = open('sample_input.txt')


# 순서대로 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

t = int(input())

for tc in range(1,t+1):
    n, m = map(int,input().split())

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

    # 공의 좌표만 저장
    wb_status = [[standard, standard], [standard-1, standard-1]]
    bb_status = [[standard, standard-1], [standard-1, standard]]
    
    player_1 = []   #  흑돌(선공)
    player_2 = []   #  백돌(후공)

    for _ in range(m):
        row, col, race = map(int,input().split())
        if race == 1:
            player_1.append(list([row-1, col-1]))
        else:
            player_2.append(list([row-1, col-1]))

    left_border = standard - 1
    right_border = standard + 2
    top_border = standard - 1
    bottom_border = standard + 2

    # 돌을 더 둘 곳이 없으면 게임 종료
    end_game = False

    for player_turn in range(m):
        playable_area = [[],[]]
        # 어느 플레이어의 턴인지 결정
        play = player_turn // 2
        if player_turn % 2 == 0:    # 선공  = 흑돌을 둘 차례
            position = player_1
            # 흰색 공 배치 상태를 보고 다음에 둘 곳 결정
            for wb in wb_status:
                y = wb[0]
                x = wb[1]
                for direction in range(8):
                    ny = y + dy[direction]
                    nx = x + dx[direction]
                    if 0 <= ny < n and 0 <= nx < n and not board[ny][nx]:
                        for i in range(len(player_1)):
                            if player_1[i][0] == ny and player_1[i][1] == nx:
                                # 플레이어가 둘 위치
                                target = player_1.pop(i)
                                # 가로 방향 배치인 경우
                                if target[0] == ny and target[1] != nx:
                                    bounce = 1 if target[1] > nx else -1
                                    for k in range(nx, target[1]+bounce, bounce):
                                        board[ny][k] = 'B'
                                        bb_status.append([ny, k])
                                        wb_status.remove([ny, k])
                                # 세로 방향 배치인 경우
                                elif target[1] == nx:
                                    bounce = 1 if target[0] > ny else -1
                                    for k in range(ny, target[0]+bounce, bounce):   # 검은 공으로 변경
                                        board[k][nx] = 'B'
                                        bb_status.append([k, nx])
                                        wb_status.remove([k, nx])
                                # 대각 방향 배치인 경우
                                else:
                                    bounce_y = 1 if target[0] > ny else -1
                                    bounce_x = 1 if target[1] > nx else -1
                                    for ky in range(ny, target[0]+bounce_y, bounce_x):
                                        for kx in range(nx, target[0]+bounce_x, bounce_x):
                                            board[ky][kx] = 'B'
                                            bb_status.append([ky, kx])
                                            wb_status.remove([ky, kx])
                            break
                else:
                    end_game = True

        else:                       # 후공 = 흑돌을 둘 차례
            position = player_2
            # 검은색 공 배치 상태를 보고 다음에 둘 곳 결정
            for bb in bb_status:
                y = bb[0]
                x = bb[1]
                for direction in range(8):
                    ny = y + dy[direction]
                    nx = x + dx[direction]
                    if 0 <= ny < n and 0 <= nx < n and not board[ny][nx]:
                        for i in range(len(player_1)):
                            if player_2[i][0] == ny and player_2[i][1] == nx:
                                target = player_2.pop(i)
                                # 가로 방향 배치인 경우
                                if target[0] == ny and target[1] != nx:
                                    bounce = 1 if target[1] > nx else -1
                                    for k in range(nx, target[1]+bounce, bounce):
                                        board[ny][k] = 'B'
                                        wb_status.append([ny, k])
                                        bb_status.remove([ny, k])
                                # 세로 방향 배치인 경우
                                elif target[1] == nx:
                                    bounce = 1 if target[0] > ny else -1
                                    for k in range(ny, target[0]+bounce, bounce):   # 검은 공으로 변경
                                        board[k][nx] = 'B'
                                        wb_status.append([k, nx])
                                        bb_status.remove([k, nx])
                                # 대각 방향 배치인 경우
                                else:
                                    bounce_y = 1 if target[0] > ny else -1
                                    bounce_x = 1 if target[1] > nx else -1
                                    for ky in range(ny, target[0]+bounce_y, bounce_x):
                                        for kx in range(nx, target[0]+bounce_x, bounce_x):
                                            board[ky][kx] = 'B'
                                            wb_status.append([ky, kx])
                                            bb_status.remove([ky, kx])
                            break
                else:
                    end_game = True
        if end_game:
            break

    whitecount = 0
    blackcount = 0
    for col in range(n):
        for row in range(n):
            if board[col][row] == 'W':
                whitecount += 1
            elif board[col][row] == 'B':
                blackcount += 1

    print('#{tc}', blackcount, whitecount)






