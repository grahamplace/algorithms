import test_algorithm, random

def partition(A, low, high):
    # select 3 random indices
    r = []
    for i in range(0, 3):
        r.append(random.randrange(low, high))

    # get median of these three elements:
    min_r = 0
    max_r = 0
    for i in range(1, 3):
        if r[i] < r[min_r]: min_r = i
        if r[i] > r[max_r] : max_r = i
    f = len(r) - max_r - min_r
    return r[f]

def sort(A, low, high):
    if low < high:
        p = partition(A, low, high)
        sort(A, low, p-1)
        sort(A, p+1, high)
    return A



def test(U, S):
    in_list = list(U)
    output = sort(U, 0, len(U))
    return test_algorithm.test(in_list, output, S, 'Insertion')
