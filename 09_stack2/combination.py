# 조합

def combinations(arr, start):
    if len(arr) == length:
        print(arr)
        return

    for i in range(start, len(numbers)):
        arr.append(numbers[i])

        # 다음에 뽑을 숫자는 현재 숫자보다 오른쪽에 있어야 함
        combinations(arr, i + 1)

        arr.pop()

numbers = [1,2,3,4]
length = 3

combinations([], 0)