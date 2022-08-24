# 암호생성기


for _ in range(1, 11):
    tc = int(input())
    password = list(map(int, input().split()))
    front_idx = 0
    rear_idx = 7
    while 0 not in password:
        for i in range(1, 6):
            front_pop = password.pop(0)
            front_pop -= i
            if front_pop <= 0:
                password.append(0)
                break
            else:
                password.append(front_pop)

    print(f'#{tc}', *password)
