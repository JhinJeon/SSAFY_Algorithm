# DFS, BFS를 고집할 필요는 없다
# 이차원 배열에 대한 기본적인 이해를 묻는 문제
import sys
sys.stdin = open('input.txt')

# 빙고판 채우기
bingo = [list(map(int,input().split())) for _ in range(5)]

# 빙고 체크용
bingoCheck = [[0 for j in range(5)] for i in range(5)]

# 사회자가 부르는 수
bingo_call = []
for _ in range(5):
    bingo_call += list(map(int, input().split()))

# 빙고판 체크
for call in range(len(bingo_call)):
    checked = False
    for col in range(5):
        for row in range(5):
            if bingo[col][row] == bingo_call[call]:
                bingoCheck[col][row] = 1  # 부른 수 체크
                checked = True
                break
        if checked:
            break

    # 빙고판 체크하면 매번 빙고 몇 개인지 확인
    numOfBingo = 0

    # 가로줄 개수 확인
    for row in range(5):
        if 0 not in bingoCheck[row]:
            numOfBingo += 1

    if numOfBingo == 3:
        print(call + 1)
        break

    # 세로줄 개수 확인
    for col in range(5):
        for row in range(5):
            if bingoCheck[row][col] == 0:
                break
        else:
            numOfBingo += 1

    if numOfBingo == 3:
        print(call + 1)
        break

    # 대각선 개수 확인(오른쪽 아래 방향)
    for col in range(5):
        if bingoCheck[col][col] == 0:
            break
    else:
        numOfBingo += 1

    if numOfBingo == 3:
        print(bingo_call.index(call) + 1)
        break

    # 대각선 개수 확인(오른쪽 위 방향)
    for col in range(5):
        if bingoCheck[col][4 - col] == 0:
            break
    else:
        numOfBingo += 1

    if numOfBingo >= 3:
        print(call + 1)
        break