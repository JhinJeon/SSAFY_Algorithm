import sys
sys.stdin = open('sample_input.txt')


def enque(k):
    global last

    # 힙에 추가
    last += 1
    heap[last] = k

    # 최소 힙에 맞게 조정하는 과정..?
    child = last
    parent = child // 2
    while parent and heap[parent] > heap[child]:  # 부모 노드가 유효하고(0이 아니고) 비교했을 때
        heap[parent], heap[child] = heap[child], heap[parent]  # 자식 노드의 값이 더 작다면 swap 해준다.

        # 1레벨 위로 이동
        child = parent
        parent = child // 2


t = int(input())

for tc in range(1, t+1):
    # n = 노드 개수
    n = int(input())
    node_info = list(map(int,input().split()))      # 노드에 입력할 값 정보
    last = 0
    answer = 0
    
    # 최소 힙을 만드는 반복문
    heap = [0] * 1000000
    for val in node_info:
        enque(val)

    # 조상의 합을 구하는 과정
    while True:
        last //= 2  # 부모 노드로 이동
        answer += heap[last]  # answer에 노드 값을 더한다.
        if not last:  # root까지 왔다면 break
            break
    print(f'#{tc}', answer)