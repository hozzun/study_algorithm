n = int(input())
qualities = list(map(int, input().split()))
qualities.sort()

answer = sum(qualities[(n + 1) // 2:]) * 2

if n % 2 == 1:
    answer += qualities[n // 2]

print(answer)