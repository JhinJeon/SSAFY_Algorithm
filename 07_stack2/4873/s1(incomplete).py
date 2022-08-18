# 반복문자 지우기
import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1,t+1):
    strings = input()
    str_stack = [strings[0]]
    dup_check = []
    # 반복되는 문자열을 발견한 경우 : 일단 새 문자열에서는 제거하지 않고 dup_check에 추가
    for s in range(1,len(strings)):
        if strings[s] == str_stack[-1]:
            dup_check.append(strings[s])
        else:
            # 기존까지 반복되던 문자열이 있는 경우
            if dup_check:
                str_stack.pop()
                dup_check.pop()
            # 전혀 새로운 문자열이 추가된 경우
            else:
                str_stack.append(strings[s])
            dup_check = []

    print(f'#{tc} {len(str_stack)}')