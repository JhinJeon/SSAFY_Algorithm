import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1,t+1):
    board = [list(input()) for _ in range(5)]

    answer = ''
    board_len_max = 0
    for rows in board:
        if len(rows) > board_len_max:
            board_len_max = len(rows)

    for row in range(board_len_max):
        for col in range(5):
            if row >= len(board[col]):
                continue
            answer += board[col][row]

    print(f'#{tc} {answer}')