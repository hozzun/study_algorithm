import math

def solve(m, n, k):
    all_v = sum(n)
    all_case = math.comb(all_v, k)
    specific_case = 0
    for i in n:
        specific_case += math.comb(i, k)
    return specific_case / all_case if all_case > 0 else 0.0

m = int(input())
n = list(map(int, input().split()))
k = int(input())
print(solve(m, n, k))