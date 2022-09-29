# 최단경로
from heapq import heappop, heappush


def dijkstra(start):
    heap = [(0, start)]     # 시작 점부터 시작 점까지의 거리는 0
    distance[start] = 0

    while heap:
        min_distance, min_node = heappop(heap)

        if min_distance > distance[min_node]:
            continue

        for next_node, dist in graph[min_node]:
            new_dist = min_distance + dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(heap, (new_dist, next_node))
    # 탐색하지 못한 노드의 경우 : 해당 노드까지 갈 수 있는 길이 없기 때문

v, e = map(int, input().split())
start_no = int(input())
graph = [[] for _ in range(v+1)]
INF = 10 * v
distance = [INF] * (v + 1)
for _ in range(e):
    u, v, weight = map(int, input().split())
    graph[u].append((v, weight))    # u번 정점에서 v번 정점을 갈 때 weight가중치(시간) 소모

dijkstra(start_no)

for i in range(1, len(distance)):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])