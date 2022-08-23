# 계산기 2
# import sys
# sys.stdin = open('input.txt')



for tc in range(1,11):
    n = int(input())
    calculation = input()
    cal_stack = []
    result = '' # 후위 표기법으로 변환한 식을 저장할 변수
    
    # 1. 중위 표기법으로 표현된 식을 후위 표기법으로 전환
    # call_stack을 연산자를 저장하는 스택으로 사용
    for c in calculation:
        if c not in '+-*-': # 연산 부호가 아닌 경우
            result += c
        else:   # 사칙연산 부호인 경우
            if c in '*/':
                # 곱셈/나눗셈인 경우 덧셈/뺄셈이 등장하기 전까지 스택에 저장된 부호 추가
                # 덧셈, 뺄셈을 나중 순위로 몰아주기 위함
                while cal_stack and cal_stack[-1] not in '+-':
                    result += cal_stack.pop()
                cal_stack.append(c)
            elif c in '+-': # 덧셈, 뺄셈인 경우
                while cal_stack:
                    result += cal_stack.pop()
                cal_stack.append(c)
                
    # 마지막 부분에 입력한 연산자 추가
    while cal_stack:
        result += cal_stack.pop()


    # 2. 후위 표기법으로 표시한 식 계산
    # call_stack을 숫자들을 저장하는 스택으로 사용
    for r in result:
        if r not in '+-*/': # 사칙연산이 아닌 경우 스택에 추가
            cal_stack.append(r)
        else:   # 사칙연산인 경우 스택에 저장된 수 두 개를 빼서 연산 후 추가
            if r == '*':
                b = int(cal_stack.pop())
                a = int(cal_stack.pop())
                cal_stack.append(a * b)
            elif r == '/':
                b = int(cal_stack.pop())
                a = int(cal_stack.pop())
                cal_stack.append(a / b)
            elif r == '+':
                b = int(cal_stack.pop())
                a = int(cal_stack.pop())
                cal_stack.append(a + b)
            elif r == '-':
                b = int(cal_stack.pop())
                a = int(cal_stack.pop())
                cal_stack.append(a + b)


    print(f'#{tc}', cal_stack[0])