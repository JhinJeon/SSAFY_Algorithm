# 최소 이동 거리

import sys
sys.stdin = open('sample_input.txt')


# 현재 위치를 기준으로 각 노드까지의 최단 거리를 반환하는 함수 dijkstra
def dijkstra(start):
    visited = [False] * (n + 1)
    visited[start] = True
    distance[start] = 0

    # 최단 거리 초기화
    for e, w in graph[start]:
        distance[e] = w

    # 시작 정점을 제외한 나머지 정점에 대해 반복
    for _ in range(n):
        # 1. MST의 정점에서 이동할 수 있는 모든 정점들 중 가장 적은 비용으로 이동 가능한 정점 찾기(그리디)
        min_dist = INF
        for i in range(1, n+1):
            # 아직 방문하지 않은 노드 방향의 비용이 더 작은 값을 발견한 경우 해당 값으로 수정
            if not visited[i] and distance[i] < min_dist:
                min_node = i
                min_dist = distance[i]

        # 2. 해당 정점을 MST에 포함한 후 비용 합산
        visited[min_node] = True

        # 3. 해당 정점과 인접한 정점에 대해 최소 비용 갱신
        for next_node, dist in graph[min_node]:
            new_dist = distance[min_node] + dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist


t = int(input())
INF = 99999999          # 임의의 큰 수

for tc in range(1, t+1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(m)]      # 연결 정보
    distance = [INF] * (n+1)            # 거리 정보

    for _ in range(m):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    # 0번 지점을 기준으로 각 지점까지의 최단거리 탐색
    dijkstra(0)
    # 끝(n번) 지점까지의 거리만 출력
    print(f'#{tc} {distance[n]}')
