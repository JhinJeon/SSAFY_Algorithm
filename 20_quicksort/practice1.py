# 퀵 정렬
import sys
sys.stdin = open('test1.txt')


def quicksort(arr, idx):
    global result, is_sort
    # 이미 정렬된 상태이면 추가 탐색 중단
    if is_sort:
        return
    pivot = arr[idx]    # 퀵 정렬 기준 숫자
    # pivot에 해당하는 수와 중복되는 숫자가 있는지 확인
    pivot_identical = arr.count(pivot)

    # pivot보다 왼쪽에 있는 값들을 내림차순으로 정렬
    lower = []  # pivot보다 큰 값
    upper = []  # pivot보다 작은 값

    #
    for a in arr:
        if a < pivot:
            lower.append(a)
        elif a > pivot:
            upper.append(a)

    for l in range(len(lower)-1):
        # 뒤의 수가 더 크면 자리 맞바꾸기
        if lower[l] < lower[l+1]:
            lower[l], lower[l+1] = lower[l+1], lower[l]

    for u in range(len(upper)-1):
        if upper[u] < upper[u+1]:
            upper[u], upper[u+1] = upper[u+1], upper[u]

    arr = upper + [pivot] * pivot_identical + lower
    # 정렬을 더 해야 하는 경우
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
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
    array = list(map(int, input().split()))
    result = []
    is_sort = False     # 정렬 여부 확인용
    quicksort(array, 0)
    print(f'#{tc}', *result)
