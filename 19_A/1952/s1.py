# 수영장
import sys
sys.stdin = open('sample_input.txt')


t = int(input())

for tc in range(1,t+1):
    # 수영장 요금(1일, 1주, 3달, 1년)
    daily, monthly, quarter, annual = map(int,input().split())
    # 수영장 이용 계획
    monthly_plan = list(map(int,input().split()))
    fee_plan = [0] * 14
    fee_sum = 0

    for m in range(12):
        playtime = monthly_plan[m]
        daily_fee = daily * playtime
        if playtime and daily_fee > monthly:
            fee_plan[m] = monthly
        else:
            fee_plan[m] = daily_fee

    for i in range(12):
        if fee_plan[i]:
            if sum(fee_plan[i:i+3]) > quarter:
                fee_sum += quarter
                for j in range(3):
                    fee_plan[i + j] = 0
            else:
                fee_sum += fee_plan[i]

    if fee_sum > annual:
        fee_sum = annual

    print(f'#{tc}', fee_sum)