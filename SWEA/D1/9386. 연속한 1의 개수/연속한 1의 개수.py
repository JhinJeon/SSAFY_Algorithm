for t in range(1, int(input()) + 1):
    n = int(input())
    numbers = input()
    streak = 0
    answer = 0
    for i in numbers:
        if int(i) == 1:
            streak += 1
        else:
            if answer < streak:
                answer = streak
            streak = 0
    if answer < streak:
        answer = streak

    print(f'#{t} {answer}')