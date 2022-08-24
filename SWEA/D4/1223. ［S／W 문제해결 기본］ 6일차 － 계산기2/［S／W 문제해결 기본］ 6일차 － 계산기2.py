for tc in range(1,11):
    n = int(input())
    calculation = input()
    cal_stack = []
    result = ''

    for c in calculation:
        if c not in '+-*-':
            result += c
        else:
            if c in '*/':
                while cal_stack and cal_stack[-1] not in '+-':
                    result += cal_stack.pop()
                cal_stack.append(c)
            elif c in '+-':
                while cal_stack:
                    result += cal_stack.pop()
                cal_stack.append(c)
    while cal_stack:
        result += cal_stack.pop()

    while cal_stack:
        cal_stack.pop()

    for r in result:
        if r not in '+-*/':
            cal_stack.append(r)
        else:
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