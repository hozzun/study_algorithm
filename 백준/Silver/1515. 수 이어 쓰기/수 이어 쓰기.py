arr = list(input().strip())

n = 1
idx = 0
while idx < len(arr):
    for i in str(n):
        if idx < len(arr) and arr[idx] == i:
            idx += 1

    n += 1

print(n - 1)