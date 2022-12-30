s = input()

croatia = {
    "c": ["=", "-"],
    "d": ["-"],
    "l": ["j"],
    "n": ["j"],
    "s": ["="],
    "z": ["="],
}

count = 0
i = 0
length = len(s)
while i < length:
    if i == length - 1:
        i += 1
    elif s[i] in croatia and s[i + 1] in croatia[s[i]]:
        i += 2
    elif s[i] + s[i + 1] == "dz" and i + 2 < len(s) and s[i + 2] == "=":
        i += 3
    else:
        i += 1
    # print(i)
    count += 1

print(count)

"""
다른 풀이
"""
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()

for i in croatia:
    word = word.replace(i, "*")  # input 변수와 동일한 이름의 변수
print(len(word))
