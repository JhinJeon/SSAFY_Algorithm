# 특별한 정렬
import sys
sys.stdin = open('sample_input.txt')


t = int(input())

for tc in range(1,t+1):
    # n = 숫자열의 길이
    # numbers = 공백 단위로 구분된 숫자들
    # answer = 새로 정렬된 리스트를 저장하기 위한 변수
    n = int(input())
    numbers = list(map(int,input().split()))
    answer = []

    # 인덱스 번호가 홀수면 오름차순(작은 수), 짝수면 내림차순(큰 수) 정렬
    for i in range(10):
        # 짝수인 경우 가장 큰 수를 리스트 맨 앞으로 뺀 후 pop
        # pop으로 반환한 값은 answer 리스트에 추가
        if i % 2 == 0:
            max_value = numbers[0]
            max_idx = 0
            for idx, val in enumerate(numbers):
                if val > max_value:
                    max_value = val
                    max_idx = idx
            numbers[0], numbers[max_idx] = numbers[max_idx], numbers[0]
            answer.append(numbers.pop(0))
        # 홀수인 경우 가장 작은 수를 리스트 맨 앞으로 뺀 후 pop
        # pop으로 반환한 값은 answer 리스트에 추가
        else:
            min_value = numbers[0]
            min_idx = 0
            for idx, val in enumerate(numbers):
                if val < min_value:
                    min_value = val
                    min_idx = idx
            numbers[0],numbers[min_idx] = numbers[min_idx], numbers[0]
            answer.append(numbers.pop(0))

    print(f'#{tc}', end=' ')
    print(*answer)