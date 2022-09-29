# 프림(PRIM)


def prim(start):
    visited = [False] * (n+1)
    distance = [INF] * (n+1)
    distance[start] = 0
    cost = 0

    # 정점의 개수만큼 반복하며 모든 정점을 이은 MST 생성
    for _ in range(n):
        # 1. MST의 정점에서 이동할 수 있는 모든 정점들 중 가장 적은 비용으로 이동 가능한 정점 찾기(그리디)
        min_dist = INF
        for i, dist in enumerate(distance):
            # 더 작은 값을 발견한 경우 해당 값으로 수정
            if not visited[i] and dist < min_dist:
                min_node = i
                min_dist = dist

        # 2. 해당 정점을 MST에 포함한 후 비용 합산
        visited[min_node] = True
        cost += min_dist

        # 3. 해당 정점과 인접한 정점에 대해 최소 비용 갱신
        for next_node, dist in graph[min_node]:
            if not visited[next_node] and dist < distance[next_node]:
                distance[next_node] = dist

    return cost



n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = 99999999          # 임의의 큰 수

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

print(prim(1))      # 1번 정점붙 시작