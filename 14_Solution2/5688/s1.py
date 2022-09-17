# 세제곱근을 찾아라
# 런타임 에러 발생

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    components = [0] * n  # 소인수(인덱스 번호)가 몇 개인지(값) 기록하는 용도
    answer = 1
    if n == 1:
        print(f'#{tc}', 1)
        continue

    for divider in range(2, n):
        while n % divider == 0:
            components[divider] += 1
            n /= divider

    for c in range(2, len(components)):
        if int(components[c]) % 3 != 0:
            answer = -1
            break
        elif components[c] == 0:
            continue
        else:
            answer = answer * c * components[c] / 3

    if answer == 1:
        answer = -1
    print(f'#{tc}', int(answer))
