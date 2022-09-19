
# 0~f에 대응하는 이진수 딕셔너리 digits
digits = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'a': '1010',
    'b': '1011',
    'c': '1100',
    'd': '1101',
    'e': '1110',
    'f': '1111',
}

t = int(input())

for tc in range(1, t+1):
    # 1. 16진수 -> 2진수
    arr = input()
    arr = arr.lower()
    digit_two = ''      # 이진수로 변환한 값 저장용

    for a in arr:
        digit_two += digits.get(a)

    # 2. 2진수 -> 10진수
    len_two = len(digit_two)    # 이진수의 자릿수 표시용
    for i in range(0, len_two, 7):    # 7비트씩 분리
        part = digit_two[i:i+7]
        total = 0                   # 십진수로 변환한 값 저장용
        k = len(part)               # k = part의 자릿수
        for p in range(len(part)):
            if part[p] == '1':      # 1이 발견된 경우 십진수로 전환
                total += 1 << (k-p-1)
        print(total, end=' ')
