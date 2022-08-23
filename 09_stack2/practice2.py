# 후위 표기법 계산

numbers = input()
stack = []

for n in numbers:
    # 피연산자를 만나면 top의 숫자 두개를 기준으로 연산한다
    # 숫자는 stack에 추가한다
    if n not in '()+-*/':
        stack.append(n)
    else:
        # a가 나중에 뺀 것(왼쪽)
        b = stack.pop()
        a = stack.pop()
        if n == '+':
            stack.append(a + b)
        elif n == '-':
            stack.append(a - b)
        elif n == '*':
            stack.append(a * b)
        elif n == '/':
            stack.append(a / b)

print(stack[-1])