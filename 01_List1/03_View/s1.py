import sys
sys.stdin = open("input.txt")

# k는 테스트 케이스 번호를 임의로 정의한 것(기본 input에서 제공하지 않음)
for k in range(1,11):
    # input에 입력되는 세대 수, 아파트 층수를 input() 두 줄에 걸쳐서 입력받기
    n = int(input())
    apartments = list(map(int,input().split()))
    # answer : 조망권이 확보되는 세대 수
    answer = 0
    # 중앙에 있는 세대를 기준으로 양옆 view 비교
    # _a는 왼쪽 두 칸, _b는 왼쪽 한 칸, _c는 오른쪽 한 칸, _d는 오른쪽 두 칸
    for i in range(2,n-2):
        view_a = apartments[i] - apartments[i-2]
        view_b = apartments[i] - apartments[i-1]
        view_c = apartments[i] - apartments[i+1]
        view_d = apartments[i] - apartments[i+2]
        result = min(view_a,view_b,view_c,view_d)

        # view 최소값이 음수인 경우(주변에 자신보다 높은 건물들만 있는 경우)
        if result < 0:
            continue
        # 그렇지 않은 경우에는 조망권이 확보되는 세대 수 추가
        else:
            answer += result

    print(f'#{k} {answer}')