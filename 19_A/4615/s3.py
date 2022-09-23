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

    # 마지막 숫자가 1이면 흑돌 좌표, 2면 백돌 좌표
    for _ in range(m):
        row, col, race = map(int,input().split())
        if race == 1:
            player_1.append(list([row-1, col-1]))
        else:
            player_2.append(list([row-1, col-1]))

    # 해당 좌표를 사용했는지 확인하는 용도
    p1_used = [False] * len(player_1)
    p2_used = [False] * len(player_2)

    left_border = standard - 1
    right_border = standard + 2
    top_border = standard - 1
    bottom_border = standard + 2

    # 선공 조절(할 수 있는 행동이 없으면 상대 플레이어가 연속 행동 가능)
    black_turn = 'True'

    for player_turn in range(m):
        playable_area = [[],[]]
        # 어느 플레이어의 턴인지 결정
        play = player_turn // 2
        played = False              # 턴을 마쳤는지 확인하는 용도
        if black_turn:    # 선공  = 흑돌을 둘 차례
            position = player_1     # 1플레이어 턴

            # 흰색(상대) 돌 배치 상태를 보고 다음에 둘 곳 결정
            for wb in wb_status:
                y = wb[0]
                x = wb[1]
                # 상대 돌 주위에 내 돌 배치
                p1_case = []    # 1p가 둘 수 있는 경우의 수
                for direction in range(8):
                    ny = y + dy[direction]      # 새로 둘 위치의 y좌표
                    nx = x + dx[direction]      # 새로 둘 위치의 x좌표
                    if 0 <= ny < n and 0 <= nx < n and not board[ny][nx]:
                        p1_case.append([ny, nx])

                # 1P가 사용 가능한 좌표에서 다움 수를 어느 좌표에 둘지 결정
                for i in range(len(player_1)):
                    if position[i] in p1_case and not p1_used[i]:
                        # target = 플레이어가 둘 좌표
                        target = position[i]
                        target_y = target[0]
                        target_x = target[1]

                        # 이미 플레이한 돌이 있는 경우 continue
                        if board[target_y][target_x]:
                            continue

                        # 기존의 내 돌이 어디에 있는지 파악
                        for bb in bb_status:
                            black_y = bb[0]  # 기존의 돌 y좌표
                            black_x = bb[1]     # 기존의 돌 x좌표

                            # 경로 상에서 검은 공으로 바뀔 흰 공들의 좌표
                            change_color_path = []
                            changeable = True   # 유효한 수인지(흰 공의 색을 바꿀 수 있는지) 확인하는 용도
                            # 가로 방향 배치인 경우
                            if black_y == target_y and black_x != target_x:
                                bounce = 1 if black_x < target_x else -1
                                # 새로 둘 위치와 기존에 둔 위치 사이의 돌 소유권 변경
                                for k in range(black_x + bounce, target_x, bounce):
                                    # 흰 돌이 경로 상에 없는 경우 탐색 중단
                                    if board[target_y][k] != 'W':
                                        changeable = False
                                        break
                                    change_color_path.append([target_y, k])

                            # 세로 방향 배치인 경우
                            elif black_x == target_x:
                                bounce = 1 if black_y < target_y else -1
                                # 새로 둘 위치와 기존에 둔 위치 사이의 돌 소유권 변경
                                for k in range(black_y + bounce, target_y, bounce):   # 검은 공으로 변경
                                    # 돌이 경로 상에 없는 경우 탐색 중단
                                    if board[k][target_x] != 'W':
                                        changeable = False
                                        break
                                    change_color_path.append([k, target_x])
                            # 대각 방향 배치인 경우
                            elif abs(black_x - target_x) == abs(black_y - target_y):
                                bounce_y = 1 if black_y < target_y else -1
                                bounce_x = 1 if black_x < target_x else -1
                                gap = abs(black_y - target_y)
                                for k in range(1,gap):
                                    if board[black_y + k * bounce_y][black_x + k * bounce_x] != 'W':
                                        changeable = False
                                    change_color_path.append([black_y + k * bounce_y, black_x + k * bounce_x])
                                if not changeable:
                                    break
                            # 규칙에 맞지 않는 배치는 탐색하지 않음
                                
                            # 변경 사항 적용
                            if changeable and change_color_path:
                                board[target[0]][target[1]] = 'B'
                                bb_status.append([target[0], target[1]])
                                for path in change_color_path:
                                    board[path[0]][path[1]] = 'B'
                                    wb_status.remove([path[0], path[1]])
                                    bb_status.append([path[0], path[1]])
                                played = True

                    # 플레이 처리가 된 경우 턴 종료
                    if played:
                        p1_used[i] = True
                        black_turn = False
                        break
            
            # 할 수 있는 행동이 없으면 다음 플레이어에게 넘기기
            else:
                black_turn = False

        else:                       # 후공 = 백돌을 둘 차례
            position = player_2     # 2플레이어 턴

            # 검은색(상대) 돌 배치 상태를 보고 다음에 둘 곳 결정
            for bb in bb_status:
                y = bb[0]
                x = bb[1]
                # 상대 돌 주위에 내 돌 배치
                p2_case = []  # 2p가 둘 수 있는 경우의 수
                for direction in range(8):
                    ny = y + dy[direction]  # 새로 둘 위치의 y좌표
                    nx = x + dx[direction]  # 새로 둘 위치의 x좌표
                    if 0 <= ny < n and 0 <= nx < n and not board[ny][nx]:
                        p2_case.append([ny, nx])

                # 2P가 사용 가능한 좌표에서 다움 수를 어느 좌표에 둘지 결정
                for i in range(len(player_2)):
                    if position[i] in p2_case and not p2_used[i]:
                        # target = 플레이어가 둘 좌표
                        target = position[i]
                        target_y = target[0]
                        target_x = target[1]

                        # 이미 플레이한 돌이 있는 경우 continue
                        if board[target_y][target_x]:
                            continue

                        # 기존의 내 돌이 어디에 있는지 파악
                        for wb in wb_status:
                            white_y = wb[0]  # 기존의 돌 y좌표
                            white_x = wb[1]  # 기존의 돌 x좌표

                            # 경로 상에서 흰 돌로 바뀔 검은 돌들의 좌표
                            change_color_path = []
                            changeable = True  # 유효한 수인지(검은 공의 색을 바꿀 수 있는지) 확인하는 용도
                            # 가로 방향 배치인 경우
                            if white_y == target_y and white_x != target_x:
                                bounce = 1 if white_x < target_x else -1
                                # 새로 둘 위치와 기존에 둔 위치 사이의 돌 소유권 변경
                                for k in range(white_x + bounce, target_x, bounce):
                                    # 검은 돌이 경로 상에 없는 경우 탐색 중단
                                    if board[target_y][k] != 'B':
                                        changeable = False
                                        break
                                    change_color_path.append([target_y, k])

                            # 세로 방향 배치인 경우
                            elif white_x == target_x:
                                bounce = 1 if white_y < target_y else -1
                                # 새로 둘 위치와 기존에 둔 위치 사이의 돌 소유권 변경
                                for k in range(white_y + bounce, target_y, bounce):  # 흰 공으로 변경
                                    # 검은 돌이 경로 상에 없는 경우 탐색 중단
                                    if board[k][target_x] != 'B':
                                        changeable = False
                                        break
                                    change_color_path.append([k, target_x])
                            elif abs(white_x - target_x) == abs(white_y - target_y):
                                bounce_y = 1 if white_y < target_y else -1
                                bounce_x = 1 if white_x < target_x else -1
                                gap = abs(white_y - target_y)
                                for k in range(1, gap):
                                    if board[white_y + k * bounce_y][white_x + k * bounce_x] != 'B':
                                        changeable = False
                                    change_color_path.append([white_y + k * bounce_y, white_x + k * bounce_x])
                                if not changeable:
                                    break
                            # 규칙에 맞지 않는 배치는 탐색하지 않음

                            # 변경 사항 적용
                            if changeable and change_color_path:
                                board[target[0]][target[1]] = 'W'
                                wb_status.append([target[0], target[1]])
                                for path in change_color_path:
                                    board[path[0]][path[1]] = 'W'
                                    bb_status.remove([path[0], path[1]])
                                    wb_status.append([path[0], path[1]])
                                played = True

                    # 플레이 처리가 된 경우 턴 종료
                    if played:
                        p2_used[i] = True
                        black_turn = True
                        break
                    
            # 할 수 있는 행동이 없으면 다음 플레이어에게 넘기기
            else:
                black_turn = True

    whitecount = len(wb_status)
    blackcount = len(bb_status)

    print(f'#{tc}', blackcount, whitecount)






