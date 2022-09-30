# 연산
# deque 사용
# import sys
# sys.stdin = open('sample_input.txt')


from collections import deque


# BFS로 연산을 진행하면서 최적의 경우의 수를 도출하는 함수
def calculation(k, find_value, calcount):
    result = deque()
    result.append([k, calcount])
    # 중복 여부 체크
    overlap = [False] * (10**6 +1)
    while result:
        num, calcount = result.popleft()
        # 이미 등장했던 숫자면 continue
        if overlap[num]:
            continue
        overlap[num] = True     # 숫자 등장 처리
        # 찾으려 했던 숫자면 탐색 횟수 반환
        if num == find_value:
            return calcount
        calcount += 1
        # 이하 +1, -1, *2, -10 연산
        val = num + 1
        if 0 < val <= 1000000:
            result.append([val, calcount])
        val = num - 1
        if 0 < val <= 1000000:
            result.append([val, calcount])
        val = num * 2
        if 0 < val <= 1000000:
            result.append([val, calcount])
        val = num - 10
        if 0 < val <= 1000000:
            result.append([val, calcount])


t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    answer = calculation(n, m, 0)
    print(f'#{tc}', answer)
