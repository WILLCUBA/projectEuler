from math import ceil
def is_palindrome(num):
    s = str(num)
    s1 = s[0: len(s) // 2]
    s2 = s[int(ceil(len(s) / 2)):]
    return s1 == s2[::-1]


result = []

for x in range(100,1000):
    for y in range(100,1000):
        z = x * y
        if is_palindrome(z):
            result.append(z)

print(max(result))