# 정곤이의 단조 증가하는 수

def danzo_check(input_no):  # input_no는 문자열 타입으로 입력
    global danzo_max
    is_continue = False
    for x in range(len(input_no) - 1):
        if input_no[x] > input_no[x + 1]:
            is_continue = True
            break
    else:
        if dz > danzo_max and not is_continue:
            danzo_max = dz

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    danzo = list(map(int, input().split()))
    danzo_max = 0

    if len(danzo) == 1:
        danzo_check(str(danzo[0]))
    else:
        for i in range(n-1):
            dz = danzo[i] * danzo[i + 1]
            danzo_check(str(dz))

    print(f'#{tc}', danzo_max)