# 퀵 정렬(로무토 방식)
import sys
sys.stdin = open('sample_input.txt')


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


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    array = list(map(int, input().split()))
    quick_sort(array, 0, len(array)-1)