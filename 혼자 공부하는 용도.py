#방법 1(내가 작성한 코드) - 하나의 긴 리스트로 만들어서 풀기
'''
T = int(input())
for k in range(0,T):
    N = int(input())
    textlist = []
    numlen = []
    for i in range(N):
        a,b = input().split()
        b = int(b)
        numlen.append(b)
        for j in range(b):
            textlist.append(a)
    print('#'+str(k+1))
    for i in range(0,len(textlist)+1,10):
        print(''.join(textlist[i:i+10]))
'''

#방법 2(김도희님 코드) - 문자열의 인덱스와 값을 enumerate로 반환해서 풀기
t = int(input())
for i in range(1,t+1):
    print(f"#{i}")
    n = int(input())
    answer = ''
    for j in range(n):
        a, b = input().split()
        b = int(b)
        answer += a * b
    for i, char in enumerate(answer):
        if i > 0 and i % 10 == 0:
            print()
        print(char, end='')
    print()
    
    T = int(input())

for test_case in range(1, T + 1):
    print("#", test_case)
    t = int(input())
    a = ''

    for x in range(1, t + 1):
        lst = list(map(str, input().split()))
        eng = str(lst[0])
        num = int(lst[1])
        res = eng * num
        a += res
    for y in range(0, len(a)+1,10):
        print(a[0:10])
        a = a[10:]
        
#방법 3(조용현님 코드) : for 문을 돌리면서 리스트 값을 수정하며 출력
T = int(input())

for test_case in range(1, T + 1):
    print("#", test_case,end='')
    print()
    t = int(input())
    a = ''

    for x in range(1, t + 1):
        lst = list(map(str, input().split()))
        eng = str(lst[0])
        num = int(lst[1])
        res = eng * num
        a += res
    for y in range(0, len(a)+1,10):
        print(a[0:10])
        a = a[10:]