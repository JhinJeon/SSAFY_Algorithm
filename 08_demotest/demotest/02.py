# 퍼펙트 셔플

t = int(input())

for tc in range(1,t+1):
    n = int(input())
    deck_list = list(input().split())
    if n % 2 == 0:
        shuffle_standard = n // 2
    else:
        shuffle_standard = n // 2 + 1
    decksplit_top = deck_list[:shuffle_standard]
    decksplit_bottom = deck_list[shuffle_standard:]
    shuffled_deck = []
    for i in range(n):
        if i % 2 == 0:
            shuffled_deck.append(decksplit_top[i//2])
        else:
            shuffled_deck.append(decksplit_bottom[i//2])
    print(f'#{tc}', *shuffled_deck)