import sys

# 테스트 인풋(sample_input) 불러오기
sys.stdin = open('sample_input.txt')

# 테스트 케이스 횟수
t = int(input())

for k in range(1,t+1):
    # n = 리스트 길이
    n = int(input())
    # numbers = 리스트를 구성하는 숫자들
    numbers = list(map(int,input().split()))
    # 리스트의 첫 번째 값을 최소값, 최대값으로 설정
    num_min = numbers[0]
    num_max = numbers[0]
    # 리스트의 두 번째 값부터 최소값, 최대값과 비교
    for i in range(1,n):
        if num_min > numbers[i]:
            num_min = numbers[i]
        if num_max < numbers[i]:
            num_max = numbers[i]
    print(f'#{k} {num_max - num_min}')
