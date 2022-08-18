# 반복문자 지우기
# 희제님 코드 참조
import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1,t+1):
    strings = input()
    str_stack = []
    for s in strings:
        # 새로운 문자열을 발견했거나, 스택이 빈 경우
        if not str_stack or str_stack[-1] != s:
            str_stack.append(s)
        # 반복되는 문자열을 발견한 경우
        else:
            str_stack.pop()
        

    print(f'#{tc} {len(str_stack)}')