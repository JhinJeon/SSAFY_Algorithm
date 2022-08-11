import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    divider = [2, 3, 5, 7, 11]
    answer = [0, 0, 0, 0, 0]
    d = 5
    while d > 0:
        for i in range(len(divider)):
            while True:
                if n % divider[i] == 0:
                    answer[i] += 1
                    n = n / divider[i]
                else:
                    d -= 1
                    break

    print(f'#{tc}', end=' ')
    for i in answer:
        print(str(i), end=' ')
    print()