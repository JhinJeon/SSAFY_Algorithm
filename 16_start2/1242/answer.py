# 1242. [S/W 문제해결 응용] 1일차 - 암호코드 스캔
import sys

sys.stdin = open('sample_input.txt')

code_dict = {
    "211": "0",
    "221": "1",
    "122": "2",
    "411": "3",
    "132": "4",
    "231": "5",
    "114": "6",
    "312": "7",
    "213": "8",
    "112": "9",
}


def bin_return(n):
    s = ""
    for m in range(3, -1, -1):
        s += "1" if n & (1 << m) else "0"
    return s


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # breaker = False
    answer = 0
    duplicated_set = set()
    for i in range(N):
        row = input().strip()
        bin_row = ""

        # if not breaker:
        for j in row:
            bin_row += bin_return(int(j, 16))
        # print(bin_row)
        bin_ratio = []
        cnt_0 = 0
        cnt_1 = 0
        decode = []

        for k in range(len(bin_row) - 1, -1, -1):
            if bin_row[k] == '1':
                if cnt_0:
                    bin_ratio.insert(0, cnt_0)
                    cnt_0 = 0
                cnt_1 += 1
            if bin_row[k] == '0':
                if cnt_1:
                    bin_ratio.insert(0, cnt_1)
                    cnt_1 = 0
                if bin_ratio:
                    cnt_0 += 1

            if len(bin_ratio) == 3:
                d = min(bin_ratio)
                str_bin_ratio = "".join(list(map(lambda x: str(x//d), bin_ratio)))
                if str_bin_ratio in code_dict.keys():
                    decode.insert(0, int(code_dict[str_bin_ratio]))
                    cnt_0 = 0
                    cnt_1 = 0
                    bin_ratio = []
                if len(decode) == 8:
                    str_decode = "".join(list(map(str, decode)))
                    if str_decode not in duplicated_set:
                        duplicated_set.add(str_decode)
                        if (sum(decode[0:8:2]) * 3 + sum(decode[1:8:2])) % 10 == 0:
                            # breaker = True
                            answer += sum(decode)
                    decode = []
                # if breaker:
                #     break
    print(f"#{tc} {answer}")