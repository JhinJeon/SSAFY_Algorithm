# 다익스트라 알고리즘
from heapq import heappop, heappush

# 특정 정점에서 다른 모든 정점으로 향하는 최단거리
# 음의 간선이 없어야 사용 가능


def dijkstra(start):
    heap = [(0, start)]
    distance[start] = 0

    # 시작 정점을 제외한 나머지 정점에 대해 반복
    while heap:
        # 1. MST의 정점에서 이동할 수 있는 모든 정점들 중 가장 적은 비용으로 이동 가능한 정점 찾기(그리디)
        min_dist, min_node = heappop(heap)

        if min_dist > distance[min_node]:
            continue

        # 3. 해당 정점과 인접한 정점에 대해 최소 비용 갱신
        for next_node, dist in graph[min_node]:
            new_dist = min_dist + dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(heap, (new_dist, next_node))


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
INF = 99999999  # 임의의 큰 수
distance = [INF] * (n + 1)

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

dijkstra(1)  # 1번 정점부터 시작
print(distance)