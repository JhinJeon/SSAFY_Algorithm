# 특정한 최단 경로
# 다익스트라

import sys
sys.stdin = open('input.txt')

from heapq import heappop, heappush


# start에서 각 노드까지 도달하는 최단거리 반환
# end번 인덱스에 저장된 값이 start에서 end로 향하는 최단거리
def dijkstra(start, end):
    distance = [INF] * (n + 1)
    distance[start] = 0
    heap_status = [(0, start)]

    # 현재 노드에 저장된 가중치와 노드 번호 반환
    while heap_status:
        weight, node = heappop(heap_status)

        # 더 이상 가중치 최적화를 할 수 없는 경우
        if weight > distance[node]:
            continue

        # 해당 정점과 인접한 정점에 대해 최소 비용 갱신 및 추가 탐색
        for next_dist, next_node in connection_info[node]:
            new_dist = weight + next_dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(heap_status, (new_dist, next_node))

    # end번 인덱스의 값은 start에서 end로 향하는 최단거리
    return distance[end]


# 연결 정보 입력
n, e = map(int, input().split())   # n = 노드 수, e = 간선 수
connection_info = [[] for _ in range(n+1)]
INF = 99999999  # 임의의 큰 수
for _ in range(e):
    d1, d2, weight = map(int, input().split())
    connection_info[d1].append((weight, d2))
    connection_info[d2].append((weight, d1))

s, e = map(int, input().split())      # 반드시 거쳐야 하는 정점들

# 출발지부터 - start - end - n 간의 이동하는 경우의 수 고려
case1 = dijkstra(1, s) + dijkstra(s, e) + dijkstra(e, n)
case2 = dijkstra(1, e) + dijkstra(e, s) + dijkstra(s, n)

# 유효한 경로가 없는 경우 -1
if case1+ case2 > INF:
    answer = -1
else:
    answer = min(case1, case2)

print(answer)
