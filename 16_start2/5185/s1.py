# 이진수

t = int(input())

for tc in range(1, t + 1):
    n, n_num = input().split()
    n_num = n_num.lower()  # 16진수 수(문자열 자료형)로 변환

    result = ''
    for num in n_num:
        k = str(bin(int(num, 16))[2:])  # 16진수 값을 이진수로 전환
        while len(k) < 4:  # 자릿수가 부족한 경우 4자리가 될 때까지 0 채우기
            k = '0' + k
        result += k

    print(f'#{tc} {result}')
