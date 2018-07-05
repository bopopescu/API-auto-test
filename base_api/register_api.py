def triangles():
    N = [1]
    while True:
        yield N
        N.append(0)
        N = [1] + [N[i] + N[i+1] for i in range(len(N)-1)] + [1]

n = 0
for t in triangles():
    print(t)
    n = n +1
    if n == 10:
        break