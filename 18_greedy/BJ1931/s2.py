# 회의실 배정
# 람다 함수로 정렬

import sys
sys.stdin = open('testcase.txt')


n = int(input())
timeline = [list(map(int, input().split())) for _ in range(n)]
timeline.sort(key=lambda x:x[0])
timeline.sort(key=lambda x:x[1])
answer = 0
current_time = 0
for i in range(n):
    if timeline[i][0] >= current_time:
        current_time = timeline[i][1]
        answer += 1

print(answer)