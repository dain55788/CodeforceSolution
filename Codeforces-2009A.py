t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    c = a//2
    print((c - a) + (b - c))
