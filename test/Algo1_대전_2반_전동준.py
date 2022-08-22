# 1. 평지 만들기

t = int(input())

for tc in range(1,t+1):

    # n = 영역의 둘레
    n = int(input())

    # 평탄화 지역 : 좌상단 행, 좌상단 열, 우하단 행, 우하단 열 순서로 입력받기
    lt_col, lt_row, rb_col, rb_row = map(int,input().split())

    # 평탄화 지역 정보 입력
    ground = [list(map(int,input().split())) for _ in range(n)]

    # height_size = 평탄화 할 영역 높이 합계
    # height_count = 평탄화 할 영역 개수
    height_size = 0
    height_count = (rb_col - lt_col + 1) * (rb_row - lt_row + 1)

    # 입력받은 범위의 좌상단~우하단 내에 있는 영역들의 높이 정보 수집
    for col in range(lt_col, rb_col+1):
        for row in range(lt_row, rb_row+1):
            height_size += ground[col][row]

    # 평탄화 기준(평균) : 높이 합계를 영역 개수로 나눈 값의 몫
    normalize = height_size // height_count

    # dig_count = 전 영역 평탄화에 필요한 작업 횟수
    dig_count = 0

    # 범위 내에서 평탄화에 필요한 작업 횟수 계산
    for col in range(lt_col, rb_col+1):
        for row in range(lt_row, rb_row+1):
            # dig = 세부 영역 별 필요 작업 횟수
            dig = ground[col][row] - normalize

            # dig_count에 dig값 계산(dig가 음수인 경우 뺄셈)
            dig_count = dig_count + dig if dig >= 0 else dig_count - dig

    # 결과 출력
    print(f'#{tc} {dig_count}')