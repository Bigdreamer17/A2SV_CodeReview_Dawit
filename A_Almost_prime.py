n = int(input())
count = 0
for i in range(1, n + 1):
    factors = []
    d = 2
    while d * d <= i:
        while i % d == 0:
            factors.append(d)
            i //= d
        d += 1

    if i > 1:
        factors.append(i)

    if len(set(factors)) == 2:
        count += 1
print(count)
