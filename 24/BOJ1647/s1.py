# 도시 분할 계획
# 20분 소요
# 이전 코드는 연결 정보를 저장하는 path_info를 path개 만큼만 채워 놓아서 인덱스 에러가 발생했다.

import sys
sys.stdin = open('input.txt')

from heapq import heappush, heappop


def prim(start):
    cost_array = []     # 길 비용 리스트
    path_heap = [(0, start)]  # 힙 선언(비용, 정점)

    while path_heap:
        distance, station = heappop(path_heap)
        # 기존에 방문한 정점이었다면 continue
        if visited[station]:
            continue

        # 아직 방문하지 않았으면 방문 처리
        visited[station] = True
        cost_array.append(distance)

        # 현재 정점에서 이동 가능한 다른 정점들 살펴보기
        for next_node, weight in path_info[station]:
            if not visited[next_node]:
                heappush(path_heap, (weight, next_node))

    return cost_array


home, path = map(int, input().split())

visited = [False] * (home + 1)
path_info = [[] for _ in range(home + 1)]

for _ in range(path):
    home_a, home_b, w = map(int, input().split())  # w = home_a에서 home_b를 가는 데 소모되는 비용
    # 양방향으로 이동 비용 추가
    path_info[home_a].append((home_b, w))
    path_info[home_b].append((home_a, w))

# 가장 비싼 길을 끊어서 두 개의 마을로 나누기
result = prim(1)
print(sum(result) - max(result))
