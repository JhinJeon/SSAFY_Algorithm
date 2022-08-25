# 부분집합

powerset = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


def get_subset(n, k):   # n = 원소 번호(값), k = 집합 개수
    if n == k:
        return k


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
