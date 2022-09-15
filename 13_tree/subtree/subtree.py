import sys
sys.stdin = open('sample_input.txt')


# 서브 트리 노드의 개수를 세는 함수 nodecount
def nodecount(node_idx):   # node_idx = 현재 노드 번호
    global result
    if node_idx:   # n이 0이 아닌 경우
        nodecount(left_child[node_idx])
        nodecount(right_child[node_idx])
        result += 1


t = int(input())

for tc in range(1, t + 1):
    e, n = map(int, input().split())
    tree = list(map(int, input().split()))
    parent = [0] * (e + 2)                  # 노드의 부모 정보
    left_child = [0] * (e + 2)              # 노드의 왼쪽 자식 정보
    right_child = [0] * (e + 2)             # 노드의 오른쪽 자식 정보
    result = 0                              # 노드 개수 저장용
    for i in range(0, 2 * e, 2):
        par, chi = tree[i], tree[i + 1]     # 연결 관계 정보 가져오기

        # 부모 정보 추가
        parent[chi] = par

        # 자식 정보가 없으면 왼쪽 자식부터 추가
        if left_child[par] == 0:
            left_child[par] = chi
        # 왼쪽 자식이 등록되어 있으면 오른쪽 자식에 추가
        else:
            right_child[par] = chi

    nodecount(n)

    print(f'#{tc}', result)