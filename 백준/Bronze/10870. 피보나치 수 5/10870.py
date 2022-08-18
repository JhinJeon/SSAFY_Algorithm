# 피보나치 수 5

n = int(input())

# 피보나치 수열의 num번째 수를 반환하는 fibonacci 함수 정의
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(n))
