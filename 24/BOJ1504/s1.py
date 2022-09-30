# 특정한 최단 경로
import sys
sys.stdin = open('input2.txt')

from heapq import heappop, heappush


def primheap(k):    # k = 탐색 시작점
    global n
    explorer = [(0, k)]         # (거리, 노드 번호)
    visited = [False] * (n+1)       # 노드 방문 여부 체크
    cost = 0

    while explorer:
        d, node = heappop(explorer)
        # 이미 방문한 지역이면 continue
        if visited[node]:
            continue

        # 새로운 지역 방문 처리 후 거리 가산
        visited[node] = True
        cost += d

        for next_node, next_distance in connection_info[node]:
            if not visited[next_node]:
                heappush(explorer, (next_distance, next_node))

    return cost


n , e = map(int, input().split())   # n = 노드 수, e = 간선 수

# 연결 정보 입력
connection_info = [[] for _ in range(n+1)]
for _ in range(e):
    d1, d2, weight = map(int, input().split())
    connection_info[d1].append((d2, weight))
    connection_info[d2].append((d1, weight))

start, end = map(int, input().split())      # 반드시 거쳐야 하는 정점들

answer = primheap(start)

if answer == 0:
    answer = -1

print(answer)
