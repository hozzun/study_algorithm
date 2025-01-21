n = int(input())

stack = []
ans = 0

for _ in range(n):
    x, y = map(int, input().split())

    while stack and stack[-1] > y:
        stack.pop()
        ans += 1

    if not stack or stack[-1] < y:
        stack.append(y)

ans += len(stack) - stack.count(0)
print(ans)