# 계산기3
import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    n = int(input())
    cal_input = input()
    cal_sort = ''
    cal_stack = []

    # 1. 중위표기법으로 표시된 수식을 후위표기법으로 전환
    for c in cal_input:
        if c in '()+-*/':   # 괄호와 사칙연산 기호인 경우
            if c == '(' or not cal_stack:   # 여는 괄호이거나 스택이 비었을 경우 기호 입력
                cal_stack.append(c)
            elif c in '*/':
                while cal_stack and cal_stack[-1] in '*/':  # 곱셈/나눗셈인 경우 덧셈/뺄셈보다 먼저 계산(정렬)
                    cal_sort += cal_stack.pop()
                cal_stack.append(c)
            elif c in '+-':
                while cal_stack and cal_stack[-1] != '(':
                    cal_sort += cal_stack.pop()
                cal_stack.append(c)
            elif c == ')':  # 닫는 괄호인 경우 여는 괄호가 나올 때까지 스택 pop
                while cal_stack and cal_stack[-1] != '(':
                    cal_sort += cal_stack.pop()
                cal_stack.pop()
        else:
            cal_sort += c
    while cal_stack:
        cal_sort += cal_stack.pop()

    # 2. 후위표기법으로 표시된 수식 연산
    for cs in cal_sort:
        if cs in '+-*/':    # 사칙연산 기호인 경우 스택의 두 수를 pop한 후 연산
            b = int(cal_stack.pop())
            a = int(cal_stack.pop())
            if cs == '*':
                cal_stack.append(a * b)
            elif cs == '/':
                cal_stack.append(a / b)
            elif cs == '+':
                cal_stack.append(a + b)
            elif cs == '-':
                cal_stack.append(a - b)
        else:   # 숫자인 경우 스택에 추가
            cal_stack.append(cs)

    print(f'#{tc}', cal_stack[-1])