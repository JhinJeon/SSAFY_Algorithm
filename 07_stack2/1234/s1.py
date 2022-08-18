# 비밀번호
import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    # n = 문자열 길이, numbers = 숫자열(문자열 타입으로 입력받음)
    n, numbers = input().split()
    n = int(n)
    # password = 연속되는 문자를 제외한 문자열 결과
    password = [numbers[0]]
    
    for n in range(1,n):
        # 문자열이 연속되지 않는 경우이거나 모든 문자열을 소거한 경우 새 문자 추가
        if not password or password[-1] != numbers[n]:
            password.append(numbers[n])
        # 문자열이 연속되는 경우 기존의 문자 pop
        else:
            password.pop()


    print(f'#{tc}', ''.join(password))