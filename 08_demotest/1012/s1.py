# 유기농 배추
import sys
sys.setrecursionlimit(10000000)
sys.stdin = open('input.txt')

# dx, dy = 이동 방향(상, 하, 좌, 우 순서)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 배추벌레가 활동 가능한 영역을 계산하는 dfs 함수 정의
def dfs(graph, x, y):
    graph[y][x] = 0 # 현재 배추 위치 방문 확인
    for direction in range(4):  # 새로운 좌표를 nx, ny에 저장
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        # 새로운 좌표가 유효한 범위이면서 활동 가능한 배추가 있는 경우
        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
            dfs(graph, nx, ny)



t = int(input())

for tc in range(1, t + 1):
    # m = 가로, n = 세로, k = 심을 배추 수
    m, n, k = map(int, input().split())
    farm = [[0] * m for _ in range(n)]
    
    # 배추의 위치 저장
    for position in range(k):
        row, col = map(int, input().split())
        farm[col][row] = 1
        
    # bug_count = 필요한 배추벌레 수 저장
    bug_count = 0
    for col in range(n):
        for row in range(m):
            if farm[col][row] == 1: # 활동하지 않은 배추가 발견되는 경우
                dfs(farm, row, col) # dfs 함수 실행
                bug_count += 1  # 필요한 배추벌레 수 1 추가
    print(bug_count)
