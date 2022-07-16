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

#방법 2(다른 교육생의 코드 참고) - 문자열의 인덱스와 값을 enumerate로 반환해서 풀기
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