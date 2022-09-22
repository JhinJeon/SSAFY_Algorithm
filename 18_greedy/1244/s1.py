# 최대 상금
# 그리드 방식(결과가 정확하지 않음)

import sys
sys.stdin = open('debug_input.txt')

t = int(input())

for tc in range(1,t+1):
    numpad, swapcount = input().split()
    swapcount = int(swapcount)
    numpad = list(numpad)

    # 스왑 횟수를 소진하면서 큰 수가 되도록 정렬
    # 큰 수 부터 앞쪽으로 이동, 큰 수와 가장 앞쪽의 수 맞바꾸기

    while swapcount:
        
        front_idx = 0
        front_val = 10
        for i in range(len(numpad)):        # i = 바꾸는 범위의 맨 앞쪽의 수
            if front_val >= int(numpad[i]): # i = 앞쪽 방향의 수들 중 가장 작은 수(중복값이 있는 경우 앞쪽 우선)
                front_val = int(numpad[i])
                front_idx = i

        rear_idx = -1
        rear_val = 0
        for j in range(len(numpad)-1, i, -1):  # j = 뒤쪽에 숨어있는 가장 큰 수(중복값이 있는 경우 뒤쪽 우선)
            if rear_val < int(numpad[j]):
                target_val = int(numpad[j])
                target_idx = j
                
        # 바꿀 숫자가 생긴 경우 서로의 위치 맞바꾸기
        if front_idx > 0 and rear_idx < -1 and front_val < rear_val:
            numpad[i], numpad[target_idx] = numpad[target_idx], numpad[i]
            swapcount -= 1
        # 바꿀 숫자가 없는 경우 반복문 종료
        else:
            break
            
    # 스왑 횟수가 남은 경우 횟수가 소진될 때까지 맨 끝 자릿수와 앞쪽에서 가장 작은 수와 맞바꾸기
    else:
        # 같은 수가 없는 경우 맨 끝 자릿수와 앞쪽에서 가장 작은 수와 맞바꾸기
        if len(set(numpad)) == len(numpad):
            last_no = numpad[-1]                # numpad의 맨 마지막 숫자
            target_idx = -2                     # 바꿀 값의 인덱스 번호
            swap_range = numpad[:target_idx]    # 바꿀 대상 범위
            for s in range(len(swap_range)):
                if swap_range[s] < last_no:
                    last_no = swap_range[s]
                    target_idx = s
            while swapcount:
                numpad[target_idx], numpad[-1] = numpad[-1], numpad[target_idx]
                swapcount -= 1

    print(f'#{tc} ', *numpad, sep="")