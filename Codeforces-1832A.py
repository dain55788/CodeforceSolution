# A. New Palindrome
# given n string of palindrome, print YES if that string can generate another palindrome, else NO
# method: if the first half substring of the string contains the same character, it could not generate another palindrome.
# if there are at least 2 different characters in the substring, it can otherwise.

new_str = []
n = int(input())
for i in range(n):
    palindrome = str(input())
    palindrome = palindrome[0:len(palindrome)//2]
    k = len(set(palindrome))
    if k == 1:
        print("NO")
    else:
        print("YES")



