t = int(input())

for tc in range(1,t+1):
    trial = 0
    original_data = list(str(input()))
    initialize = list('0' * len(original_data))

    for bit in range(len(initialize)):
        if original_data[bit] != initialize[bit]:
            if initialize[bit] == '0':
                change_to = '1'
            else:
                change_to = '0'
            for i in range(bit,len(initialize)):
                initialize[i] = change_to
            trial += 1

    print(f'#{tc}', trial)