

def mid_search(k):
    if k * 2 <= m:
        mid_search(k * 2)
    print(node_value[k], end=' ')
    if k * 2 < m:
        mid_search(k * 2)
    return


n, m = map(int,input().split())

node_value = [0] * n
left_child = [0] * n
right_child = [0] * n

node_info = list(map(int, input().split()))

for i in range(m):
    node_value[i+1] = node_info[2 * i]
    if not left_child[i]:
        left_child[i+1] = node_info[2 * i+1]
    elif not left_child[i]:
        right_child[i+1] = node_info[2 * i+1]

print('중위 순회', end=' ')
mid_search(1)
