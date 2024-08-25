N = int(input())

for i in range(1, N+1):
    N_sum = i + sum(map(int, str(i)))

    if N_sum == N:
        print(i)
        break

else:
    print(0)