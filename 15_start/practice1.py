# 진수 표현
# 비트 연산자 안 쓴 방법

t = int(input())

for tc in range(1, t+1):
    array = input()
    for i in range(0, len(array), 7):
        output = 0
        part = int(array[i:i+7])
        part_str = str(part)

        for j in range(-1, -len(part_str) - 1, -1):
            output += 2 ** ((j * -1) - 1) if int(part_str[j]) else 0
        print(output, end=' ')
