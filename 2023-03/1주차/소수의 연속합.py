'''


'''

import math


def get_primes(n):
    is_prime = [True for _ in range(n + 1)]

    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            j = 2

            while i * j <= n:
                is_prime[i * j] = False
                j += 1

    prime_number = []
    for num in range(2, n + 1):
        if is_prime[num]:
            prime_number.append(num)

    return prime_number


n = int(input())

prime_number = get_primes()
count = 0
interval_sum = 0
end = 0

cnt, summ = 0, 0
i, j = 0, 0
while True:
    if summ == n:
        cnt += 1

    if summ > n:
        summ -= prime_number[i]
        i += 1
    elif j == len(prime_number):
        break
    else:
        summ += prime_number[j]
        j += 1

print(cnt)

# print(count)
