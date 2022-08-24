<<<<<<< HEAD
# 후위 표기법
=======
# 중위 표기법을 후위 표기법으로 전한

word = input()
result = ''
stack = []

for w in word:
    # 피연산자는 stack에 넣는다
    # 숫자는 result에 추가한다
    if w in '()+-*/':
        # 여는 괄호가 나오면 스택에 추가
        if w == '(' or not stack:
            stack.append(w)
        # 다른 연산자가 나오면 여는 괄호 직전까지 추가
        elif w in '*/':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(w)
        elif w in '+-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(w)
        # 닫는 괄호가 나오면 여는 괄호 직전까지 추가 + 여는 괄호 제거
        elif w == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

    else:
        result += w
>>>>>>> d493e1da6402dd003b83940966606a2ab1a82084
