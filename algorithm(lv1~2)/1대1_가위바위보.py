#A가 이기는 시나리오와 B가 이기는 시나리오의 구분
a,b = input().split()
a = int(a)
b = int(b)
if a == (b % 3) + 1:
    print('A')
if b == (a % 3) + 1:
    print('B')