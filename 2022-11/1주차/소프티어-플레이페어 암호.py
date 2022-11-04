import sys
import string

msgs = list(input())
keys = list(input())

alphabet_idx_in_key_metrix = {}

key_metrix = [[0] * 5 for i in range(5)]
unused_keys = list(string.ascii_uppercase)
unused_keys.remove("J")

idx = 0
i = 0
j = 0

for key in keys:
    if not key in unused_keys:
        continue

    i = idx // 5
    j = idx % 5

    key_metrix[i][j] = key
    unused_keys.remove(key)

    alphabet_idx_in_key_metrix[key] = (i, j)

    idx += 1


for unused_key in unused_keys:
    if idx == 25:
        break

    i = idx // 5
    j = idx % 5

    key_metrix[i][j] = unused_key
    alphabet_idx_in_key_metrix[unused_key] = (i, j)
    idx += 1

msg_pairs = []
msg_length = len(msgs)

# if not msg_length // 2 == 0:
#     msgs.append('X')
#     msg_length += 1

i = 0
while True:
    if i >= msg_length:
        break

    left = msgs[i]

    if i == msg_length - 1:
        msg_pairs.append((left, "X"))
        break

    right = msgs[i + 1]

    if left != right:
        msg_pairs.append((left, right))
        i += 2

    else:
        new_right = "Q" if right == "X" else "X"
        msg_pairs.append((left, new_right))
        i += 1


# print(key_metrix)
# print(msg_pairs)
# print(alphabet_idx_in_key_metrix)


encrypted = ""
for (left, right) in msg_pairs:

    left_r, left_c = alphabet_idx_in_key_metrix[left]
    right_r, right_c = alphabet_idx_in_key_metrix[right]

    # print(left_r, left_c,  right_r, right_c, left, right)

    if left_r == right_r:
        left_c = (left_c + 1) % 5
        right_c = (right_c + 1) % 5

    elif left_c == right_c:
        left_r = (left_r + 1) % 5
        right_r = (right_r + 1) % 5

    else:
        right_c, left_c = left_c, right_c

    left_encrypted = key_metrix[left_r][left_c]
    right_encrypted = key_metrix[right_r][right_c]

    # print(left_encrypted + right_encrypted)
    encrypted += left_encrypted + right_encrypted


print(encrypted)
