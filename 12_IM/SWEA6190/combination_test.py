# 정곤이의 단조 증가하는 수

length = 2
result = []
danzo = [1,5,8,9]


def combinations(arr, start):
    global result
    if len(arr) == length:
        result += arr
        return

    else:
        for i in range(start, len(danzo)):
            arr.append(danzo[i])

            # 다음에 뽑을 숫자는 현재 숫자보다 오른쪽에 있어야 함
            combinations(arr, i + 1)

            arr.pop()


combinations([],0)
print(result)