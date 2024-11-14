string = str(input())
distinct_char = set(string)

if len(distinct_char) % 2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")