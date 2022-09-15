def enq(n):
    global last

    # 힙에 추가
    last += 1
    heap[last] = n

    # 최소 힙에 맞게 조정하는 과정..?
    c = last
    p = c // 2
    while p and heap[p] > heap[c]:  # 부모 노드가 유효하고(0이 아니고) 비교했을 때
        heap[p], heap[c] = heap[c], heap[p]  # 자식 노드의 값이 더 작다면 swap 해준다.

        # 1레벨 위로 이동
        c = p
        p = c // 2


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    heap = [0] * 1000000  # N이 최대 1000000까지 가능!
    last = 0
    answer = 0

    # 최소 힙을 만드는 반복문
    for number in numbers:
        enq(number)

    # 조상의 합을 구하는 과정
    while True:
        last //= 2  # 부모 노드로 이동
        answer += heap[last]  # answer에 노드 값을 더한다.
        if not last:  # root까지 왔다면 break
            break
    print(f"#{tc} {answer}")