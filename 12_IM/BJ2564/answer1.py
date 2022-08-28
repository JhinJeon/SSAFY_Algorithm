import sys
read = sys.stdin.readline

# 입력
w, h = map(int, read().split())
n = int(read())
store_loc = [list(map(int, read().split())) for _ in range(n)]
my_loc = list(map(int, read().split()))

# 풀이
answer = 0

if my_loc[0] == 1:  # 북
    for d, l in store_loc:
        if d == 1:
            answer += abs(my_loc[1] - l)
        elif d == 2:
            left_way = my_loc[1] + h + l
            right_way = (w - my_loc[1]) + h + (w - l)
            answer += min(left_way, right_way)
        elif d == 3:
            answer += my_loc[1] + l
        elif d == 4:
            answer += (w - my_loc[1]) + l
elif my_loc[0] == 2:  # 남
    for d, l in store_loc:
        if d == 1:
            left_way = my_loc[1] + h + l
            right_way = (w - my_loc[1]) + h + (w - l)
            answer += min(left_way, right_way)
        elif d == 2:
            answer += abs(my_loc[1] - l)
        elif d == 3:
            answer += my_loc[1] + (h - l)
        elif d == 4:
            answer += (w - my_loc[1]) + (h - l)
elif my_loc[0] == 3:  # 서
    for d, l in store_loc:
        if d == 1:
            answer += my_loc[1] + l
        elif d == 2:
            answer += (h - my_loc[1]) + l
        elif d == 3:
            answer += abs(my_loc[1] - l)
        elif d == 4:
            left_way = my_loc[1] + w + l
            right_way = (h - my_loc[1]) + w + (h - l)
            answer += min(left_way, right_way)
elif my_loc[0] == 4:  # 동
    for d, l in store_loc:
        if d == 1:
            answer += my_loc[1] + (w - l)
        elif d == 2:
            answer += (h - my_loc[1]) + (w - l)
        elif d == 3:
            left_way = (h - my_loc[1]) + w + (h - l)
            right_way = my_loc[1] + w + l
            answer += min(left_way, right_way)
        elif d == 4:
            answer += abs(my_loc[1] - l)

# 출력
print(answer)