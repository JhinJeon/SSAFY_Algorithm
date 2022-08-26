# 창고 다각형
import sys
sys.stdin = open('sample2.txt')


column_count = int(input())
column_info = dict()
max_height = 0
col_start = 1000
col_end = 1
wide = 0

for _ in range(column_count):
    position, height = map(int,input().split())
    column_info[position] = height
    if height > max_height:
        max_height = height
    if position < col_start:
        col_start = position
    elif position > col_end:
        col_end = position

# 딕셔너리를 키 값을 기준으로 정렬, 정렬 결과는 튜플을 담고 있는 리스트
column_info = sorted(column_info.items(),reverse=False)

# 정렬 결과를 다시 딕셔너리로 전환
column_dict = dict()
for item in column_info:
    column_dict[item[0]] = item[1]

# 정렬한 임시 리스트에서 시작 높이 가져오기
current_height_left = column_info[0][1]
current_height_right = column_info[-1][1]


for position in range(col_start, col_end+1):
    column = column_dict.get(position)
    if column:
        if column == max_height:
            wide += max_height
            break
        else:
            if column > current_height_left:
                current_height_left = column
    wide += current_height_left


for position in range(col_end, col_start-1, -1):
    column = column_dict.get(position)
    if column:
        if column == max_height:
            break
        else:
            if column > current_height_right:
                current_height_right = column
    wide += current_height_right

print(wide)
