N = int(input())

for _ in range(N):
    cnt = []
    arr = list(map(str, input().rstrip()))
    for j in range(len(arr)):
        if arr[j] == '(':
            cnt.append(arr[j])
        elif arr[j] == ')':
            if '(' in cnt:
                cnt.pop()
            else:
                cnt.append(arr[j])

    if len(cnt) == 0:
        print('YES')
    else:
        print('NO')