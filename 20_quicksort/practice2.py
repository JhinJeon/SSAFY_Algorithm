import sys
sys.stdin = open('test2.txt')

<<<<<<< HEAD
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
=======

# 전위 순회 함수
def front_search(k):
    # 현재 노드 정보 출력
    print(node_value[k], end=' ')
    # 왼쪽 자식 노드 방문
    if left_child[k]:
        front_search(left_child[k])
    # 오른쪽 자식 노드 방문
    if right_child[k]:
        front_search(right_child[k])
    return


# 중위 순회 함수
def mid_search(k):
    # 왼쪽 자식 노드 방문
    if left_child[k]:
        mid_search(left_child[k])
    # 현재 노드 정보 출력
    print(node_value[k], end=' ')
    # 오른쪽 자식 노드 방문
    if right_child[k]:
        mid_search(right_child[k])


# 후위 순회 함수
def rear_search(k):
    # 왼쪽 자식 노드 방문
    if left_child[k]:
        rear_search(left_child[k])
    # 오른쪽 자식 노드 방문
    if right_child[k]:
        rear_search(right_child[k])
    # 현재 노드 정보 출력
    print(node_value[k], end=' ')


n, m = map(int,input().split())

node_value = [i for i in range(n + 1)]    # 노드 값 정보
left_child = [0] * (n+1)    # 노드(인덱스 번호)의 왼쪽 자식 정보
right_child = [0] * (n+1)   # 노드(인덱스 번호)의 오른쪽 자식 정보

node_info = list(map(int, input().split()))     # 노드 관계 정보 입력

for i in range(m):
    idx = node_info[2*i]        # 부모 노드 번호
    node_value[idx] = node_info[i * 2]      # 부모 노드의 값 추가
    # 왼쪽 자식 정보가 없으면 왼쪽 자식부터 추가
    if not left_child[idx]:
        left_child[idx] = node_info[2 * i+1]
    # 왼쪽 자식 정보가 있으면 오른쪽 자식에 추가
    else:
        right_child[idx] = node_info[2 * i+1]
>>>>>>> c6f28641cf9456dab114e19acfd7a72e60ca6376

print('전위 순회 :', end=' ')
front_search(1)
print()
print('중위 순회 :', end=' ')
mid_search(1)
print()
print('후위 순회 :', end=' ')
rear_search(1)
<<<<<<< HEAD
print()
=======
>>>>>>> c6f28641cf9456dab114e19acfd7a72e60ca6376
