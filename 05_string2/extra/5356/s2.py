import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1,t+1):
    board = [list(input()) for _ in range(5)]

    # answer = 출력할 문자열을 저장하는 변수
    answer = ''
    board_len_max = 0
    
    # board_len_max = board를 구성하는 row들 중 가장 긴 값
    for rows in board:
        if len(rows) > board_len_max:
            board_len_max = len(rows)

    # row 인덱스가 유효한 경우 행 인덱스를 따라 세로로 읽기
    # 읽은 값은 answer에 추가
    for row in range(board_len_max):
        for col in range(5):
            # 유효한 인덱스가 아닌 경우 값을 읽지 않음
            if row >= len(board[col]):
                continue
            answer += board[col][row]

    print(f'#{tc} {answer}')