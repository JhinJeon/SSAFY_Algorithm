# 체스판 다시 칠하기
import sys
sys.stdin = open('1018sample3.txt')

n, m = map(int,input().split())

board = [list(input()) for _ in range(n)]
repaint = n * m

for col_start in range(n-7):
    for row_start in range(m-7):
        repaint_caseW = 0
        repaint_caseB = 0
        for col in range(col_start, col_start + 8):
            for row in range(row_start, row_start + 8):
                if (col_start - col + row_start - row) % 2 == 0 and board[col][row] != 'W':
                    repaint_caseW += 1
                if (col_start - col + row_start - row) % 2 == 1 and board[col][row] != 'B':
                    repaint_caseW += 1
            for row in range(row_start, row_start + 8):
                if (col_start - col + row_start - row) % 2 == 0 and board[col][row] != 'B':
                    repaint_caseB += 1
                if (col_start - col + row_start - row) % 2 == 1 and board[col][row] != 'W':
                    repaint_caseB += 1
        if repaint_caseW < repaint:
            repaint = repaint_caseW
        if repaint_caseB < repaint:
            repaint = repaint_caseB

print(repaint)