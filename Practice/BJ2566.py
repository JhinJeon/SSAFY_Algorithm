# 최댓값
import sys
sys.stdin = open('input2.txt')

board = [list(map(int,input().split())) for _ in range(9)]
max_value = 0
max_idx = [0, 0]
for col in range(9):
    for row in range(9):
        if board[col][row] >= max_value:
            max_value = board[col][row]
            max_idx = [col+1, row+1]

print(max_value)
print(*max_idx)
