bar_razor = list(input())
answer = 0
st = []

for i in range(len(bar_razor)):

    #열린괄호 (
    if bar_razor[i] == '(':
        st.append('(')

    #닫힌괄호 )
    else:
        if bar_razor[i-1] == '(':  #레이저
            st.pop()
            answer += len(st) #레이저 기준 왼쪽에 토막난 막대기 수 == 스택 속 막대기 수

        else: #막대기 끝
            st.pop() 
            answer += 1

print(answer)