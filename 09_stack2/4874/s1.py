# Forth

t = int(input())

for tc in range(1,t+1):
    cal_code = list(input().split())    # 입력받는 수식(공백 기준 분리)
    cal_stack = []  # 수식 계산용 스택
    for cc in cal_code:
        if cc == '.':   # .를 입력받는 경우(수식 맨 마지막)
            if len(cal_stack) > 1:  # 스택에 값이 2개 이상 있는 경우(연산자 개수가 부족한 경우)
                answer = 'error'
                break
            # 스택에 값이 1개 있는 경우(정상)
            answer = cal_stack[-1]

        elif cc in '+-*/':  # 사칙 연산 기호를 입력받은 경우 스택에서 숫자 2개를 pop한 후 계산
            if len(cal_stack) < 2:
                answer = 'error'
                break
            b = cal_stack.pop()
            a = cal_stack.pop()
            if cc == '*':
                cal_stack.append(a * b)
            elif cc == '/':
                cal_stack.append(a // b)
            elif cc == '+':
                cal_stack.append(a + b)
            elif cc == '-':
                cal_stack.append(a - b)
        else:   # 숫자를 입력받은 경우 스택에 추가
            cal_stack.append(int(cc))

    print(f'#{tc}', answer)