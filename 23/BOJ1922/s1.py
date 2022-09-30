# 네트워크 발생

import sys

sys.stdin = open('input.txt')

# 끝까지 거슬러 올라가서 근본 부모 노드를 찾는 함수(경로 압축)
def find_set(node):
    if node != parent[node]:  # 부모 노드가 자기 자신이 아니면 반복
        parent[node] = find_set(parent[node])
    # 부모 노드가 자기 자신이면 해당 값 반환(대표값)
    return parent[node]


n = int(input())
m = int(input())
network = []

for _ in range(m):
    s, e, w = map(int, input().split())  # w = 비용, s, = 출발 노드, e = 도착 노드
    network.append((w, s, e))

network.sort()  # 비용을 기준으로 오름차순

parent = list(range(n + 1))
counts = 0  # 간선 개수(개수가 (정점-1)개가 되면 종료)
cost = 0  # 총 비용

for w, x, y in network:
    x_root, y_root = find_set(x), find_set(y)

    # 부모 노드가 다른 경우(아직 연결 관계가 기록되지 않은 경우) 연결 관계 형성
    if x_root != y_root:
        parent[y_root] = x_root
        cost += w
        counts += 1

        if counts >= n - 1:
            break

print(cost)
