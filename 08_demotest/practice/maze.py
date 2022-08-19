# 미로에서 출발점에서 도착점까지의 경로를 출력하시오.
import sys
sys.stdin = open('maze_input.txt')

def dfs(x, y):
    visited[x][y] = True  # 방문처리
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maze[nx][ny] == 0:
            road.append((nx, ny))  # 경로에 포함

            # 도착점이면 경로를 출력
            if nx == n - 1 and ny == m - 1:
                print(road)
                return road

            dfs(nx, ny)  # 다음 칸 이동
            road.pop()  # 되돌아가면서 이전 경로 삭제


n, m = map(int, input().split())  # 행, 열
maze = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우
road = [(0, 0)]  # 출구까지의 경로

dfs(0, 0)
print(dfs(0, 0))  # (0,0) 정점에서 시작