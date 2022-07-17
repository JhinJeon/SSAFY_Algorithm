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