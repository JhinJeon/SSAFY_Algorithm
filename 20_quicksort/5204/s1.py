# 병합 정렬
import sys

sys.stdin = open('sample_input.txt')


def div(arr):
    if len(arr) <= 1:
        return arr
    std = len(arr) // 2
    left = div(arr[:std])
    right = div(arr[std:])
    return con(left, right)


def con(left_arr, right_arr):
    global case
    result = []
    i, j = 0, 0
    while len(left_arr) > i and len(right_arr) > j:    # l, r 둘다 원소가 존재할 때
        if left_arr[i] <= right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1
    while len(left_arr) > i:           # l 원소만 남았을때
        result.append(left_arr[i])
        if i == len(left_arr) - 1:     # l의 마지막이 r보다 클때 카운트
            case += 1
        i += 1
    while len(right_arr) > j:           # r 원소만 남았을 때
        result.append(right_arr[j])
        j += 1
    return result               # 정렬한 리스트 반환


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    array = list(map(int, input().split()))
    standard = n//2
    case = 0            # 왼쪽 원소 마지막 > 오른쪽 원소 마지막인 경우의 수
    print(f'#{tc}', div(array)[standard], case)
