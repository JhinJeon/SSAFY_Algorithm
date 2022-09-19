# 진수 표현
# 비트 연산자 사용

t = int(input())

for tc in range(1, t+1):
    array = input()
    for i in range(0, len(array), 7):
        arr = int(array[i:i+7])      # 7자 단위로 슬라이싱 후 정수화
        total = 0                    # 십진수로 변환한 값

        arr_str = str(arr)          # 문자열로 전환(자릿수 반환용)
        digits = len(arr_str)       # 자릿수 저장

        # 자릿수에서 숫자 1이 발견된 경우 2를 (자릿수-1)만큼 제곱한 값을 total에 합산
        for i in range(digits):
            if arr_str[i] == '1':
                k = digits - i - 1
                total += 1 << k
        print(total, end=' ')   # 결과 출력


# <<를 쓰면 제곱하는 효과, >>를 쓰면 자릿수를 거꾸로 탐색하는 효과
