k = int(input())

chocolate = 1
while chocolate < k:
    chocolate *= 2

check = chocolate
answer = 0
while k % check != 0:
    check //= 2
    answer += 1

print(chocolate, answer)