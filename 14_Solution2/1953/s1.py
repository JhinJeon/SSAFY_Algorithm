# 탈주범 검거

# bfs 방식

import sys
sys.stdin = open('testinput.txt')

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
def find_path(y, x):
    global answer, time_limit
    queue = [[y, x]]
    while queue and time_limit > 0:
        for _ in range(len(queue)):
            # 다음 이동할 위치 좌표
            next_target = queue.pop(0)
            y = next_target[0]
            x = next_target[1]
            
            # 파이프 모양 판별용
            path_code = str(graph[y][x])

            # 연결된 길을 중복해서 탐색하려 하는 경우
            if int(path_code) <= 0:
                continue
            answer += 1
            direction = path.get(path_code)
            graph[y][x] = -1
            for d in range(4):
                # 짝수 번째 인덱스인 경우(y축 이동)
                if d % 2 == 0:
                    ny = y + direction[d]
                    nx = x
                # 홀수 번째 인덱스인 경우(x축 이동)
                else:
                    ny = y
                    nx = x + direction[d]
                # 인덱스 범위가 유효한 경우 1(그래프 안에 있고, 통행 가능한 구역인지 확인
                if 0 <= ny < col_len and 0 <= nx < row_len and graph[ny][nx] > 0:

                    # 인덱스 범위가 유효한 경우 2(통행 가능한 구역의 파이프도 현재 위치로 연결되어 있는지)
                    new_path = path.get(str(graph[ny][nx]))
                    if nx == x and ny + new_path[(d + 2) % 4] == y or ny == y and nx + new_path[(d + 2) % 4] == x:
                        queue.append([ny, nx])
        time_limit -= 1


t = int(input())

for tc in range(1,t+1):
    col_len, row_len, start_col, start_row, time_limit = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(col_len)]
    answer = 0

    find_path(start_col, start_row)

    print(f'#{tc}', answer)