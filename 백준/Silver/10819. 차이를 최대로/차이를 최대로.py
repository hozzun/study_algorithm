def dfs():
    global answer

    if len(temp) == n:
        cur_sum = 0
        for i in range(n - 1):
            cur_sum += abs(temp[i] - temp[i + 1])
        answer = max(answer, cur_sum)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            temp.append(arr[i])
            dfs()
            temp.pop()
            visited[i] = False


n = int(input())
arr = list(map(int, input().split()))

visited = [False] * n
temp = []
answer = 0

dfs()
print(answer)