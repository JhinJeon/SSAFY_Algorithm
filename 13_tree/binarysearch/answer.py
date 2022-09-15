def bst(n):
    global cnt
    if n * 2 <= N:
        bst(n * 2)

    tree[n] = cnt
    cnt += 1

    if n * 2 + 1 <= N:
        bst(n * 2 + 1)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    tree = [0] * (N + 1)
    cnt = 1
    bst(1)

    print(f"#{tc} {tree[1]} {tree[N // 2]}")