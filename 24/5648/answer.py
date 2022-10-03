import sys
sys.stdin = open('sample_input.txt')

dx = [0, 0, -1, 1]  # 상 하 좌 우
dy = [1, -1, 0, 0]
for tc in range(1, 1 + int(input())):
    n = int(input())
    atoms = []
    for i in range(n):
        x, y, d, k = map(int, input().split())
        x = (x + 1000) * 2              # 음수 좌표를 양수로 넓히고,
        y = (y + 1000) * 2              # 0.5씩 이동시키지말고, 배열을 2배 늘리고 1씩 이동시킨다.
        atoms.append([x, y, d, k])      # 원자들의 상태를 담을 배열

    total = 0
    while len(atoms) >= 2:      # 2개 이상이어야 충돌한다.
        loc = []                # 이동하는 위치 기억(충돌 확인을 위함)
        hit = set()             # 충돌되는지 확인
        nxt_atoms = []          # 이동한 원자들의 상태를 담을 배열
        for i in range(len(atoms)):
            x, y, d, k = atoms[i]
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx <= 4000 and 0 <= ny <= 4000:     # 배열의 크기를 넘으면 제거한다.
                if (nx, ny) in loc:     # 동일 위치가 또 나오면 충돌!
                    hit.add((nx, ny))
                else:                   # 아니면 위치를 새로 추가
                    loc.append((nx, ny))
                nxt_atoms.append((nx, ny, d, k))    # 원자들의 다음 상태들을 담아준다.
        atoms = []          # 사용할 원자 배열을 초기화
        for i in range(len(nxt_atoms)):     # 이동한 원자들을 순회
            x, y, d, k = nxt_atoms[i]
            if (x, y) in hit:               # 부딪힌 위치에 있으면 total에 k를 더한다.
                total += k
            else:                           # 안 부딪혔으면 원자 배열에 담아준다.
                atoms.append((x, y, d, k))
    print(f'#{tc} {total}')
