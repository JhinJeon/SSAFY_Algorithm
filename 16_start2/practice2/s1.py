# 이진수2

t = int(input())

for tc in range(1, t + 1):
    n = float(input())
    result = ''
    digits = -1

    # 12자리까지 탐색
    while digits > -13:
        value = 2**digits  # 이진수의 소수점은 2의 음수제곱
        if n > value:  # n 이 value보다 큰 경우 자리수 1 표시
            result += '1'
            n -= value
            digits -= 1
        elif n < value:  # n이 value보다 작은 경우 자리수 0으로 표시
            result += '0'
            digits -= 1
        else:  # n이 value와 동일한 경우 나머지 값을 1로 표시하고 반복문 종료
            result += '1'
            break
    if digits <= -13:  # 12자리를 초과하는 경우 overflow로 대체
        result = 'overflow'

    print(f'#{tc} {result}')
