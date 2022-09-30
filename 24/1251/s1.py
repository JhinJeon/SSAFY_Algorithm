# 하나로
import sys
sys.stdin = open('re_sample_input.txt')


# 끝까지 거슬러 올라가서 근본 부모 노드를 찾는 함수(경로 압축)
def find_set(node):
    if node != parents[node]:        # 부모 노드가 자기 자신이 아니면 반복
        parents[node] = find_set(parents[node])
    # 부모 노드가 자기 자신이면 해당 값 반환(대표값)
    return parents[node]


t = int(input())

for tc in range(1,t+1):
    island_count = int(input())                         # 섬의 개수
    island_x = list(map(int, input().split()))          # 섬들의 x좌표
    island_y = list(map(int, input().split()))          # 섬들의 y좌표
    taxrate = float(input())                            # 세율(0 이상 1 이하의 소수)

    estimates = []     # 현재 섬(인덱스 번호)에서 다른 섬을 연결할 때 발생하는 비용

    for i in range(island_count):
        for j in range(island_count):
            # i번 섬에서 j번 섬을 잇는 터널을 공사하는 데 필요한 비용 추가(비용, 출발 섬 번호,  도착 섬 번호)
            if i != j:
                cost = (abs(island_x[j] - island_x[i]) ** 2 + abs(island_y[j] - island_y[i]) ** 2)
                estimates.append((cost, i, j))

    # 오름차순으로 정렬
    estimates.sort()

    counts = 0  # 간선 개수(개수가 (정점-1)개가 되면 종료)
    cost = 0  # 공사비용 총합
    parents = list(range(island_count))

    # 최소 공사비용(cost) 도출
    for dist, x, y in estimates:
        x_root, y_root = find_set(x), find_set(y)

        if x_root != y_root:
            parents[y_root] = x_root
            cost += dist
            counts += 1

            if counts >= island_count - 1:
                break

    # 최소 환경 부담금을 출력
    answer = round(cost * taxrate)
    print(f'#{tc}', answer)