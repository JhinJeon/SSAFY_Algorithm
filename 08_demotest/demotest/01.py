# 민석이의 과제 체크하기

t = int(input())

for tc in range(1,t+1):
    student, submit = map(int,input().split())
    submit_no = list(map(int,input().split()))
    student_list = [i for i in range(1, student+1)]
    answer = []
    for s in student_list:
        if s not in submit_no:
            answer.append(s)

    answer.sort()

    print(f'#{tc}', *answer)