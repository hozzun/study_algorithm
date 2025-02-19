n = int(input())
budget = sorted(list(map(int, input().split())))
total_budget = int(input())

limit = 0
if total_budget >= sum(budget):
    print(budget[-1])

else:
    total = 0
    rest = n
    temp = 0
    for i in range(n):
        if total_budget >= total + (budget[i] * rest):
            total += budget[i]
            rest -= 1

        else:
            temp = budget[i]
            while total_budget < total + (temp * rest):
                temp -= 1

            print(temp)
            break