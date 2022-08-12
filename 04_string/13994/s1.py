# 새로운 버스 노선
# 오답

import sys

sys.stdin = open('sample_in.txt')

t = int(input())

for t in range(1, t + 1):
    stops = list()
    n = int(input())
    end_lim = 0
    for i in range(n):
        bustype, start, end = map(int,input().split())
        if end > end_lim:
            end_lim = end
        if bustype == 1:
            stops.append(list(range(start,end+1)))
        elif bustype == 2:
            temp_2 = list()
            if start % 2 == 1:
                for k in range(start,end + 1):
                    if k % 2 == 1:
                        temp_2.append(k)
            else:
                for k in range(start,end + 1):
                    if k % 2 == 0:
                        temp_2.append(k)
            stops.append(temp_2)
        else:
            temp_3 = list()
            if start % 2 == 0:
                for k in range(start, end+1):
                    if k % 4 == 0:
                        temp_3.append(k)
            else:
                for k in range(start,end + 1):
                    if k % 3 == 0 and k % 10 != 0:
                        temp_3.append(k)
            stops.append(temp_3)

    answer = 0
    for i in range(end_lim):
        common = 0
        for stop in stops:
            if i in stop:
                common += 1
        if common > answer:
            answer = common
            common = 0
        else:
            common = 0

    if answer == 1:
        answer = 0

    print(f'#{t} {answer}')


