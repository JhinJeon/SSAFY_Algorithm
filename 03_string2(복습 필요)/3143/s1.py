# 가장 빠른 문자열 타이핑

t = int(input())


for tc in range(1, t + 1):
    a, b = input().split()

    # 문자열 a에서 b가 발견되는 경우 0으로 치환
    a = a.replace(b, '0')

    # 치환된 문자열 a의 길이를 정답으로 반환
    answer = len(a)
    print(f'#{tc} {answer}')
