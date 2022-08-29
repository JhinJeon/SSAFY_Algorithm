
t = int(input())

for tc in range(1, t+1):
    n = int(input())
    danzo = list(map(int, input().split()))
    danzo_max = 0
    danzo_case = set()
    result = []

    for idx_1 in range(len(danzo)):
        for idx_2 in range(idx_1, len(danzo)):
            if idx_1 != idx_2:
                danzo_case.add((danzo[idx_1], danzo[idx_2]))

    for dc in danzo_case:
        n1, n2 = dc[0], dc[1]
        danzo_cal = str(n1 * n2)
        for i in range(len(danzo_cal)-1):
            if int(danzo_cal[i]) > int(danzo_cal[i+1]):
                break
        else:
            result.append(int(danzo_cal))

    if not result:
        answer = -1
    else:
        answer = max(result)

    print(f'#{tc}', answer)
