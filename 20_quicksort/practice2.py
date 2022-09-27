
# 전위 순회
def front_search(k):
    # 현재 위치 출력
    print(node_value[k], end=' ')
    # 왼쪽 자식 정보가 있는 경우
    if left_child[k]:
        front_search(left_child[k])
    # 오른쪽 자식 정보가 있는 경우
    if right_child[k]:
        front_search(right_child[k])
    # 다 찾고 루트 노드로 돌아왔으면 반복 종료
    if k == 1:
        return


# 중위 순회
def mid_search(k):
    # 왼쪽 자식 정보가 있는 경우
    if left_child[k]:
        mid_search(left_child[k])
    # 현재 위치 출력
    print(node_value[k], end=' ')
    # 오른쪽 자식 정보가 있는 경우
    if right_child[k]:
        mid_search(right_child[k])
    # 다 찾고 루트 노드로 돌아왔으면 반복 종료
    if k == 1:
        return


# 후위 순회
def rear_search(k):
    # 왼쪽 자식 정보가 있는 경우
    if left_child[k]:
        rear_search(left_child[k])
    # 오른쪽 자식 정보가 있는 경우
    if right_child[k]:
        rear_search(right_child[k])
    # 현재 위치 출력
    print(node_value[k], end=' ')
    # 다 찾고 루트 노드로 돌아왔으면 반복 종료
    if k == 1:
        return


n, m = map(int,input().split())         # n = 노드 개수, m = 연결 관계 개수

node_value = [i for i in range(n+1)]    # 노드 값
left_child = [0] * (n+1)                # 노드(인덱스)의 왼쪽 자식(값) 정보
right_child = [0] * (n+1)               # 노드(인덱스)의 오른쪽 자식(값) 정보

node_info = list(map(int, input().split()))     # 노드의 연결 관계(부모-자식) 입력

for i in range(m):
    # 노드 번호에 값 저장
    node_idx = node_info[i * 2]
    # 왼쪽 자식 정보가 없으면 왼쪽 자식부터 추가
    if not left_child[node_idx]:
        left_child[node_idx] = node_info[2 * i+1]
    # 이미 왼쪽 자식이 있는 경우 오른쪽 자식 추가
    else:
        right_child[node_idx] = node_info[2 * i+1]

print('전위 순회 :', end=' ')
front_search(1)
print()
print('중위 순회 :', end=' ')
mid_search(1)
print()
print('후위 순회 :', end=' ')
rear_search(1)
print()
