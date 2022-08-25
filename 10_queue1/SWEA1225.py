# 암호생성기
import sys
sys.stdin = open('input.txt')

for _ in range(1, 11):
    tc = int(input())   # 테스트 번호
    password = list(map(int, input().split()))  # 비밀번호 리스트(큐)

    while 0 not in password:    # 비밀번호에서 0이 나오기 전까지 반복
        for i in range(1, 6):   # 뺄 수(피연산자)를 1부터 5까지 반복
            front_pop = password.pop(0)    # 맨 앞의 수를 반환(pop)
            front_pop -= i      # 반환한 수에 규칙에 따라 연산
            if front_pop <= 0:      # 연산 결과가 0보다 작거나 같은 경우
                password.append(0)  # 0을 큐에 입력한 후 반복 종료
                break
            else:   # 연산 결과가 0보다 큰 경우 결과값을 큐에 입력
                password.append(front_pop)

    print(f'#{tc}', *password)
