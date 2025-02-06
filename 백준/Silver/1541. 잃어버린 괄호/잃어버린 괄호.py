def solve(modify):
    arr = []
    change = ""
    for i in range(len(modify)):
        if modify[i] == "+":
            arr.append(int(change))
            arr.append("+")
            change = ""
        elif modify[i] == "-":
            arr.append(int(change))
            arr.append("-")
            change = ""
        elif i == len(modify) - 1:
            change += modify[i]
            arr.append(int(change))
        else:
            change += modify[i]

    ans = arr[0]
    negative = False
    for i in range(1, len(arr), 2):
        operator = arr[i]
        num = arr[i + 1]

        if operator == "-": negative = True
        if negative: ans -= num
        else: ans += num

    return ans

modify = input().strip()
print(solve(modify))