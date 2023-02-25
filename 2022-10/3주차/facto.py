def factorial(n):
    if n == 1:
        return 1

    return factorial(n - 1) * n


def factorial2(n):
    answer = 1
    for i in range(2, n + 1):
        answer *= i

    return answer


n = 10
print(factorial(n))
print(factorial2(n))
