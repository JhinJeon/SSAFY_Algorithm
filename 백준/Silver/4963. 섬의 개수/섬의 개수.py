import sys

sys.setrecursionlimit(1000000)

# dx, dy = 이동 방향(상, 우상, 우, 우하, 하, 좌하, 좌, 좌상 순서)
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0 , -1]


# 이동 가능한 지역을 탐색하는 dfs 함수 정의
def dfs(graph, x, y):
    graph[y][x] = 0  # 현재 배추 위치 방문 확인
    for direction in range(8):  # 새로운 좌표를 nx, ny에 저장
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 새로운 좌표가 유효한 범위이면서 육지인 경우
        if 0 <= nx < w and 0 <= ny < h and graph[ny][nx] == 1:
            dfs(graph, nx, ny)


while True:
    w, h = map(int, input().split())    # w = 가로, h = 세로
    if w == 0 and h == 0:   # 0 0 을 입력받으면 반복문 종료
        break
    map_graph = [list(map(int,input().split())) for _ in range(h)]


    # land_count = 대륙 수 저장
    land_count = 0
    for col in range(h):
        for row in range(w):
            if map_graph[col][row] == 1:  # 탐색하지 않은 육지가 발견되는 경우
                dfs(map_graph, row, col)  # dfs 함수 실행
                land_count += 1  # 필요한 배추벌레 수 1 추가
    print(land_count)