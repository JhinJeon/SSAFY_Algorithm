# SWEA - GNS
import sys
sys.stdin = open('GNS_test_input.txt')

words = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
numbers = [0,1,2,3,4,5,6,7,8,9]

t = int(input())

for tc in range(1,t+1):
    tc_no, n = input().split()
    n = int(n)
    letter_list = list(input().split())

    for j in range(n):
        for i in range(10):
            if letter_list[j] == words[i]:
                letter_list[j] = numbers[i]

    letter_list.sort(reverse=False)

    for j in range(n):
        for i in range(10):
            if letter_list[j] == numbers[i]:
                letter_list[j] = words[i]


    print(f'#{tc}')
    print(*letter_list)