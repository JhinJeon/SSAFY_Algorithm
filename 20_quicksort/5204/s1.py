# 퀵 정렬
import sys
sys.stdin = open('sample_input.txt')


def quicksort(arr, idx):
    global result, is_sort, case
    # 이미 정렬된 상태이면 추가 탐색 중단
    if is_sort:
        return

    left = arr[:idx//2]
    right = arr[idx//2:]

    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 더 큰 경우
    if left and right and left[-1] > right[-1]:
        case += 1
        
    for l in range(len(left)-1):
        # 뒤의 수가 더 작으면 자리 맞바꾸기
        if left[l] > left[l+1]:
            left[l], left[l+1] = left[l+1], left[l]

    for u in range(len(right)-1):
        # 뒤의 수가 더 작으면 자리 맞바꾸기
        if right[u] > right[u+1]:
            right[u], right[u+1] = right[u+1], right[u]
        
    arr = left + right
    # 정렬을 더 해야 하는 경우
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            quicksort(arr, i+1)
        # 재귀호출 중 정렬된 케이스가 있으면 추가 탐색 중단
        if is_sort:
            break
    # 최적의 결과가 나온 경우 정렬 완료 처리 후 결과 적용
    else:
        result = list(arr)
        is_sort = True
        return


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    array = list(map(int, input().split()))
    standard = n//2
    result = []
    is_sort = False     # 정렬 여부 확인용
    case = 0            # 왼쪽 원소 마지막 > 오른쪽 원소 마지막인 경우의 수
    quicksort(array, 0)
    answer = result[n//2]
    print(f'#{tc}', answer, case)