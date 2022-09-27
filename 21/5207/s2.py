# 이진 탐색
# 시간초과 발생
import sys
sys.stdin = open('sample_input.txt')


# list_a 정렬용(병합정렬)
def merge(left, right):
    merged_arr = []
    i, j = 0, 0  # 왼쪽, 오른쪽 리스트 각각의 인덱스

    while i < len(left) and j < len(right):
        # 왼쪽 리스트의 원소가 작거나 같으면 삽입
        if left[i] <= right[j]:
            merged_arr.append(left[i])
            i += 1
        # 오른쪽 리스트의 원소가 작으면 삽입
        else:
            merged_arr.append(right[j])
            j += 1

    # 왼쪽과 오른쪽 리스트 중 하나라도 원소를 모두 소모하면, 남은 리스트의 원소를 모두 삽입
    merged_arr.extend(left[i:])
    merged_arr.extend(right[j:])

    return merged_arr


def merge_sort(arr):
    # 더 이상 분할할 수 없는 경우(종료 조건)
    if len(arr) <= 1:
        return arr

    # 1. 리스트를 분할하여 각각 정렬
    middle = len(arr) // 2
    left_arr = merge_sort(arr[:middle])
    right_arr = merge_sort(arr[middle:])

    # 2. 정렬된 두 리스트를 병합
    return merge(left_arr, right_arr)


# 정렬된 list_a에서 값 b를 찾는 용도
def binary_search(arr, l, r, find_value):   # l = 0번 인덱스, r = len(arr)-1번 인덱스
    global case
    if len(arr) <= 2:   # 길이가 2 이하인 경우 l과 r이 겹침(케이스 합산)
        case += 1
        return
    pivot = (l + r)//2
    left = arr[:pivot]
    right = arr[pivot:]
    if find_value in left:
        binary_search(left, 0, len(left)-1, b)
    elif find_value in right:
        binary_search(right, 0, len(right)-1, b)


t = int(input())

for tc in range(1,t+1):
    n, m = map(int, input().split())
    list_a = list(map(int, input().split()))        # n개의 정수 저장
    list_b = list(map(int, input().split()))        # m개의 정수 저장
    case = 0
    merge_sort(list_a)     # list_a 정렬

    for b in list_b:
        binary_search(list_a, 0, n-1, b)
    print(f'#{tc}', case)