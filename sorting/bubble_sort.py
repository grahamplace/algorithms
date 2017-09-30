import sys


def parse_input_str(s):
    s = s.replace(' ', '')
    elements = s.split(',')
    elements = [int(e) for e in elements]
    return elements

def bubble_sort_array(A):
    n = len(A)
    for i in range(n):
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                tmp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = tmp
    return A

def main():
    filename = sys.argv[1]

    with open(filename) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

    outfile_name = filename + '.out'
    outfile = open(outfile_name,'w')
    for c in content:
        a = parse_input_str(c)
        s = bubble_sort_array(a)
        s = [str(e) + ',' for e in s]
        outfile.write(''.join(s) + '\n')

    outfile.close()



if __name__ == "__main__":
    main()
