# 16진수 딕셔너리
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

# 암호비트 딕셔너리
pw_pattern = {
    '001101': 0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001011': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9
}


t = int(input())

for tc in range(1, t+1):
    arr = input()
    arr = arr.lower()
    bit_two = ''

    # 16진수 -> 4자리 2진수로 변환해서 추가
    for a in arr:
        bit_two += digits.get(a)

    len_two = len(bit_two)  # 인덱스 표시용
    i = 0   # 탐색 범위

    while i < len_two:
        part = bit_two[i:i+6]   # 6비트 단위로 탐색
        answer = pw_pattern.get(part)   # pw_pattern 딕셔너리에서 값 찾기

        # pw_pattern이 발견되는 경우 출력 후 인덱스 건너뛰기
        if answer is not None:
            print(answer, end=' ')
            i += 6
        else:
            i += 1
