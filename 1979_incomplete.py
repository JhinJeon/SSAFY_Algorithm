T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int,input().split())
    puzzle = []
    for i in range(n):
        puzzle.append(list(map(int,input().split())))
    answer = 0
    streak = 0
    for i in range(n):	#가로 인덱스
        streakmax = []
        streak = 0
        for j in range(n):
            if puzzle[i][j] == 1:
                streak += 1
            else:
                streak = 0
            if streak >= k:
                streakmax.append(streak)
        for m in streakmax:
            if max(streakmax) != k:
                break
            if m == k:
                answer += 1
    for i in range(n):
        streakmax = []
        sreak = 0
        for j in range(n):  #세로 인덱스
            if puzzle[j][i] == 1:
                streak += 1
            else:
                streak = 0
            if streak >= k:
                streakmax.append(streak)
        for m in streakmax:
            if max(streakmax) != k:
                break
            if m == k:
                answer += 1                 
    print("#"+str(test_case)+" "+str(answer))