# 부분집합의 합
import sys
sys.stdin = open('sample_input.txt')

t = int(input())

# 집합 a 정의
a = [n for n in range(1,13)]

for tc in range(1,t+1):
    # n = 부분집합 원소의 개수, k = 부분집합 원소의 합계
    n, k = map(int,input().split())
    # answer = 조건에 맞는 부분집합 개수를 카운트하는 변수
    answer = 0
    
    for i in range(1 << 12):
        # subset = 부분집합 저장용 임시 리스트
        subset = []
        for j in range(12):
            # 부분집합을 구성하는 원소를 subset에 저장
            if i & (1 << j):
                subset.insert(0,a[j])

        # 부분집합의 원소 수와 원소 합계 조건을 만족하는 경우 카운트 추가
        # sum_temp = 부분집합의 원소 합계를 저장하는 임시 변수
        # len_temp = 부분집합의 원소 개수를 저장하는 임시 변수
        sum_temp = 0
        len_temp = 0
        for sub in subset:
            sum_temp += sub
            len_temp += 1
        if len_temp == n and sum_temp == k:
            answer += 1

    print(f'#{tc} {answer}')