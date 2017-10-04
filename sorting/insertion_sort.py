import test_algorithm

def sort(A):
    i = 1
    for i in range(1,len(A)):
        for j in range(i - 1, -1, -1):
            if A[j] < A[j + 1] : break
            temp = A[j]
            A[j] = A[j + 1]
            A[j + 1] = temp
    return A



def test(U, S):
    in_list = list(U)
    output = sort(U)
    return test_algorithm.test(in_list, output, S, 'Insertion')
