# 이진 탐색
# 런타임 에러 발생
import sys
sys.stdin = open('sample_input.txt')


# list_a 정렬용(로무토 방식 퀵 정렬)
# 가장 오른쪽 원소를 피벗으로 지정
def partition(arr, left, right):
    pivot = arr[right]   # 피벗 = 가장 왼쪽 원소
    i, j = left-1, left     # i는 0번 인덱스보다 왼쪽의 가상의 공간에서 시작
    while j < right:
        # 피벗보다 작은 값을 왼쪽에, 피벗보다 큰 값을 오른쪽에 보내기
        if pivot > arr[j]:
            i += 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        j += 1

    # i가 -1인 경우 right와 동일한 값을 가리키게 됨
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i + 1


def quick_sort(arr, left, right):
    if left < right:
        middle = partition(arr, left, right)
        quick_sort(arr, left, middle - 1)
        quick_sort(arr, middle + 1, right)
    return False


# 정렬된 list_a에서 값 b를 찾는 용도
def binary_search(find_value):
    global case
    check = 0   # 1 = 왼쪽, 2 = 오른쪽
    l, r = 0, n-1  # l = 0번 인덱스, r = len(arr)-1번 인덱스
    while l <= r:
        mid = (l + r) // 2
        if list_a[mid] == find_value:
            case += 1
            return
        elif list_a[mid] > find_value:
            if check == 1:
                break
            check = 1
            r = mid - 1
        else:
            if check == 2:
                break
            check = 2
            l = mid + 1
    return


t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    list_a = list(map(int, input().split()))        # n개의 정수 저장
    list_b = list(map(int, input().split()))        # m개의 정수 저장
    case = 0
    quick_sort(list_a, 0, n-1)      # list_a 정렬
    for b in list_b:
        binary_search(b)
    print(f'#{tc}', case)
