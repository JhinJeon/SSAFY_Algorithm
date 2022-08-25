# 미로1(BFS)
import sys
sys.stdin = open('input.txt')

# 순서대로 상, 우, 하, 좌 이동
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


# 미로 탈출 가능 여부를 반환하는 bfs 함수 정의
def bfs(start_col, start_row):  # start_col = 시작 행 인덱스, start_row = 시작 열 인덱스
    visited[start_col][start_row] = True    # 시작 지점 방문 처리
    queue_status = [(start_col, start_row)]
    exit = 0    # 탈출 가능 여부[기본 = 0(불가능)]

    while queue_status:
        y, x = queue_status.pop(0)  # 큐에서 y, x 좌표 반환
        for direction in range(4):  # 현재 좌표에서 이동한 위치를 n_row, n_col에 저장
            n_row = x + dx[direction]
            n_col = y + dy[direction]

            # 새 인덱스가 미로 범위를 벗어나는지 확인
            if 0 <= n_row < 16 and 0 <= n_col < 16:
                # 목적지를 발견한 경우
                if miro[n_col][n_row] == 3: 
                    exit = 1    # 탈출 가능 처리 후 반복문 종료
                    break

                # 추가로 탐색 가능한 지점을 발견한 경우
                if not visited[n_col][n_row] and miro[n_col][n_row] == 0:   
                    queue_status.append((n_col, n_row))     # 큐에 추가하고 반복 처리
                    visited[n_col][n_row] = True

        if exit == 1:   # 탈출이 가능한 경우 반복문 즉시 종료
            break
    # 큐가 비어서 반복문이 종료되는 경우 0(탈출 불가), break에 의해 종료된 경우 1(탈출 가능)
    return exit


for _ in range(1,11):
    tc = int(input())
    miro = [list(map(int,input())) for _ in range(16)]      # 미로 정보 저장
    visited = [[False] * 16 for _ in range(16)]     # 방문 여부 저장
    for col in range(16):
        for row in range(16):
            if miro[col][row] == 2:     # 시작 지점을 찾은 경우
                print(f'#{tc}', bfs(col, row))      # bfs 탐색 진행 후 결과 출력