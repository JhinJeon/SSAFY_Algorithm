# 카드1

n = int(input())    # 카드 장수이자 가장 아래에 있는 카드

deck = [i for i in range(1,n+1)]  # 1번부터 n번까지의 카드로 구성된 큐 생성
act = 0     # 카드를 버릴지, 큐에 다시 입력할지 결정하는 용도(짝수 = 버리기, 홀수 = 다시 섞기)

while deck:     # deck에 카드가 소진될 때까지 반복
    topdeck = deck.pop(0)   # topdeck = 덱 맨 위에서 뽑은 카드(큐의 반환값)

    if act % 2 == 1:    # act가 홀수인 경우 다시 섞기
        deck.append(topdeck)
    else:   # act가 짝수인 경우 버리기(버리는 카드 출력)
        print(topdeck, end=' ')
    act += 1
