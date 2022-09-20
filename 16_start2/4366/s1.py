# 정식이의 은행 업무

t = int(input())

for tc in range(1,t+1):
    digit_2 = input()  # 이진수
    digit_3 = input()  # 삼진수
    answer = None

    for i2 in range(1, len(digit_2)):   # 이진수의 자릿수 슬라이싱 : 이진수는 첫 번째 자리수는 무조건 1
        for i3 in range(len(digit_3)):  # 삼진수의 자릿수 슬라이싱 : 삼진수는 첫째 자리수도 1,2가 등장할 수 있음
            for c2 in range(2):         # i2의 자릿수에 대체할 숫자
                for c3 in range(3):     # i3의 자릿수에 대체할 숫자
                    d2_case = digit_2[:i2] + str(c2) + digit_2[i2+1:]   # 이진수에서 자리수 하나만 바꾸기
                    d3_case = digit_3[:i3] + str(c3) + digit_3[i3+1:]   # 삼진수에서 자리수 하나만 바꾸기
                    
                    # 자릿수를 바꾼 수들을 십진수화 해서 크기 비교
                    v2 = int(d2_case,2)
                    v3 = int(d3_case,3)

                    # 값이 동일한 경우 출력 후 반복문 종료
                    if int(d2_case,2) == int(d3_case,3):
                        answer = int(d2_case, 2)
                        print(f'#{tc}', answer)
                        break
                if answer:
                    break
            if answer:
                break
        if answer:
            break



