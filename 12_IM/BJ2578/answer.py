# 빙고판 채우기
bingo = []
bingoCheck = [[0 for j in range(5)] for i in range(5)]
for _ in range(5):
    bingo.append(input().split())

# 빙고판 체크
for i in range(5):
    fiveBingo = input().split()
    for j in range(5):
        # 빙고판 돌면서 찾기
        for ci in range(5):
            for cj in range(5):
                if bingo[ci][cj] == fiveBingo[j]:
                    bingoCheck[ci][cj] = 1  # 부른 수 체크
                    break  # 딱 한번임 => ci를 안 나갔다!!!!!!!!!!!!!!!!!!
            if bingo[ci][cj] == fiveBingo[j]:
                break

        # 빙고판 체크하면 매번 빙고 몇 개인지 확인
        numOfBingo = 0

        # 가로줄 개수 확인
        for row in range(5):
            if all(bingoCheck[row][:]):
                numOfBingo += 1

        if numOfBingo == 3:
            print(i * 5 + j + 1)
            break

        # 세로줄 개수 확인
        for col in range(5):
            for row in range(5):
                if bingoCheck[row][col] == 0:
                    break
            else:
                numOfBingo += 1

        if numOfBingo == 3:
            print(i * 5 + j + 1)
            break

        # 대각선 개수 확인
        for col in range(5):
            if bingoCheck[col][col] == 0:
                break
        else:
            numOfBingo += 1

        if numOfBingo == 3:
            print(i * 5 + j + 1)
            break

        for col in range(5):
            if bingoCheck[col][4 - col] == 0:
                break
        else:
            numOfBingo += 1

        if numOfBingo == 3:
            print(i * 5 + j + 1)
            break
    if numOfBingo >= 3:
        break