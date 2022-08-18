# 특별한 정렬
import sys
sys.stdin = open('sample_input.txt')


t = int(input())

for tc in range(1,t+1):
    # n = 숫자열의 길이
    # numbers = 공백 단위로 구분된 숫자들

    n: int = int(input())
    numbers = list(map(int, input().split()))

    # 인덱스 번호가 홀수면 오름차순(작은 수), 짝수면 내림차순(큰 수) 정렬
    for i in range(n):
        # 짝수인 경우 가장 큰 수를 리스트 맨 앞으로 뺀 후 pop
        # pop으로 반환한 값은 answer 리스트에 추가
        if i % 2 == 0:
            max_val = numbers[i]
            max_idx = i
            for idx, val in enumerate(numbers[i:]):
                if val > max_val:
                    max_val = val
                    max_idx = idx + i
            numbers[i], numbers[max_idx] = numbers[max_idx], numbers[i]

        # 홀수인 경우 가장 작은 수를 리스트 맨 앞으로 뺀 후 pop
        # pop으로 반환한 값은 answer 리스트에 추가
        else:
            min_val = numbers[i]
            min_idx = i
            for idx, val in enumerate(numbers[i:]):
                # val <= min_val을 해야 마지막 인덱스에서 min_idx가 갱신되어 인덱스 에러가 발생하지 않음
                if val <= min_val:
                    min_val = val
                    min_idx = idx
            numbers[i], numbers[min_idx + i] = numbers[min_idx + i], numbers[i]

    print(f'#{tc}', end=' ')
    print(*numbers[:10])