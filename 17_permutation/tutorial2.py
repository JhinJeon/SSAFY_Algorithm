# 자기 길이만큼 순열 뽑기(위치 바꾸기)

numbers = [1, 2, 3, 4]


def change_position(n):  # 길이가 n인 배열 대상
    if n == len(numbers):
        print(numbers)
    for i in range(n, len(numbers)):
        # 자리 바꾸기
        numbers[i], numbers[n] = numbers[n], numbers[i]

        # 재귀 호출
        change_position(n+1)

        # 이후 원상복귀
        numbers[i], numbers[n] = numbers[n], numbers[i]


change_position(0)
