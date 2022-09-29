# 여행 가자
# 모든 목적지가 연결된 도시들을 거쳐서 출발점으로 갈 수 있는지 확인
import sys
sys.stdin = open('input.txt')


# 끝까지 거슬러 올라가서 근본 부모 노드를 찾는 함수(경로 압축)
def find_set(node):
    if node != parent[node]:        # 부모 노드가 자기 자신이 아니면 반복
        parent[node] = find_set(parent[node])
    # 부모 노드가 자기 자신이면 해당 값 반환(대표값)
    return parent[node]


# # 바로 위의 부모 노드를 찾는 함수
# def find_set(node):
#     while node != parent[node]:
#         node = parent[node]
#     return node


def union(x_root, y_root):
    if x_root != y_root:
        if x_root < y_root:
            parent[y_root] = x_root
        else:
            parent[x_root] = y_root


n = int(input())
m = int(input())
parent = list(range(n+1))

# Union
for i in range(n):
    line = input().split()
    for j in range(n):
        if line[j] == '1':
            i_root, j_root = find_set(i+1), find_set(j+1)
            union(i_root, j_root)

plans = list(map(int, input().split()))
root = find_set(plans[0])

for i in range(1, m):
    if root != find_set(plans[i]):
        answer = 'NO'
        break
else:
    answer = 'YES'

print(answer)