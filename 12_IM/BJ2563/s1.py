# 색종이

n = int(input())
paste_info = []
bg_paper = []

for _ in range(n):
    paste_info.append(tuple(map(int,input().split())))

for paste in paste_info:
    for col in range(10):
        for row in range(10):
            bg_paper.append(tuple([paste[0] + row, paste[1] + col]))

answer = set(bg_paper)
print(len(answer))