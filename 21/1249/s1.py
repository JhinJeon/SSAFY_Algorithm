# 보급로
# BFS 특성 상 이미 방문한 지역을 체크해야 하는데, 이 경우 돌아가는 경우의 수는 어떻게 처리해야 할지 난감하다.

import sys
sys.stdin = open('input.txt')

# 순서대로 상, 우, 하, 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs(col, row):
    next_visit =[(col, row)]   # 다음 방문 지점(행, 열)
    while next_visit:
        for _ in range(len(next_visit)):
            y, x = next_visit.pop(0)
            # 방문 처리
            visited[y][x] = True
            result = elapsed_time[y][x]

            for direction in range(4):
                nx = x + dx[direction]
                ny = y + dy[direction]
                # 시작점으로 되돌아간 경우
                if ny == 0 and nx == 0:
                    continue
                # 목적지를 향해서 경로를 찾는 경우
                elif 0 <= nx < n and 0 <= ny < n:
                    # 아직 방문하지 않은 지역인 경우
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        next_visit.append((ny, nx))
                        elapsed_time[ny][nx] = result + graph[ny][nx]
                    # 이미 방문한 지역인 경우 기존보다 시간 단축이 되는 경우에만 이동
                    else:
                        if elapsed_time[ny][nx] > result + graph[ny][nx]:
                            elapsed_time[ny][nx] = result + graph[ny][nx]
                            next_visit.append((ny, nx))


t = int(input())

for tc in range(1,t+1):
    n = int(input())    # 정사각형 지도 한 변의 길이
    graph = [list(map(int, input())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    elapsed_time = [[0] * n for _ in range(n)]   # 구역까지 도달하는 데 걸린 시간
    bfs(0,0)
    answer = elapsed_time[-1][-1]
    print(f'#{tc}', answer)