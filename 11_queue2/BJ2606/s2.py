# 바이러스
# bfs

import sys
sys.stdin = open('input.txt')


def bfs(start):
    visited = [False] * (n+1)
    visited[start] = True    # 시작 지점은 방문 처리
    queue = [start]    # BFS 탐색 상태(큐)
    total = 0   # 추가로 감염된 컴퓨터 수

    while queue:
        node = queue.pop(0)
        for next_computer in network_status[node]:    # 연결된 컴퓨터들 탐색
            if not visited[next_computer]:      # 방문하지 않은 컴퓨터가 있으면
                visited[next_computer] = True   # 방문 처리
                queue.append(next_computer)     # 탐색 상태 큐에 추가
                total += 1      # 감염된 컴퓨터 수 + 1

    return total


computer = int(input())
n = int(input())
answer = 0
network_status = [[] for _ in range(computer+1)]    # 연결 정보

for _ in range(n):
    a, b = map(int, input().split())
    network_status[a].append(b)
    network_status[b].append(a)

print(bfs(1))