import sys
sys.stdin = open('sample_input.txt')


# 퀵 정렬 함수(파이썬식 방법)
# 코드는 간결하고 안정적이지만(중복된 값의 인덱스가 바뀔 일이 없지만) 메모리 사용량이 많음
# 병합 정렬과 유사
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]      # 피벗 값(중앙으로 설정)
    lesser_arr, equal_arr, greater_arr = [], [], []     # 피벗보다 작은 값, 피벗과 동일한 값(중복), 피벗보다 높은 값
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    # 분류된 리스트 재귀 호출
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    array = list(map(int,input().split()))      # 정렬 전 리스트
    answer = quick_sort(array)[n//2]            # 정렬된 리스트의 n//2번 인덱스의 값
    
    print(f'#{tc}', answer)