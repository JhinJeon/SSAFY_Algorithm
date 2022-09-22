# 최대 상금
import sys
sys.stdin = open('input.txt')


def numswap(arr, count_remain):
    global case
    if not count_remain:
        num_result = ""
        for n in numpad:
            num_result += str(n)
        case.append(num_result)
        return

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            numswap(arr, count_remain - 1)
            arr[i], arr[j] = arr[j], arr[i]
    return



t = int(input())

for tc in range(1,t+1):
    numpad, swapcount = input().split()
    swapcount = int(swapcount)
    numpad = list(numpad)
    case = []       # 경우의 수 저장용
    # 스왑 횟수를 소진하면서 큰 수가 되도록 정렬
    # 큰 수 부터 앞쪽으로 이동, 큰 수와 가장 앞쪽의 수 맞바꾸기

    numswap(numpad, swapcount)

    answer = 0
    for c in case:
        c = int(c)
        if c > answer:
            answer = c

    print(f'#{tc}', answer)