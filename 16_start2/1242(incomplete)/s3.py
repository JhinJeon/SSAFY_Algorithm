# 암호코드 스캔
import sys
sys.stdin = open('debug_input.txt')

# 암호 코드 딕셔너리(역방향)
# 암호코드 구성 이진수는 0 - 1 - 0 - 1 순으로 나옴

# 역방향 딕셔너리
pw_code = {
    (1, 1, 2): 0,
    (1, 2, 2): 1,
    (2, 2, 1): 2,
    (1, 1, 4): 3,
    (2, 3, 1): 4,
    (1, 3, 2): 5,
    (4, 1, 1): 6,
    (2, 1, 3): 7,
    (3, 1, 2): 8,
    (2, 1, 1): 9,
}

# 정방향 딕셔너리
# pw_code = {
#     (2, 1, 1): '0',
#     (2, 2, 1): '1',
#     (1, 2, 2): '2',
#     (4, 1, 1): '3',
#     (1, 3, 2): '4',
#     (2, 3, 1): '5',
#     (1, 1, 4): '6',
#     (3, 1, 2): '7',
#     (2, 1, 3): '8',
#     (1, 1, 2): '9',
# }

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())    # n = 세로, m = 가로
    solved = False      # 해결 여부 체크용
    answer = []         # 암호 값 기록용

    # 배열 입력받기(이진수 변환 과정 포함)
    for _ in range(n):
        arr = input()[:m]       # [:m]은 런타임 에러 방지용
        arr = arr.strip('0')
        replace_to_2bit = ""            # 이진수로 대체할 문자열

        # 16진수를 2진수로 변환
        while idx > -len(arr) - 1:
            # 16진수 수를 4자리 이진수로 전환
            p = bin(int(arr[idx], 16))[2:]
            while len(p) < 4:
                p = '0' + p
            replace_to_2bit = p + replace_to_2bit       # 정방향으로 더하기

        replace_to_2bit = replace_to_2bit.rstrip('0')

        # 뒤쪽부터 탐색
        idx = -1
        sync_idx = 1  # code_sync의 인덱스를 가리키는 번호
        array_found = list()    # 한 줄 내에서 찾은 암호 패턴 저장용

        while idx > -len(replace_to_2bit)-1:
            code_sync = [0, 0, 0]  # 1 - 0 - 1이 각 몇 개씩 나오는지 기록하는 용도

            # 1. code_sync에 패턴을 기록하는 과정
            while idx > -len(replace_to_2bit)-1:
                if sync_idx == 4:
                    if replace_to_2bit[idx] == '1':
                        sync_idx = 0
                    else:
                        idx -= 1
                        continue
                # 1 - 0 - 1 순으로 바꾸면서 더하기
                if int(replace_to_2bit[idx]) != sync_idx % 2:
                    sync_idx += 1

                # 인덱스 범위를 이탈하는 경우 다음 1을 만날 때까지 반복문 종료
                if sync_idx == 4:
                    break
                code_sync[sync_idx-1] += 1
                idx -= 1

            # 2. 찾은 패턴을 십진수 값으로 해독
            # 딕셔너리에서 해시할 수 있도록 리스트의 최소값으로 나누고 튜플 형태로 전환
            divider = min(code_sync)
            for i in range(3):
                code_sync[i] = code_sync[i] // divider
            tuple_code = tuple(code_sync)

            # pw_code 딕셔너리에서 해당하는 십진수 가져오기
            pw_decode = pw_code.get(tuple_code)

            # 십진수 값을 array_found에 추가
            array_found.append(pw_decode)

        # 한 줄 내에서 모든 암호 패턴들을 찾은 후
        for i in range(0, len(array_found), 8):
            check_array = array_found[i:i+8]
            valid_check = 0
            pw_value = 0
            for k in range(8):
                check_num = check_array[k]
                if k % 2 == 0:
                    valid_check += check_num * 3
                else:
                    valid_check += check_num
                pw_value += check_num

        # 유효한 암호 코드인 경우 값 합산
        if valid_check % 10 == 0:
            answer.append(pw_value)

    # 모든 줄을 탐색한 후 중복값 제거 및 출력
    answer = sum(list(set(answer)))
    print(f'#{tc}', answer)
