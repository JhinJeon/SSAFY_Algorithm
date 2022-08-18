# 이진탐색
# while 반복 사용

import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1,t+1):
    # 책 페이지 수, a가 찾는 페이지, b가 찾는 페이지
    book, find_a, find_b = map(int,input().split())

    # a, b의 시도 횟수를 trial_a, trial_b에 저장
    trial_a = 0
    trial_b = 0

    # start a(b) : a(b)의 탐색 범위(처음, 끝)
    start_a = 1
    end_a = book
    start_b = 1
    end_b = book

    # a가 원하는 페이지를 찾는 데까지 시도한 횟수 계산
    while True:
        trial_a += 1
        mid = int((start_a + end_a) / 2)
        # 원하는 페이지에 도달하면 반복 종료
        if mid == find_a:
            break

        # 중간값이 찾으려는 값보다 크면 끝쪽을 절반으로 축소
        elif mid > find_a:
            end_a = mid

        # 중간값이 찾으려는 값보다 작으면 앞쪽을 절반으로 축소
        else:
            start_a = mid

    # b가 원하는 페이지를 찾는 데까지 시도한 횟수 계산
    while True:
        trial_b += 1
        mid = int((start_b + end_b) / 2)
        # 원하는 페이지에 도달하면 반복 종료
        if mid == find_b:
            break

        # 중간값이 찾으려는 값보다 크면 끝쪽을 절반으로 축소
        elif mid > find_b:
            end_b = mid

        # 중간값이 찾으려는 값보다 작으면 앞쪽을 절반으로 축소
        else:
            start_b = mid

    # 값이 작은 쪽(탐색 시도를 적게 한 쪽)이 승리
    # 무승부는 0으로 표시
    if trial_a > trial_b:
        answer = 'B'
    elif trial_b > trial_a:
        answer = 'A'
    else:
        answer = 0

    print(f'#{tc} {answer}')