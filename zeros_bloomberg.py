def zeros_inplace(A):
    n = len(A)
    i,j = 0,0
    for j in range(n-1):
        if A[j+1] != 0:
            A[i], A[j+1] = A[j+1], A[i] #swapping
            i+=1
    return A
