# 버블 정렬

test_list = [1, 3, 5, 7, 0, 9, 8, 6, 10, 2, 4]

# 오름차순(작은 수부터) 정렬

for i in range(len(test_list)):
    for j in range(i, len(test_list)):
        if test_list[i] > test_list[j]:
            test_list[i], test_list[j] = test_list[j], test_list[i]

# 확인해 보자
print(test_list)

# 3개씩 묶은 부분합의 합계 구하기(슬라이딩 윈도우)

idx = 0
result = sum(test_list[idx:idx+3])
answer = sum(test_list[0:3])
for i in range(len(test_list)-3):
    result = result - test_list[i] + test_list[i+3]
    answer += result

print(answer)
