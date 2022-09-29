# 그룹 나누기
# union-find 이용
import sys
sys.stdin = open('input.txt')


# 끝까지 거슬러 올라가서 근본 부모 노드를 찾는 함수(경로 압축)
def find_set(node):
    if node != parent[node]:        # 부모 노드가 자기 자신이 아니면 반복
        parent[node] = find_set(parent[node])
    # 부모 노드가 자기 자신이면 해당 값 반환(대표값)
    return parent[node]


t = int(input())

for tc in range(1,t+1):
    n, m = map(int,input().split())     # n = 신청자 수, m = 관계 수
    input_info = list(map(int,input().split()))
    parent = list(range(n+1))
    for i in range(0,m*2,2):
        x, y = input_info[i], input_info[i+1]
        x_root, y_root = find_set(x), find_set(y)

        # Union
        if x_root != y_root:  # root(대표)가 다른 경우 병합(부모-자식 관계 생성)
            # root가 작은 값에 큰 값을 자식으로 붙이기
            if x_root < y_root:
                parent[y_root] = x_root
            else:
                parent[x_root] = y_root

    # 1번부터 n번까지 부모 찾기(같은 부모 = 같은 팀)
    for i in range(1, n+1):
        find_set(i)

    answer = 0
    teams = []
    for i in range(1, n + 1):
        if parent[i] == 0:
            answer += 1
        elif parent[i] not in teams:
            teams.append(parent[i])
            answer += 1

    print(f'#{tc}', answer)