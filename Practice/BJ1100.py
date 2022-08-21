# 하얀 칸

chess_board = [list(input()) for _ in range(8)]
answer = 0

for col in range(8):
    for row in range(8):
        if (col + row) % 2 == 0 and chess_board[col][row] == 'F':
            answer += 1

print(answer)