# 경비원
# (0,0)으로부터 절대 거리 측정
import sys
sys.stdin = open('test_input.txt')

len_x, len_y = map(int,input().split())
store_count = int(input())

# 상점 방향, 상점 좌표(왼쪽/위에서 몇 번째인지) 입력받기
# 방향은 1 = 북, 2 = 남, 3 = 서, 4 = 동
distances = []
around = 2 * (len_x + len_y)

for _ in range(store_count+1):    # 값은 (y, x) 순서
    store_dir, store_idx = map(int,input().split())
    if store_dir == 1:  # 북쪽
        distances.append(store_idx)
    elif store_dir == 4:    # 동쪽
        distances.append(store_idx + len_x)
    elif store_dir == 2:    # 남쪽
        distances.append(2 * len_x + len_y - store_idx)
    else:
        distances.append(around - store_idx)

dongun = distances.pop()

answer = 0
for store in distances:
    c1 = dongun - store if dongun > store else store - dongun
    c2 = around - c1
    if c1 > c2:
        answer += c2
    else:
        answer += c1

print(answer)
