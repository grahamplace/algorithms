def sort(A):
    n = len(A)
    for i in range(n):
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                tmp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = tmp
    return A


def test(U, S):
    print('\nBubble Sort:')
    print('Testing Bubble Sort on Array:')
    print('▶️  ', end='')
    print(U)

    # Confirm valid inputs:
    if (len(U) != len(S)):
        print('Input arrays do not have same length. Aborting test.')
        return False

    s = sort(U)
    if s != S:
        print('\n🚨  Arrays do not match! 🚨')
        print('\nBubble Sort Output:')
        print('❌  ', end='')
        print(s)
        print('\nSolution in File:')
        print('✅  ', end='')
        print(S)
        return False
    else:
        print('\n🎊  Success! Sorted Array:')
        print('✅  ', end='')
        print(s)
        return True
