N = int(input())

arr = []
for _ in range(N):
    txt = input()
    if txt not in arr and txt.isnumeric() == False:
        arr.append(txt)

arr.sort()
arr.sort(key = len)

print(*arr, sep='\n')