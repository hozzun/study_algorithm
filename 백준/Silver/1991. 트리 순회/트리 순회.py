N = int(input())

graph = [[] for _ in range(130)]

for _ in range(N):
    a, b, c = map(str, input().split())
    a = ord(a)
    b = ord(b)
    c = ord(c)

    graph[a].append(b)
    graph[a].append(c)

def preorder(node):
    if node == 46:
        return

    print(chr(node), end='')
    preorder(graph[node][0])
    preorder(graph[node][1])

def inorder(node):
    if node == 46:
        return

    inorder(graph[node][0])
    print(chr(node), end='')
    inorder(graph[node][1])

def postorder(node):
    if node == 46:
        return

    postorder(graph[node][0])
    postorder(graph[node][1])
    print(chr(node), end='')

preorder(65)
print()
inorder(65)
print()
postorder(65)