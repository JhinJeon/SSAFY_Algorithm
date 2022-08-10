import sys
sys.stdin = open('input.txt')

# 일단 테스트 케이스는 통과함
t = int(input())

for tc in range(1, t+1):
    numbers = list(map(int, input().split()))
    # 부분집합 경우의 수 탐색
    # idx = 부분집합 카운트 시작 인덱스 번호
    # element = 부분집합에 추가할 원소 인덱스 범위
    # sum_temp = 부분집합의 합계를 저장하는 임시 변수
    answer = 0
    for idx in range(10):
        if numbers[idx] == 0:
            answer = 1
            break
        for element in range(idx, 10):
            sum_temp = numbers[idx] + numbers[element]
            if sum_temp == 0:
                answer = 1
                break
        if answer == 1:
            break

    print(f'#{tc} {answer}')
