# A. Creating Words
"""
Sample input:
6
bit set
cat dog
hot dog
uwu owo
cat cat
zzz zzz

Output:
sit bet (swap b and s)
dat cog (swap c and d)
dot hog
owu uwo
cat cat
zzz zzz

"""

def swap(a: str, b: str) -> None:
    a = list(a)
    b = list(b)
    temp = b[0]
    b[0] = a[0]
    a[0] = temp
    a = "".join(a)
    b = "".join(b)
    return a,b

n = int(input())
for i in range(n):
    a, b = map(str, input().split())
    a, b = swap(a, b)
    print(f'{a} {b}')
