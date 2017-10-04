def test(U, output, S, name):
    print('\n\n' + name + ' Sort:')
    print('Testing ' + name + ' Sort on Array:')
    print('▶️  ', end='')
    print(U)

    # Confirm valid inputs:
    if (len(U) != len(S)):
        print('Input arrays do not have same length. Aborting test.')
        return False

    if output != S:
        print('\n🚨  Arrays do not match! 🚨')
        print('' + name + ' Sort Output:')
        print('❌  ', end='')
        print(output)
        print('\nSolution in File:')
        print('✅  ', end='')
        print(S)
        return False
    else:
        print('\n🎊  Success! Sorted Array:')
        print('✅  ', end='')
        print(output)
        return True
