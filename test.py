import sys
sys.stdin = open('sample_input.txt')
# 노선 수
t = int(input())

for test_case in range(1, t + 1):

    # 최대 이동거리, 종점, 충전기 수
    k, n, m = map(int, input().split())

    # 정류장
    stops = list(map(int, input().split()))

    # 목적지 추가
    stops.append(n)

    # 충전소
    stop = 0
    counts = []

    for i in range(len(stops)):

        if stop + k >= stops[i]:
            for j in range(len(stops) - i):
                if stop + k < stops[i + j]:  # 충전 위치와 다음 정류장 거리 비교
                    stop = stops[i + j - 1]  # 다음 충전 위치
                    counts.append(j - 1)  # 리스트에 충전할 정류장 추가

            count = len(counts)

        # 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우
        else:
            count = 0
            break

    print(f'#{test_case} {count}')
