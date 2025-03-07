def z(n, row, col):
    check = 2 ** (n - 1)

    if n == 0:
        return 0

    if row < check and col < check:
        return z(n - 1, row, col)

    elif row < check and col >= check:
        return check ** 2 + z(n - 1, row, col - check)

    elif row >= check and col < check:
        return (2 * (check ** 2)) + z(n - 1, row - check, col)

    elif row >= check and col >= check:
        return (3 * (check ** 2)) + z(n - 1, row - check, col - check)

n, r, c = map(int, input().split())

print(z(n, r, c))