# 2. 같은 모양 찾기

t = int(input())    # t = 테스트 케이스 개수

for tc in range(1, t+1):
    n = int(input())    # 입력받는 그래프의 크기(n * n)

    # graph = 이차원 배열 정보
    graph = [list(map(int, input().split())) for _ in range(n)]

    # standard = graph 내에서 찾을 패턴
    standard = [list(map(int, input().split())) for _ in range(3)]

    # graph 안에 있는 패턴 개수
    answer = 0

    for col in range(n-2):
        for row in range(n-2):
            # 3 * 3 영역을 한 행씩 비교
            for check in range(3):
                # 다른 부분이 있으면 즉시 비교 종료
                if graph[col + check][row:row+3] != standard[check]:
                    break
            # 모두 동일한 경우 패턴 개수 + 1
            else:
                answer += 1
    
    # 결과 출력
    print(f'#{tc} {answer}')

