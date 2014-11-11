def count(n,W={}):
    if n in [0]:
        return 1
    if n in W:
        return W[n]
    W[n] = sum([count(n-i,W) for i in [1,2,3] if n-i >=0])
    return W[n]

count(4)
