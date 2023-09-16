import os
import time

def file_existence():
    # check existence file
    print ( os.path.exists('/etc/passwd') )
    print( os.path.isfile('/etc/passwd') )
    print( os.path.realpath('/usr/local/bin/python3') )


if __name__ == '__main__':
    file_existence()