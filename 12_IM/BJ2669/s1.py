# 직사각형 네개의 합집합의 면적 구하기

paste_info = []
board = set()
for _ in range(4):
    # lb_x, lb_y, rt_x, rt_y
    paste_info.append(list(map(int,input().split())))

for paste in paste_info:
    for x in range(paste[0], paste[2]):
        for y in range(paste[1], paste[3]):
            board.add((x,y))

print(len(board))