"""
part filename to basename and dirname
"""
import os

def path_names():
    # part <dirname>/<basename> 
    path = '/cygdrive/d/alogrithm_python/file_transfer/mydata.py'

    # <basename> : mydata.py
    print ( os.path.basename(path) )
    # <dirname> : /cygdrive/d/alogrithm_python/file_transfer
    print ( os.path.dirname(path) )
    # /cygdrive/d/alogrithm_python/file_transfer/mydata.py
    print ( os.path.expanduser(path) )
    # ('/cygdrive/d/alogrithm_python/file_transfer/mydata', '.py')
    print ( os.path.splitext(path) )

if __name__ == '__main__':
    path_names()