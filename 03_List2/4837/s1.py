# 부분집합의 합
import sys
sys.stdin = open('sample_input.txt')

t = int(input())

# 집합 a 정의
a = [1,2,3,4,5,6,7,8,9,10,11,12]

for tc in range(1,t+1):
    # n = 부분집합 원소의 개수, k = 부분집합 원소의 합계
    n, k = map(int,input().split())
    # answer = 조건에 맞는 부분집합 개수를 카운트하는 변수
    answer = 0
    
    for i in range(1 << 12):
        # sum_temp = 부분집합 원소의 합계를 저장할 임시 변수
        # element_count = 부분집합 원소의 개수를 저장할 임시 변수
        sum_temp = 0
        element_count = 0
        for j in range(12):
            # 부분집합이 값이 추가될 때 원소 개수와 합계를 임시 변수에 저장
            if i & (1 << j):
                sum_temp += a[j]
                element_count += 1

        # 부분집합의 원소 수와 원소 합계 조건을 만족하는 경우 카운트 추가
        if element_count == n and sum_temp == k:
            answer += 1

    print(f'#{tc} {answer}')