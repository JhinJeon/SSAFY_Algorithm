import sys
sys.stdin = open("sample_input.txt")

t = int(input())

for tc in range(1,t+1):
    # n = 숫자열 길이
    # m = 연속으로 더하려는 숫자 개수
    n, m = map(int,input().split())
    # numbers = 숫자열 정보
    numbers = list(map(int,input().split()))
    # 숫자열의 맨 처음부터 m번째 수까지 더한 값을 최대값과 최소값의 기본값으로 설정
    total_min = sum(numbers[0:m])
    total_max = sum(numbers[0:m])
    
    for i in range(n-m+1):
        # 새로운 최대값(최소값)이 등장하는 경우 해당 값으로 변경
        total_case = sum(numbers[i:i+m])
        if total_case > total_max:
            total_max = total_case
        if total_case < total_min:
            total_min = total_case

    print(f'#{tc} {total_max - total_min}')
