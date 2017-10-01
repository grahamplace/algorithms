import test_algorithm, array, math

# A, B MUST be sorted arrays when passed to merge
def merge(A, B):
   C = []
   i = 0
   j = 0
   while i < len(A) or j < len(B):
       if i == len(A):
           C.append(B[j])
           j += 1
           continue
       if j == len(B):
           C.append(A[i])
           i += 1
           continue

       if A[i] <= B[j]:
           C.append(A[i])
           i += 1
       else:
           C.append(B[j])
           j += 1
   return C

def sort(A):
    n = len(A)
    if n <= 1 : return A
    mid = math.floor(n/2)
    a = sort(A[0 : mid])
    b = sort(A[mid : n])
    return merge(a, b)

def test(U, S):
    in_list = list(U)
    output = sort(U)
    return test_algorithm.test(in_list, output, S, 'Merge')
