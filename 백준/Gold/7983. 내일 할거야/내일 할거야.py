import sys
input = sys.stdin.readline

N = int(input())
arr = []
for tc in range(N):
    d, t = map(int, input().split())
    arr.append((d, t))

arr.sort(key=lambda arr:arr[1], reverse=True)

time = arr[0][1]
for i in range(N):
    time = min(time, arr[i][1]) - arr[i][0]

print(time)