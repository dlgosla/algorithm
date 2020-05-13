T = int(input())
for test_case in range(1, T + 1):
    p, q = map(float, input().split())
    s1 = (1-p)*q
    s2 = p*(1-q)*q
    if(s1<s2 ):
        print("#",test_case," YES")
    else:
        print("#",test_case," NO")

