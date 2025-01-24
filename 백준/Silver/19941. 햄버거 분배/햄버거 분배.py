n, k = map(int, input().split())
arr = list(input().strip())

cnt = 0
check = [False] * n

for idx, i in enumerate(arr):
    if i == 'P':
        for j in range(max(0, idx-k), min(n, idx+k+1)):
            if arr[j] == 'H' and not check[j]:
                cnt += 1
                check[j] = True
                break

print(cnt)