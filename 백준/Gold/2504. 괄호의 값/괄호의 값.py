def solve(array):
    stack = []
    tmp = 1
    ans = 0
    for i in range(len(array)):
        if array[i] == '(':
            stack.append(array[i])
            tmp *= 2
        elif array[i] == '[':
            stack.append(array[i])
            tmp *= 3
        elif array[i] == ')':
            if not stack or stack[-1] != '(':
                return 0
            if array[i - 1] == '(':
                ans += tmp
            stack.pop()
            tmp //= 2
        elif array[i] == ']':
            if not stack or stack[-1] != '[':
                return 0
            if array[i - 1] == '[':
                ans += tmp
            stack.pop()
            tmp //= 3
    return ans if not stack else 0

arr = list(input().strip())
print(solve(arr))