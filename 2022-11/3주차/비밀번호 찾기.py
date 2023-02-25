n, m = map(int, input().split())

hash = {}
for i in range(n):
    site, password = input().split()
    hash[site.strip()] = password.strip()

for i in range(m):
    site = input().strip()
    print(hash[site])
