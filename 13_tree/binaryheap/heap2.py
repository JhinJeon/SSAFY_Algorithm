from heapq import heappush

t = int(input())

for tc in range(1, t+1):
    heap_tree = []
    n = int(input())
    val_list = list(map(int, input().split()))

    for i in range(n):
        heappush(heap_tree, val_list[i])
        if i == n - 1:
            last = i

    result = 0
    while n > 1:                # 마지막 노드의 조상 노드 합 구하기
        n = n // 2
        result += heap_tree[n - 1]

    print(f'#{tc}', result)
