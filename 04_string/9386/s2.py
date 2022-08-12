# 연속한 1의 개수

import sys
sys.stdin = open('input1.txt')

# 테스트 케이스 수를 for 반복문 선언할 때 받음
for t in range(1, int(input()) + 1):
    # n = 수열 길이
    # numbers = 수열
    n = int(input())
    numbers = input()
    
    # streak_list = 연속된 횟수를 기록하는 리스트
    # streak = 1이 연속된 횟수를 저장하는 임시 변수
    streak_list = [0]
    streak = 0

    # 수열의 앞쪽부터 반복문 실행
    for i in range(n):
        # 탐색한 값이 1이면 연속된 횟수 + 1, 연속된 횟수 기록
        if int(numbers[i]) == 1:
            streak += 1
            streak_list.append(streak)
        # 탐색한 값이 0이면 연속 횟수 초기화
        else:
            streak = 0

    # answer = 1이 연속으로 등장한 기록 중 최댓값
    answer = max(streak_list)

    print(f'#{t} {answer}')
