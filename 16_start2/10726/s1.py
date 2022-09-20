# 이진수 표현

t = int(input())

for tc in range(1,t+1):
    n, m = map(int,input().split())
    m = bin(m)[2:]  # m은 이진수로 전환
    answer = 'ON'   # 비트 기본값은 켜짐(ON)
    while len(m) < n:   # 자릿수 보정
        m = '0' + m

    # 뒤쪽부터 n개 비트 확인
    for i in range(-1, -n-1, -1):
        # 하나라도 꺼져 있으면 OFF
        if m[i] == '0':
            answer = 'OFF'
            break

    print(f'#{tc} {answer}')