from collections import Counter

def solve(name):
    count = Counter(name)
    odd_count = 0
    odd_char = ''
    for char, cnt in count.items():
        if cnt % 2 != 0:
            odd_count += 1
            odd_char = char
            if odd_count > 1:
                return "I'm Sorry Hansoo"

    half_name = []
    for char in sorted(count.keys()):
        half_name.append(char * (count[char] // 2))

    left_half = ''.join(half_name)
    if odd_count == 1:
        return left_half + odd_char + left_half[::-1]
    else:
        return left_half + left_half[::-1]

name = input().rstrip()
print(solve(name))