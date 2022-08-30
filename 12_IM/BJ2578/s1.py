# 빙고
import sys
sys.stdin = open('input.txt')

bingo_board = [list(map(int,input().split())) for _ in range(5)]
bingo_check = []
for _ in range(5):
    bingo_check += list(map(int,input().split()))


for idx, bingo_num in enumerate(bingo_check):
    checked = False
    bingo_count = 0
    # 빙고판에 'O' 표시
    for col in range(5):
        for row in range(5):
            if bingo_board[col][row] == bingo_num:
                bingo_board[col][row] = 'O'
                checked = True
                break
        if checked:
            break
    
    # 빙고가 몇개 있는지 확인(가로)
    for col in range(5):
        for row in range(5):
            if bingo_board[col][row] != 'O':
                break
        else:
            bingo_count += 1

    if bingo_count >= 3:
        print(idx + 1)
        break

    # 빙고가 몇개 있는지 확인(세로)
    for row in range(5):
        for col in range(5):
            if bingo_board[col][row] != 'O':
                break
        else:
            bingo_count += 1

    if bingo_count >= 3:
        print(idx + 1)
        break

    # 빙고가 몇 개 있는지 확인(대각선 1)

    for row in range(5):
        if bingo_board[row][row] != 'O':
            break
    else:
        bingo_count += 1

    if bingo_count >= 3:
        print(idx + 1)
        break

    # 빙고가 몇 개 있는지 확인(대각선 2)
    for row in range(5):
        if bingo_board[col][4-col] != 'O':
            break
    else:
        bingo_count += 1

    if bingo_count >= 3:
        print(idx + 1)
        break