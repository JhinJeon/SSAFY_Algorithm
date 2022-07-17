t = int(input())
n,m = map(int,input().split())
for k in range(t):
    answer = 0
    area = []
    for i in range(n):
        area.append(list(map(int,input().split())))
    if m == n:	#파리채가 전 범위를 커버하는 경우
        for i in range(len(sum)):
            answer += sum(area[i])
    else:	#파리채로 잡는 부분 (미구현)
        catch = 0
        catchsum = []
        for dy in range(n-m):
            for dx in range(n-m):
                catch += area[dy][dx]
print("#"+str(t+1)+" "+str(answer))