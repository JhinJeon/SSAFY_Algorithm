# 새로운 버스 노선
# 오답

import sys

sys.stdin = open('sample_in.txt')

for t in range(1, int(input()) + 1):
    n = int(input())
    stops_2 = []
    stops_3 = []
    for i in range(n):
        bustype, start, end = map(int,input().split())
        if bustype == 1:
            stops_1 = list(range(start,end+1))
        elif bustype == 2:
            stops_2.append(start)
            stops_2.append(end)
            if start % 2 == 1:
                for k in range(start+1,end):
                    if k % 2 == 1:
                        stops_2.append(k)
            else:
                for k in range(start+1,end):
                    if k % 2 == 0:
                        stops_2.append(k)
        else:
            stops_3.append(start)
            stops_3.append(end)
            if start % 2 == 0:
                for k in range(start+1,k):
                    if k % 4 == 0:
                        stops_3.append(k)
            else:
                for k in range(start+1,k):
                    if k % 3 == 0 and k % 10 != 0:
                        stops_3.append(k)

    if set(stops_1) & set(stops_2) & set(stops_3):
        answer = 3
    elif set(stops_1) & set(stops_2) or set(stops_2) & set(stops_3) or set(stops_1) & set(stops_3):
        answer = 2
    else:
        answer = 1
    print(f'#{t} {answer}')


