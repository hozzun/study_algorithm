n = input().strip()

if '0' not in n:
    print(-1)
else:
    num = list(map(int, n))

    if sum(num) % 3 != 0:
        print(-1)
    else:
        num.sort(reverse=True)
        print(''.join(map(str, num)))