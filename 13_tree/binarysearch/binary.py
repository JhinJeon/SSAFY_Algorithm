# 이진탐색

import sys
sys.stdin = open('sample_input.txt')


# 중위 탐색을 진행하는 함수 inorder
def inorder(k):
    global value
    # 왼쪽 자식 노드의 번호가 최대 노드 개수보다 작은 경우
    if k * 2 <= n:
        inorder(2 * k)
    node_info[k] = value
    value += 1

    # 오른쪽 자식 노드의 번호가 최대 노드 개수보다 작은 경우
    if k * 2 + 1 <= n:
        inorder(2 * k + 1)

t = int(input())


for tc in range(1,t+1):
    n = int(input())
    node_info = [0] * (n+1)     # 노드 정보

    # 루트 노드를 기준으로 탐색
    value = 1
    inorder(1)

    answer = node_info[n//2]
    print(f'#{tc}', answer)

