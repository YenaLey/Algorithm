while(1):
    sentence = input()
    stack = list()

    if sentence == "." : #온점만 입력시 종료
        break

    for s in sentence :

        # 열린 괄호라면
        if s == '[' or s == '(' : 
            stack.append(s)

        # 닫힌 괄호 ] 일 때
        elif s == ']' : 
            if len(stack) != 0 and stack[-1] == '[' : #스택이 비어있지 않고, top data가 짝 괄호일 때
                stack.pop()
            else :  # 비어 있거나 짝 괄호가 없을 때
                stack.append(']')
                break
        elif s == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
                break
    if len(stack) == 0 : #스택이 비어있을 경우
        print('yes')
    else :
        print('no')