#일부 테스트케이스에서 틀리는 문제 발생
T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int,input().split())
    puzzle = []
    for i in range(n):
        puzzle.append(list(map(int,input().split())))
    answer = 0
    for i in range(n):	#가로 인덱스
        streakmax = []
        streak = 0
        total = 0
        for j in range(n):
            if puzzle[i][j] == 1:
                streak += 1
            else:
                streakmax.append(streak)
                streak = 0
        streakmax.append(streak)
        if k in streakmax:
            total = streakmax.count(k)
        answer += total
    for i in range(n):
        streakmax = []
        streak = 0
        total = 0
        for j in range(n):  #세로 인덱스
            if puzzle[j][i] == 1:
                streak += 1
            else:
                streakmax.append(streak)
                streak = 0
        streakmax.append(streak)
        if k in streakmax:
            total = streakmax.count(k)
        answer += total   
    print("#"+str(test_case)+" "+str(answer))