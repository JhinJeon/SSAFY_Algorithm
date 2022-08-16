# 고대 유적

import sys

sys.stdin = open('input1.txt')

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    size_max = 0
    graph = []

    for i in range(n):
        graph.append(list(map(int, input().split())))

    # (열 방향)1을 찾은 경우 길이 + 1, 최대 길이를 경신하면 현재 길이를 최대 길이로 설정
    for col in range(n):
        size_row = 0
        for row in range(m):

            if graph[col][row] == 1:
                size_row += 1
                if size_row > size_max:
                    size_max = size_row
            else:
                size_row = 0

    # n과 m이 같지 않을 때에도 인덱스 에러가 발생하지 않도록 별도의 반복문 설정
    # (행 방향)1을 찾은 경우 길이 + 1, 최대 길이를 경신하면 현재 길이를 최대 길이로 설정
    for row in range(m):
        size_col = 0
        for col in range(n):
            if graph[col][row] == 1:
                size_col += 1
                if size_col > size_max:
                    size_max = size_col
            else:
                size_col = 0

    print(f'#{tc} {size_max}')
