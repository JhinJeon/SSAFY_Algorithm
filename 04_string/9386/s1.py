# 연속한 1의 개수

import sys
sys.stdin = open('input1.txt')

# 테스트 케이스 수를 for 반복문 선언할 때 받음
for t in range(1, int(input()) + 1):
    # n = 수열 길이
    # numbers = 수열
    n = int(input())
    numbers = input()
    
    # streak = 1이 연속된 횟수를 저장하는 임시 변수
    # answer = 1이 연속된 횟수의 최댓값을 저장하는 임시 변수
    streak = 0
    answer = 0
    
    # 수열의 앞쪽부터 반복문 실행
    for i in range(n):
        # 탐색한 값이 1이면 연속된 횟수 + 1
        if int(i) == 1:
            streak += 1
        # 탐색한 값이 0이면 연속 횟수 초기화
        # 만약 기존의 최댓값보다 크다면 최댓값 경신
        else:
            if answer < streak:
                answer = streak
            streak = 0
    # 수열의 마지막 부분에도 1이 나왔을 때
    if answer < streak:
        answer = streak

    print(f'#{t} {answer}')
