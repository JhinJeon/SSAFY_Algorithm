# 대표값 탐색 함수
# 끝까지 거슬러 올라가서 근본 부모 노드를 찾는 함수(경로 압축)
# def find_set(node):
#     if node != parent[node]:        # 부모 노드가 자기 자신이 아니면 반복
#         parent[node] = find_set(parent[node])
#     # 부모 노드가 자기 자신이면 해당 값 반환(대표값)
#     return parent[node]


# 바로 위의 부모 노드를 찾는 함수
def find_set(node):
    while node != parent[node]:
        node = parent[node]
    return node


n, m = map(int, input().split())       # 정점, 간선(union) 개수
parent = list(range(n+1))               # 부모 노드의 정보

for _ in range(m):
    x, y = map(int, input().split())
    x_root, y_root = find_set(x), find_set(y)

    # Union
    if x_root != y_root:        # root(대표)가 다른 경우 병합(부모-자식 관계 생성)
        # root가 작은 값에 큰 값을 자식으로 붙이기
        if x_root < y_root:
            parent[y_root] = x_root
        else:
            parent[x_root] = y_root

for i in range(1, n+1):
    print(find_set(i), end=' ')

print()
print(parent)
