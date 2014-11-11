import numpy as np

# input : list of tuples in order of their multiplication
# output : min number of computation, order of multiplication
# algo:
#   m[i,j] = min in k from {i to j}(m[i,k]+m[k+1,j]+p_{i-1}*p_{k}*p_{j})
#   s[i,j] =  that k

A = [(2, 100), (100, 2), (2, 100)]
def mat(A):
    m = np.zeros((len(A), len(A)), dtype = np.int)
    s = np.zeros((len(A), len(A)), dtype = np.int)
    for d in range(1,len(A)): # d is difference j-i
        for i in range(len(A)-d):
            j=i+d
            m[i,j] = 10000000000000.0 # Assumption: this is infinity
            for k in range(i, j):
                q = m[i,k]+m[k+1,j]+ A[i][0]*A[k][1]*A[j][1]
                if q < m[i,j]: 
                    m[i,j] = q
                    s[i,j] = k

    return m,s, m[0,len(A)-1]
