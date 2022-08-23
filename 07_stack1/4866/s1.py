# 괄호 검사
import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1, t + 1):
    # answer : 괄호 쌍이 맞으면 1, 맞지 않으면 0
    # bracket = 괄호 쌍이 맞는지 검증하기 위한 스택
    answer = 0
    string = input()
    bracket = []

    for s in string:
        # 여는 괄호가 탐색되는 경우
        if s == '[' or s == '{' or s == '(':
            bracket.append(s)
        # 닫는 대괄호가 탐색되는 경우
        elif s == ']':
            # 여는 괄호가 없었으면 반복 중단
            if not bracket:
                break
            # 여는 괄호와 짝이 맞지 않으면 반복 중단
            bracket_check = bracket.pop()
            if bracket_check != '[':
                break
        # 닫는 중괄호가 탐색되는 경우
        elif s == '}':
            # 여는 괄호가 없었으면 반복 중단
            if not bracket:
                break
            # 여는 괄호와 짝이 맞지 않으면 반복 중단
            bracket_check = bracket.pop()
            if bracket_check != '{':
                break
        # 닫는 소괄호가 탐색되는 경우
        elif s == ')':
            # 여는 괄호가 없었으면 반복 중단
            if not bracket:
                break
            # 여는 괄호와 짝이 맞지 않으면 반복 중단
            bracket_check = bracket.pop()
            if bracket_check != '(':
                break
    # 남는 여는 괄호가 없는 경우 괄호 짝이 맞는 것으로 판단
    else:
        if not bracket:
            answer = 1

    print(f'#{tc} {answer}')
