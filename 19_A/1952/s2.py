# 수영장
import sys
sys.stdin = open('sample_input.txt')


def dfs(k, case_sum):
    global monthly_plan, fee_sum, start
    result = start + case_sum
    if k >= 12:
        if fee_sum > result:
            fee_sum = result
        return
    for i in range(k, 12):
        if fee_plan[i]:
            if sum(fee_plan[i:i + 3]) > quarter:
                case_sum += quarter
                dfs(k+3, case_sum)
                case_sum -= quarter
            else:
                case_sum += fee_plan[i]
                dfs(k+1, case_sum)
                case_sum -= fee_plan[i]
    else:
        if fee_sum > result:
            fee_sum = result
        return


t = int(input())

for tc in range(1,t+1):
    # 수영장 요금(1일, 1주, 3달, 1년)
    daily, monthly, quarter, annual = map(int,input().split())
    # 수영장 이용 계획
    fee_sum = max(daily, monthly, quarter, annual) * 12
    monthly_plan = list(map(int,input().split()))
    fee_plan = [0] * 14

    for m in range(12):
        playtime = monthly_plan[m]
        daily_fee = daily * playtime
        if playtime and daily_fee > monthly:
            fee_plan[m] = monthly
        else:
            fee_plan[m] = daily_fee

    for i in range(12):
        start = sum(fee_plan[:i])
        dfs(i, 0)

    if fee_sum > annual:
        fee_sum = annual

    print(f'#{tc}', fee_sum)


# 10 30 50 500
# 0 0 20 30 0 30 20