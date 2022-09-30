# heapq X prim

from heapq import heappush, heappop


def prim(start):
    visited = [False] * (n + 1)
    heap = [(0, start)]  # 힙 선언[(비용, 정점)]
    cost = 0

    while heap:
        min_dist, min_node = heappop(heap)
        if visited[min_node]:
            continue

        # 2. 해당 정점을 MST에 포함한 후 비용 합산
        visited[min_node] = True
        cost += min_dist

        # 3. 해당 정점과 인접한 정점에 대해 최소 비용 갱신
        for next_node, dist in graph[min_node]:
            if not visited[next_node]:
                heappush(heap, (dist, next_node))

    return cost


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
INF = 99999999  # 임의의 큰 수

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

print(prim(1))  # 1번 정점붙 시작
