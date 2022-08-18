# 종이붙이기

# 종이를 붙일 수 있는 경우의 수를 반환하는 get_deploy_case 함수 정의
def get_deploy_case(size):
    # 가로 길이가 10이나 20인 경우 2n-1가지 방법 가능
    if size <= 2:
        return 2 * size - 1
    # 가로 길이가 20 초과인 경우 홀수는 2n-1가지, 짝수는 2n-3가지 가능
    else:
        if size % 2 == 0:
            return 2 * get_deploy_case(size-1) + 1
        else:
            return 2 * get_deploy_case(size-1) - 1

t = int(input())

for tc in range(1,t+1):
    n = int(input())
    # width = 함수에 입력할 수 있도록 단위 축소
    width = n // 10
    answer = get_deploy_case(width)
    print(f'#{tc} {answer}')



# 규칙 : 1 3 5 11 21 43 85
# n이 짝수 번째면 2(n-1) + 1 = 2n - 1
# n이 홀수 번째면 2(n-1) -1 = 2n - 3