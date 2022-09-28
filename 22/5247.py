# 연산
# 제한시간 초과
import sys
sys.stdin = open('sample_input.txt')

# 연산값 목록
ca = [1, -1, 2, -10]     # 3번째 수는 *2


# 연산을 진행하면서 최적의 경우의 수를 도출하는 함수
def calculation(k, find_value, calcount):
    result = [k]
    # bfs로 경우의 수 탐색
    solved = False
    while result:
        for _ in range(len(result)):
            num = result.pop(0)
            if num < 0:
                continue
            for i in range(4):
                if i == 2:
                    val = num * ca[i]
                else:
                    val = num + ca[i]
                if val == find_value:
                    return calcount + 1
                if val >= 0:
                    result.append(val)
        calcount += 1


t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    answer = calculation(n, m, 0)
    print(f'#{tc}', answer)
