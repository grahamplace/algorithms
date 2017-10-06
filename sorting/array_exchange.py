def exchange(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    return A
