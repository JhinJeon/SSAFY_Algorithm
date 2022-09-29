# 홈 방범 서비스

t = int(input())

for tc in range(1,t+1):
    n, wtp = map(int,input().split())

    array = [list(map(int,input().split())) for _ in range(n)]      # 방범 대상 구역
    print(f'#{tc}')