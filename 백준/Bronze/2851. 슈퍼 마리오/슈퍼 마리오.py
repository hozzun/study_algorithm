arr = []
for tc in range(10):
    score = int(input())
    arr.append(score)

cnt = 0
temp = 0
for i in arr:
    if cnt + i <= 100:
        cnt += i
        if cnt == 100:
            break
    elif cnt + i > 100:
        temp += i
        break

a = 100 - cnt
b = (cnt + temp) - 100
if cnt == 100:
    print(100)
elif a < b:
    print(cnt)
elif a > b:
    print(cnt+temp)
elif a == b:
    print(cnt+temp)