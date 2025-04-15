A, B = map(int, input().split())

result = []
for i in range(1, 1001):
    for j in range(1, i+1):
        result.append(i)

sum_result = sum(result[A-1:B])
print(sum_result)