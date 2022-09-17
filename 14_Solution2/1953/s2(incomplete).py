# 탈주범 검거
# dfs 방식(미완성)

import sys
sys.stdin = open('sample_input.txt')

# 순서대로 상, 우, 하, 좌
path = {
    '1':[-1, 1, 1, -1],
    '2':[-1, 0, 1, 0],
    '3':[0, 1, 0, -1],
    '4':[-1, 1, 0, 0],
    '5':[0, 1, 1, 0],
    '6':[0, 0, 1, -1],
    '7':[-1, 0, 0, -1]
}


# 도주 가능한 경우의 수를 계산하는 함수 find_path
def find_path(y, x, t):
    global answer
    path_code = str(graph[y][x])
    graph[y][x] = 0
    direction = path.get(path_code)
    while t > 0:
        for d in range(4):
            # 짝수 번째 인덱스인 경우(y축 이동)
            if d % 2 == 0:
                ny = y + direction[d]
                nx = x
            else:
                ny = y
                nx = x + direction[d]
            if 0 <= ny < col_len and 0 <= nx < row_len and graph[ny][nx] != 0:
                t -= 1
                find_path(ny, nx, t)
        t += 1


t = int(input())

for tc in range(1,t+1):
    col_len, row_len, start_col, start_row, time_limit = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(col_len)]
    answer = 1

    find_path(start_col, start_row, time_limit)

    print(f'#{tc}', answer)