# 세제곱근을 찾아라

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    answer = -1
    num_min, num_max = 1, n  # 숫자의 범위

    while num_min <= num_max:
        # median = 세제곱근, result = median이 n의 세제곱근인지 확인하는 용도
        median = (num_min + num_max) // 2
        result = median**3

        if result == n:  # 값을 찾은 경우 반복문 종료
            answer = median
            break

        elif result > n:  # 찾으려는 값보다 큰 경우 최댓값 범위 축소
            num_max = median - 1

        else:  # 찾으려는 값보다 작은 경우 최솟값 범위보다 축소
            num_min = median + 1

    print(f'#{tc}', answer)
