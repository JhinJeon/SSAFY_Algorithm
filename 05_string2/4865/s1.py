# 글자수

t = int(input())

for tc in range(1,t+1):
    # cnt_max = 문자열 개수의 최대값을 저장하는 변수
    # str1은 중복을 제거하기 위해 set 형태로 저장
    str1 = set(list(input()))
    str2 = input()
    cnt_max = 0
    
    # cnt = str2에서 str1에 있는 문자 개수를 임시로 저장하는 변수
    for s1 in str1:
        cnt = 0
        for s2 in str2:
            # str1을 구성하는 문자가 str2에도 있는 경우 개수 카운트
            if s1 == s2:
                cnt += 1
                # 최댓값을 갱신하는 경우 cnt_max 값 수정
                if cnt > cnt_max:
                    cnt_max = cnt

    print(f'#{tc} {cnt_max}')