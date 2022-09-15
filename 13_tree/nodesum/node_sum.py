import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1, t+1):
    # n = 노드 개수
    # m = 리프 노드의 개수(자식이 없는 노드 수)
    # n = 값을 구하려는 노드 번호
    n, m, l = map(int, input().split())
    node_info = list([0] * (n + 1))      # 인덱스 = 노드 번호, 값 = 노드에 저장된 수
    # node_info에 리프 노드 정보 저장
    for _ in range(m):
        idx, val = map(int, input().split())
        node_info[idx] = val

    child = n               # n번 노드부터 탐색 시작
    parent = child // 2     # parent의 번호는 child 번호를 2로 나눈 값의 몫

    # 가장 마지막 번호인 노드부터 순차적으로 탐색
    while parent > 0:
        node_info[parent] += node_info[child]
        child -= 1
        parent = child // 2

    print(f'#{tc}', node_info[l])