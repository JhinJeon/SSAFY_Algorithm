# 최대 상금
# 탐색 과정 출력 기능

import sys
sys.stdin = open('input.txt')


def numswap(arr, count_remain):
    global case, answer, process
    num_result = int("".join(arr))
    # 동일한 탐색 깊이에서 이미 등장한 숫자인 경우 탐색 중단
    if (num_result, count_remain) in case:
        return

    # 현재 탐색 깊이와 숫자 정보를 튜플 형태로 저장
    case.add((num_result, count_remain))
    # 더 이상 위치 변경이 불가능한 경우
    if not count_remain:
        num_result = int("".join(arr))      # 리스트화한 값을 정수로 전환
        if answer < num_result:             # 최댓값을 경신하는 경우
            answer = num_result
            process = list(case)
        return

    # 앞쪽 숫자와 뒤쪽 숫자를 교환하는 모든 경우의 수 탐색(완전탐색)
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]     # 두 숫자의 위치 변경
            numswap(arr, count_remain - 1)      # 재귀 호출
            arr[i], arr[j] = arr[j], arr[i]     # 이후 원상복귀


t = int(input())

for tc in range(1, t+1):
    numpad, swapcount = input().split()
    swapcount = int(swapcount)      # 남은 위치 변경 가능 횟수
    numpad = list(numpad)           # 처음 입력받은 숫자를 리스트에 저장
    case = set()       # 경우의 수 저장용
    answer = 0         # 최댓값 저장용
    process = []       # 탐색 과정 저장용

    numswap(numpad, swapcount)

    print(f'#{tc}', answer)
    # process.sort(key=lambda x: x[1], reverse=True)
    print(process)
