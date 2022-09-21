# 숫자 정렬(오름차순)
numbers = [3, 32, 29, 58, 2, 1, 69, 99, 74, 82]
answer = []


def number_sort(array):
    for i in range(len(array)):
        min_index = i       # 최솟값의 인덱스 번호(기본값 = 정렬 범위의 맨 앞쪽)

        for j in range(i+1, len(array)):
            # 새로운 최솟값이 발견되면 값 갱신
            if array[min_index] > array[j]:
                min_index = j

        # 탐색 범위의 맨 앞쪽 값과 최솟값 위치 맞바꾸기
        array[i], array[min_index] = array[min_index], array[i]


number_sort(numbers)
print(numbers)
