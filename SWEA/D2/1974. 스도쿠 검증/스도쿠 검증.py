def block_isvalid(idx_y, idx_x):
    block_test = set()
    for y in range(idx_y, idx_y+3):
        for x in range(idx_x, idx_x+3):
            block_test.add(puzzle[y][x])
    if block_test == sudoku_box:
        return True     # 유효한 블록인 경우 True
    else:
        return False


t = int(input())
input_puzzles = [list(map(int, input().split())) for _ in range(t * 9)]
sudoku_box = set(i for i in range(1, 10))    # 유효성 검사용 집합(1부터 9까지 수가 하나씩 있는지)

for tc in range(t):
    puzzle = list(input_puzzles[(tc*9):(tc*9)+9])
    answer = 1

    for row in range(9):
        col_test = set()
        for col in range(9):
            # 블록(3 * 3 영역) 유효성 검사
            if row % 3 == 0 and col % 3 == 0:
                if not block_isvalid(col, row):
                    answer = 0
                    break

            col_test.add(puzzle[col][row])

        # 행 유효성 검사
        if col_test != sudoku_box:
            answer = 0
            break

        # 열 유효성 검사
        row_test = set(puzzle[row])
        if row_test != sudoku_box:
            answer = 0
            break

    print(f'#{tc+1}', answer)