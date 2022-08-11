numbers = [1,2,3,4]
n = len(numbers)

for i in range(1 << n):
    for j in range(n):
        # 부분집합에 속하는 원소 출력(end = ' '로 정해서 한 집합의 원소면 공백을 단위로 출력되도록 설정)
        if i & (1 << j): # & : i와 j가 동일하면 이하 조건문 실행
            print(numbers[j], end =' ')
    print()