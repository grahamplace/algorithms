import sys
from os import listdir
from os.path import isfile, join
import bubble_sort, merge_sort, insertion_sort

def parse_input_str(s):
    s = s.replace(' ', '')
    elements = s.split(',')
    elements = [int(e) for e in elements]
    return elements

def get_input_files():
    file_path = 'data'
    files = [f for f in listdir(file_path) if isfile(join(file_path, f))]
    return files

def test(U, S):
    # Add calls to test all additional sorting algorithms here:
    bubble_sort.test(list(U), S)
    merge_sort.test(list(U), S)
    insertion_sort.test(list(U), S)

def main():
    i = 1
    files = get_input_files()
    for s in files:
        with open('data/' + s) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        unsorted = parse_input_str(content[0])
        solution = parse_input_str(content[1])
        print('\n---------------------------------Test ' + str(i) + '---------------------------------')
        print('Testing File: ' + s)
        print('Unsorted Array:')
        print(unsorted)
        print('Sorted Array:  ')
        print(solution)
        test(unsorted, solution)
        print('\n------------------------------------------------------------------------\n')
        i += 1

if __name__ == "__main__":
    main()
