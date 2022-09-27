# 퀵 정렬(호어 방식)
import sys
sys.stdin = open('sample_input.txt')


# 가장 왼쪽 원소를 피벗으로 지정
def partition(arr, left, right):
    pivot = arr[left]   # 피벗 = 가장 왼쪽 원소
    i, j = left, right
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1

        while i <= j and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            print(arr)

    arr[left], arr[j] = arr[j], arr[left]
    print(arr)
    return j


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