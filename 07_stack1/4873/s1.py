# 반복문자 지우기
# 복습용 버전

import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1,t+1):
    strings = input()
    str_stack = []
    # 반복되는 문자열을 발견한 경우 : 일단 새 문자열에서는 제거하지 않고 dup_check에 추가
    for s in strings:
        if not str_stack or str_stack[-1] != s:
            str_stack.append(s)
        else:
            str_stack.pop()

    print(f'#{tc} {len(str_stack)}')