# 암호코드 스캔
# 11번부터 답이 틀리는 문제

import sys
sys.stdin = open('sample_input.txt')

# 암호 코드 딕셔너리
# 암호코드 구성 이진수는 0 - 1 - 0 - 1 순으로 나옴
pw_code = {
    (3, 2, 1, 1): '0',
    (2, 2, 2, 1): '1',
    (2, 1, 2, 2): '2',
    (1, 4, 1, 1): '3',
    (1, 1, 3, 2): '4',
    (1, 2, 3, 1): '5',
    (1, 1, 1, 4): '6',
    (1, 3, 1, 2): '7',
    (1, 2, 1, 3): '8',
    (3, 1, 1, 2): '9',
}

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())    # n = 세로, m = 가로
    array = list()
    solved = False      # 해결 여부 체크용
    answer = 0          # 암호 값 기록용
    overlap_value = -1  # 중복값 검사용

    # 배열 입력받기(이진수 변환 과정 포함)
    for _ in range(n):
        arr = input()[:m]       # [:m]은 런타임 에러 방지용
        arr = arr.strip('0')
        idx = -1                # 인덱스 번호
        replace_to_2bit = ""            # 이진수로 대체할 문자열
        pw_valid = ""  # 암호 유효성 검사용
        pw_value = 0  # 암호 값 계산용(십진수)

        # 뒤쪽부터 탐색
        while idx > -len(arr)-1:
            # 16진수 수를 이진수로 전환
            p = bin(int(arr[idx], 16))[2:]
            while len(p) < 4:
                p = '0' + p
            replace_to_2bit = p + replace_to_2bit
            idx -= 1

        # replace_to_2bit에 저장된 문자열이 있는 경우(0만 있는 줄이 아닌 경우)
        if replace_to_2bit:
            replace_to_2bit = replace_to_2bit.rstrip('0')   # 0으로 끝나는 뒷 부분 자르기
            rept = len(replace_to_2bit) % 56                # 앞쪽에 0을 이어붙이는 횟수 또는 슬라이싱 할 위치
            if rept >= 28:
                while rept < 56:            # 암호 길이가 56의 배수가 아닌 경우 앞 부분 이어 붙이기
                    replace_to_2bit = '0' + replace_to_2bit
                    rept += 1
                replace_to_2bit = replace_to_2bit[-56 * (len(replace_to_2bit) // 56):]
            else:
                replace_to_2bit = replace_to_2bit[rept:]

            pw_size = len(replace_to_2bit)  # 배열 길이 정보 갱신
            fit = pw_size // 56  # 배열 길이(암호 8자)

            # 암호 배열에서 7 * fit만큼의 범위 탐색
            for i in range(0, pw_size, 7 * fit):
                part = replace_to_2bit[i:i + 7 * fit]  # 탐색 구역
                code_sync = [0, 0, 0, 0]  # 0 - 1 - 0 - 1이 각 몇 개씩 나오는지 기록하는 용도
                sync_idx = 0  # code_sync의 인덱스를 가리키는 번호

                # 탐색 범위의 이진수를 code_sync에서 집계
                for p in part:
                    # 코드에서 길이가 7 * fit인 부분의 코드 구성 계산
                    if int(p) != sync_idx % 2:
                        sync_idx += 1
                    if sync_idx > 3:  # 인덱스 범위 초과 시 반복문 즉시 종료
                        break
                    code_sync[sync_idx] += 1

                # 배열 가로 길이에 비례해서 이진수 등장 횟수 보정
                for a in range(4):
                    code_sync[a] = code_sync[a] // fit

                # 딕셔너리에서 해시할 수 있도록 튜플 형태로 전환
                code_sync = tuple(code_sync)

                # pw_code에서 해당하는 코드 가져오기
                pw_decode = pw_code.get(code_sync)

                # 십진수에 대응 가능한 코드인 경우
                if pw_decode:
                    pw_valid += pw_decode
                    pw_value += int(pw_decode)

            # 완성된 암호의 유효성 검사
            if len(pw_valid) != 8:  # 불완전한 암호 해독 결과인 경우
                continue
            valid_check = 0
            for p in range(8):
                # 홀수 번째 자릿수는 3배한 값을 더하기
                if p % 2 == 0:
                    valid_check += int(pw_valid[p]) * 3
                else:
                    valid_check += int(pw_valid[p])

            # 유효성 체크용 값이 10의 배수이면서 직전 줄에 등장하지 않은 경우
            if valid_check % 10 == 0 and overlap_value != pw_value:
                overlap_value = pw_value
                answer += pw_value

    if not answer:
        answer = 0
    print(f'#{tc}', answer)
