# 암호코드 스캔
import sys
sys.stdin = open('sample_input.txt')

# 암호 코드 딕셔너리
# 암호코드 구성 이진수는 0 - 1 - 0 - 1 순으로 나옴
pw_code = {
    '[3, 2, 1, 1]': '0',
    '[2, 2, 2, 1]': '1',
    '[2, 1, 2, 2]': '2',
    '[1, 4, 1, 1]': '3',
    '[1, 1, 3, 2]': '4',
    '[1, 2, 3, 1]': '5',
    '[1, 1, 1, 4]': '6',
    '[1, 3, 1, 2]': '7',
    '[1, 2, 1, 3]': '8',
    '[3, 1, 1, 2]': '9',
}

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    array = [input() for _ in range(n)]
    solved = False  # 암호 해독 여부 구분용
    pw_valid = ""  # 암호 유효성 검사용 변수
    pw_value = 0  # 암호값 저장용 변수

    for arr in array:
        pw_size = len(arr)
        fit = (pw_size // 56) + 1  # 암호 배열 길이 배율 조정계수
        idx = -1  # 탐색 인덱스 번호
        encoded_code = ""       # 16진수 -> 이진수로 변환한 코드

        # 배열 내에서 암호 배열 길이만큼 범위 탐색
        while idx > -pw_size + 7 * fit:
            part = arr[idx - 7 * fit: idx]  # 탐색 구역
            sync_idx = 0  # code_sync의 인덱스를 가리키는 번호

            if part[-1] == '0':
                idx -= 1
            else:
                # 탐색 범위의 16진수 코드를 이진수로 변환
                for p in part:
                    p = bin(int(p, 16))[2:]
                    while len(p) < 4:
                        p = '0' + p
                    encoded_code += p
                # 순서를 정방향으로 전환
                encoded_code = encoded_code[::-1]

                # 이진수 코드를 7 * fit개씩 탐색
                for i in range(0, len(encoded_code), 7 * fit):
                    code_sync = [0, 0, 0, 0]  # 0 - 1 - 0 - 1이 각 몇 개씩 나오는지 기록하는 용도
                    sync_idx = 0
                    # 코드에서 길이가 7 * fit인 부분의 코드 구성 계산
                    for j in range(i,i+7*fit):
                        if encoded_code[j] != sync_idx % 2:
                            sync_idx += 1
                        if sync_idx > 3:  # 인덱스 범위 초과 시 반복문 즉시 종료
                            break
                        code_sync[sync_idx] += 1

                    # 배열 가로 길이에 비례해서 이진수 등장 횟수 보정
                    for a in range(4):
                        code_sync[a] = code_sync[a] // fit

                    # pw_code에서 해당하는 코드 가져오기
                    pw_decode = pw_code.get(code_sync)

                    # 유효한 코드인 경우
                    if pw_decode:
                        pw_valid += pw_decode
                        pw_value += int(pw_decode)
                        solved = True

        # 완성된 암호의 유효성 검사
        if solved:
            valid_check = 0
            for p in range(fit * 7):
                # 홀수 번째 자릿수는 3배한 값을 더하기
                if p % 2 == 0:
                    valid_check += int(pw_valid[p]) * 3
                else:
                    valid_check += int(pw_valid[p])

            if valid_check % 10 != 0:
                answer = 0
            else:
                answer = pw_value
            print(f'#{tc}', answer)
            break
