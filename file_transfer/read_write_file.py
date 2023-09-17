"""
Read/Write data to file 
"""
from tempfile import NamedTemporaryFile
import tempfile

def rw_text():
    # write data into file
    # write file with -> 'w'
    with open('mydata.txt', 'w', encoding='utf-8') as wf:
        wf.write('text1\n')
        wf.write('text2\n')

    # append data into file -> 'a'
    with open('mydata.txt', 'a', encoding='utf-8') as wf:
        print( 'Hello World 1!', file=wf )

    # append data into file -> 'wt'
    with open('mydata.txt', 'wt') as wf:
        wf.write( 'Hello World 2!' )

    # read file with -> 'r'
    with open('mydata.txt', 'r', encoding='utf-8') as rf:
        text = rf.read()    
        print(text)

    # get tempfile by NamedTemporaryFile function
    with NamedTemporaryFile() as tempfile:
        print('dirname is: ', tempfile.name)
    
    print('\n')

if __name__ == '__main__':
    rw_text()