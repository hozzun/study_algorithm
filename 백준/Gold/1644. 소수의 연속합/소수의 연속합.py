n = int(input())
prime_numbers = []
check = [False] * (n + 1)

for i in range(2, n + 1):
    if not check[i]:
        prime_numbers.append(i)
    for j in range(i * 2, n + 1, i):
        check[j] = True

count = 0
left = 0
right = 0
cur_sum = 0 if not prime_numbers else 2

while left < len(prime_numbers):
    if cur_sum == n:
        count += 1
        cur_sum -= prime_numbers[left]
        left += 1
    elif cur_sum > n:
        cur_sum -= prime_numbers[left]
        left += 1
    else:
        right += 1
        if right < len(prime_numbers):
            cur_sum += prime_numbers[right]
        else:
            break

print(count)