import re

s = input()
target = input()

max_count = 0
for i in range(len(s)):
    count = len(re.findall(target, s[i:]))
    if max_count < count:
        max_count = count

print(max_count)
