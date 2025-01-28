import sys

input = sys.stdin.readline
n, m = map(int, input().split())
keywords = set(input().strip() for _ in range(n))
for _ in range(m):
    blog = input().strip()
    used_keywords = set(blog.split(','))
    keywords -= used_keywords
    print(len(keywords))