#가장자리부터 중앙까지 왼쪽과 오른쪽이 같은지 확인
T = int(input())
for i in range(1,T+1):  #1부터 T까지
    txt = input()
    if len(txt) == 1:   #텍스트가 외자인 경우
        print("#"+str(i)+" "+'1')   #회문임을 표시(1)
    for j in range(len(txt)//2):    #텍스트가 외자가 아닌 경우
        if txt[j] != txt[-1-j]: #텍스트의 왼쪽과 오른쪽이 다른 경우
            print("#"+str(i)+" "+'0')
            break
        print("#"+str(i)+" "+'1')   #텍스트의 왼쪽과 오른쪽이 같은 경우
        break