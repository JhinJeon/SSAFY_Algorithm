# 미로
import sys
sys.stdin = open('sample_input.txt')


t = int(input())

# 이동 방향 : 상, 우, 하, 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


# 미로의 출구를 찾을 수 있는지를 판단하는 maze_search 함수 정의
def maze_search(x, y):
    global result   # result = 출구를 찾을 수 있으면 1, 없으면 0
    visited[y][x] = True    # 현재 위치 방문 처리
    for direction in range(4):  # 현재 위치에서 dx, dy만큼 이동(상, 하, 좌, 우)
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 새로운 좌표가 유효한 범위이며 방문하지 않은 경우
        if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
            if miro[ny][nx] == 3:   # 출구를 찾은 경우
                result = 1
                return
            elif miro[ny][nx] == 0: # 탐색 가능한 구역이 있는 경우
                maze_search(nx, ny)



for tc in range(1,t+1):
    n = int(input())
    miro = [list(map(int,input())) for _ in range(n)]   # 미로 배열
    visited = [[False] * n for _ in range(n)]   # 방문 여부 확인
    result = 0  # 출구 탐색 가능 여부(기본값 : 불가능)
    for col in range(n):
        for row in range(n):
            if miro[col][row] == 2:    # 시작 지점을 찾은 경우
                maze_search(row, col)   # 시작 지점을 기준으로 maze_search 함수 실행

    # answer : 출구를 찾을 수 있는 경우 1, 그렇지 못하는 경우 0
    if result == 1:
        answer = 1
    else:
        answer = 0

    print(f'#{tc}', answer)
