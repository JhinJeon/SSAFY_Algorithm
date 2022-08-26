# 정곤이의 단조 증가하는 수

'''
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
'''

length = 2


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
    result = []

    if len(danzo) == 1:
        danzo_check(str(danzo[0]))
    else:
        combinations([], 0)
        for i in range(len(danzo), 2):
            dz = result[i] * result[i + 1]
            danzo_check(str(dz))

    print(f'#{tc}', danzo_max)