# 크루스칼 알고리즘(신장 트리)

# # 연결된 노드(직전 부모 노드)를 찾아주는 함수
# def find_set(node):
#     while node != parent[node]:
#         node = parent[node]
#     return node


# 끝까지 거슬러 올라가서 근본 부모 노드를 찾는 함수(경로 압축)
def find_set(node):
    if node != parent[node]:        # 부모 노드가 자기 자신이 아니면 반복
        parent[node] = find_set(parent[node])
    # 부모 노드가 자기 자신이면 해당 값 반환(대표값)
    return parent[node]


n, m = map(int, input().split())    # 정점, 간선 개수
edges = []                          # 간선 별 비용 정보

for _ in range(m):
    s, e, w = map(int, input().split())
    edges.append((w, s, e))

edges.sort()                        # 비용을 기준으로 오름차순

parent = list(range(n+1))
counts = 0      # 간선 개수(개수가 (정점-1)개가 되면 종료)
cost = 0        # 가중치 총합

for dist, x, y in edges:
    x_root, y_root = find_set(x), find_set(y)

    if x_root != y_root:
        parent[y_root] = x_root
        cost += dist
        counts += 1

        if counts >= n-1:
            break

print(cost)