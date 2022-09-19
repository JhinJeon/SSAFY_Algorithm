# 단순 2진 암호코드
import sys
sys.stdin = open('input.txt')

# 암호 패턴에 대응하는 숫자 딕셔너리
pw_pattern = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}


t = int(input())

for tc in range(1, t+1):
    col, row = map(int, input().split())
    array = [list(input().split()) for _ in range(col)]     # 배열 구성하는 값은 문자열(str) 타입
    pw_code = 0                                     # 암호 코드값
    pw_valid = ''                                   # 암호 코드 유효성 검증용
    solved = False                                  # 암호 확인 여부 체크용(불필요한 계산 방지)

    for arr in array:
        len_arr = len(arr[0])
        i = -1

        while i > -len_arr - 1:              # 뒤쪽부터 탐색, 7개씩 끊어서 암호 딕셔너리와 대조
            part = arr[0][i-7:i]
            decoded_code = pw_pattern.get(part)

            # 암호 패턴이 발견된 경우
            if decoded_code is not None:
                # 암호 코드값 합산
                pw_code += decoded_code
                # 자릿수를 기억하기 위해 문자열 형태로 합산
                pw_valid += str(decoded_code)
                i -= 7
                solved = True
            else:
                i -= 1

                
        # 암호 코드가 완성된 경우
        if solved:
            pw_valid = pw_valid[::-1]       # 뒤쪽부터 추가했으므로 순서 뒤집기
            validation_check = 0            # 검증용 값(10의 배수인 경우 유효한 암호로 판단)
            for v in range(len(pw_valid)):  # 홀수 번째면 3배 곱한 값을 합산
                if v % 2 == 0:
                    validation_check += 3 * int(pw_valid[v])
                else:
                    validation_check += int(pw_valid[v])
                    
            # 암호가 무효인 경우(검증용 값이 10의 배수가 아닌 경우) 암호값을 0으로 처리
            if validation_check % 10 != 0:
                answer = 0
            else:
                answer = pw_code
            print(f'#{tc}', answer)
            break

