# 색칠하기

import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1,t+1):
    n = int(input())
    # board = 10 * 10 크기의 빈(흰색) 격자
    board = [[0] * 10 for _ in range(10)]

    # paints = 색칠 영역에 대한 정보를 담을 리스트
    paints = []
    for color in range(n):
        paints.append(list(map(int,input().split())))

    # board의 각 구역마다 paints의 정보에 따라 색칠
    # 빨간색을 1을 더하고, 파란색은 2를 더함
    for col in range(10):
        for row in range(10):
            for paint in paints:
                if paint[0] <= row <= paint[2] and paint[1] <= col <= paint[3]:
                    board[col][row] += paint[4]

    # answer = 보라색으로 색칠된 구역 수
    answer = 0
    
    # 구역의 값이 3인 경우(빨간색과 파란색을 한 번씩 더한 경우) answer에 카운트
    for col in range(10):
        for row in range(10):
            if board[col][row] == 3:
                answer += 1

    print(f'#{tc} {answer}')