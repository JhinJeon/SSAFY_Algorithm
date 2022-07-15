T = int(input())
for t in range(T):
    n,m = map(int,input().split())
    nlist = []  #숫자열 1
    mlist = []  #숫자열 2
    ansum = []  #(숫자열1 * 숫자열2)의 경우의 수 저장
    nlist = list(map(int,input().split()))
    mlist = list(map(int,input().split()))
    if n < m:   #nlist보다 mlist가 더 긴 경우
        for k in range(m-n+1):
            answer = []
            for i in range(len(nlist)):
                answer.append(nlist[i]*mlist[i+k])  #i를 고정하여 인덱스에 따라 나란히 곱하도록 작성
            ansum.append(sum(answer))
    elif n > m: #nlist가 mlist보다 긴 경우
        for k in range(n-m+1):
            answer = []
            for i in range(len(mlist)):
                answer.append(nlist[i+k]*mlist[i])
            ansum.append(sum(answer))
    else:   #nlist와 mlist의 길이가 동일한 경우
        answer = []
        for i in range(nlist):
            answer.append(nlist[i]*mlist[i])
        ansum.append(sum(answer))
    print('#'+str(t+1)+' '+str(max(ansum))) #ansum에 저장된 경우의 수 중 최댓값 출력