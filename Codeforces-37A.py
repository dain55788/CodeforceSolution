# A. Towers

def insertAsc(a, n, x):
    j = n
    while j > 0:
        if a[j - 1] <= x:
            break
        a[j] = a[j - 1]
        j -= 1
    a[j] = x


def insertion(a, n):
    for i in range(1, n):
        x = a[i]
        insertAsc(a, i, x)

def max_tower_length(nums) -> int:
    max_len = 1
    result = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            max_len += 1
        else:
            result = max(result, max_len)
            max_len = 1
    return max(result, max_len)

n = int(input())
arr = list(map(int, input().split()))

total_set = set(arr)
total_num = len(total_set) # total number of towers

insertion(arr, n)

if len(arr) == 1:
    print(f"1 1")
else:
    tower_length = max_tower_length(arr)
    print(f"{tower_length} {total_num}")
