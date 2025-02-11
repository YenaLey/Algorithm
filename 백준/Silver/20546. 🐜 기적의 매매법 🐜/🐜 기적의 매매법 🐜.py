cash = int(input())
stock_list = list(map(int, input().split()))

def BNP(cash, stock_list):
  count = 0
  for stock in stock_list:
    if cash >= stock:
      count += cash // stock
      cash = cash % stock
  return cash + stock_list[-1] * count

def TIMING(cash, stock_list):
  count = 0

  for i in range(3, len(stock_list)):

    if (stock_list[i]-stock_list[i-1] > 0 and stock_list[i-1]-stock_list[i-2] > 0 and stock_list[i-2]-stock_list[i-3] > 0): # 3일 연속 상승한 경우 (전량 매도)
      cash += count * stock_list[i]
      count = 0

    elif (stock_list[i]-stock_list[i-1] < 0 and stock_list[i-1]-stock_list[i-2] < 0 and stock_list[i-2]-stock_list[i-3] < 0): # 3일 연속 하락한 경우 (전량 매수)
      if cash >= stock_list[i]:
        count += cash // stock_list[i]
        cash = cash % stock_list[i]

  return cash + stock_list[-1] * count

if BNP(cash, stock_list) > TIMING(cash, stock_list):
  print("BNP")
elif BNP(cash, stock_list) < TIMING(cash, stock_list):
  print("TIMING")
else:
  print("SAMESAME")