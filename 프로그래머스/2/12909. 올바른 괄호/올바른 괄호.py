def solution(s):
    answer = False

    stack = []
    for parenthesis in s:
        if parenthesis == '(':
            stack.append(parenthesis)
        elif stack and parenthesis == ')':
            stack.pop()
        elif stack == [] and parenthesis == ')':
            return False
    
    if stack == []:
        answer = True
    
    return answer