#가로, 세로, 블록 안에 있는 숫자 개수가 중복 제외하고 9개인지 확인하는 원리로 코드 작성
t = int(input())
sudoku = []
for i in range(t*9):
    sudoku.append(list(map(int,input().split())))
for x in range(t):
    temp = []    
    answer = 1
    graph = sudoku[x*9:(x+1)*9]
    for i in range(9):  #각 열의 숫자 종류가 9종인지 확인
        temp = []
        for j in range(9):
            temp.append(graph[i][j])
        bucket = list(set(temp))
        if len(bucket) != 9:
            answer = 0
            continue
    for i in range(9):  #각 행의 숫자 종류가 9종인지 확인
        temp = []
        for j in range(9):
            temp.append(graph[j][i])
        bucket = list(set(temp))
        if len(bucket) != 9:
            answer = 0
            continue
    temp = []
    for a in range(0,7,3):  #블록 안의 숫자가 9종인지 확인
        for b in range(0,7,3):
            for c in range(3):
                for d in range(3):
                    temp.append(graph[a+c][b+d])
            bucket = list(set(temp))
            if len(bucket) != 9:
                answer = 0
                continue
            else:
                temp = []
    print('#'+str(x+1)+' '+str(answer))