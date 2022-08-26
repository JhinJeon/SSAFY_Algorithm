# 빙고
import sys
sys.stdin = open('input.txt')

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

def is_bingo(start_y, start_x):
    bingo_queue = [(start_y, start_x)]
    bingo_count = 1
    while bingo_queue:
        for _ in range(len(bingo_queue)):
            x, y = bingo_queue.pop(0)
            for direction in range(8):
                nx = x + dx[direction]
                ny = y + dx[direction]
                if 0 <= nx < 5 and 0 <= ny < 5 and cheolsu[ny][nx] == 'O':
                    bingo_queue.append((ny, nx))
        bingo_count += 1

    return bingo_count


cheolsu = [list(map(int,input().split())) for _ in range(5)]
solved = False
bingo_num = []

for _ in range(5):
    bingo_num += list(map(int,input().split()))

for count, bingo in enumerate(bingo_num):
    for col in range(5):
        bingo_check = False
        for row in range(5):
            if count > 4 and cheolsu[col][row] == 'O':
                if is_bingo(col, row) == 5:
                    print(count)
                    solved = True
                    break
            if cheolsu[col][row] == bingo:
                cheolsu[col][row] = 'O'
                bingo_check = True
                break
        if solved or bingo_check:
            break
    if solved:
        break
