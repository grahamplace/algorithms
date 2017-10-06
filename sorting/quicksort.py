import test_algorithm, array_exchange

def exchange(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    return A

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            array_exchange.exchange(A, i, j)
    array_exchange.exchange(A, i + 1, r)
    return i + 1

def sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        sort(A, p, q - 1)
        sort(A, q + 1, r)
    return A

def test(U, S):
    in_list = list(U)
    output = sort(U, 0, len(U) - 1)
    return test_algorithm.test(in_list, output, S, 'Quick')
