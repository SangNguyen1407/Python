"""
file content

TEST1,TEST2,TEST3|TEST4,TEST5,TEST6

with delimiter=','
['TEST1', 'TEST2', 'TEST3|TEST4', 'TEST5', 'TEST6']

with delimiter=' '
['TEST1,TEST2,TEST3|TEST4,TEST5,TEST6']
"""
import csv

def rw_csv():
    # ['TEST1', 'TEST2', 'TEST3|TEST4', 'TEST5', 'TEST6']
    with open('stocks.csv', 'r', newline='') as csvfile:
        f_csv = csv.reader(csvfile, delimiter=',')
        for row in f_csv:
            print(row)

    # ['TEST1,TEST2,TEST3|TEST4,TEST5,TEST6']
    with open('stocks.csv', 'r', newline='') as csvfile1:
        f_csv = csv.reader(csvfile1, delimiter=' ')
        for row in f_csv:
            print(row)

if __name__ == '__main__':
    rw_csv()