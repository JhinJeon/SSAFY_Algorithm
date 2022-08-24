# 부분집합

powerset = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


def get_subset(n, k):   # n = 원소 번호(값), k = 집합 개수
    if n == k:
        return k
