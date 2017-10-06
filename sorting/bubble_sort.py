import test_algorithm, array_exchange

def sort(A):
    n = len(A)
    for i in range(n):
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                array_exchange.exchange(A, j, j + 1)
    return A

def test(U, S):
    in_list = list(U)
    output = sort(U)
    return test_algorithm.test(in_list, output, S, 'Bubble')
