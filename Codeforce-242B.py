n = int(input())
Left = []
Right = []

for i in range(n):
    l, r = map(int, input().split())
    Left.append(l)
    Right.append(r)

left = min(Left)
right = min(Right)
for i in range(n):
    if left == Left[i] and right == Right[i]:
        print(i+1)
        break
print(-1)