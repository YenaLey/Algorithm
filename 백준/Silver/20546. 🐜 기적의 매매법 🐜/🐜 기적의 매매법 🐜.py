cash = int(input())
stock_list = list(map(int, input().split()))

def BNP(cash, stock_list):
    count = 0
    for stock in stock_list:
        if cash >= stock:
            count += cash // stock
            cash %= stock  # cash = cash % stock (연산 최적화)
    return cash + stock_list[-1] * count

def TIMING(cash, stock_list):
    count = 0

    for i in range(3, len(stock_list)):
        # 최근 3일간 주가 상승 또는 하락 여부 확인 (가독성 개선)
        up_trend = stock_list[i] > stock_list[i-1] > stock_list[i-2] > stock_list[i-3]
        down_trend = stock_list[i] < stock_list[i-1] < stock_list[i-2] < stock_list[i-3]

        if up_trend:  # 3일 연속 상승 → 전량 매도
            cash += count * stock_list[i]
            count = 0
        elif down_trend:  # 3일 연속 하락 → 전량 매수
            if cash >= stock_list[i]:
                count += cash // stock_list[i]
                cash %= stock_list[i]

    return cash + stock_list[-1] * count

# 💡 BNP와 TIMING을 각각 1번만 계산하여 최적화
bnp_result = BNP(cash, stock_list)
timing_result = TIMING(cash, stock_list)

if bnp_result > timing_result:
    print("BNP")
elif bnp_result < timing_result:
    print("TIMING")
else:
    print("SAMESAME")
