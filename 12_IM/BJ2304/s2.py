# 창고 다각형
import sys
sys.stdin = open('sample2.txt')


column_count = int(input())
column_info = dict()
max_height = 0
col_end = 1
wide = 0

for _ in range(column_count):
    position, height = map(int,input().split())
    column_info[position] = height
    if height > max_height:
        max_height = height
    if position > col_end:
        col_end = position

# 딕셔너리를 키 값을 기준으로 정렬, 정렬 결과는 튜플을 담고 있는 리스트
column_info = sorted(column_info.items(),reverse=False)
heights = [0] * (col_end + 1)

for infos in column_info:
    heights[infos[0]] += infos[1]

remaining_max = heights.count(max_height)
max_passed = False
current_height = 0
for i in range(1, col_end+1):
    if max_passed:
        break
    elif heights[i] == max_height:
        current_height = max_height
        remaining_max -= 1
        if remaining_max == 0:
            max_passed = True
    else:
        if heights[i] > current_height:
            current_height = heights[i]
    wide += current_height


current_height = 0
for i in range(col_end, -1, -1):
    if heights[i] == max_height:
        break
    else:
        if heights[i] > current_height:
            current_height = heights[i]
    wide += current_height

print(wide)
