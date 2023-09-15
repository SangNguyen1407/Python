from datetime import datetime

def str_datetime():
    # diff = b - a
    a = datetime( 2023, 7, 1 )
    b = datetime( 2023, 12, 1 )
    diff = b - a
    print( diff )

    # 2012-09-20 00:00:00
    text = '2012-09-20'
    c = datetime.strptime(text, '%Y-%m-%d')
    print( c )
    
    # Friday September 15, 2023
    c = datetime.strftime(datetime.now(), '%A %B %d, %Y')
    print( c )

    # Saturday July 01, 2023
    c = datetime.strftime(datetime( 2023, 7, 1 ), '%A %B %d, %Y')
    print( c )

    # Monday January 01, 1
    c = datetime.strftime(datetime( 1, 1, 1 ), '%A %B %d, %Y')
    print( c )



if __name__ == '__main__':
    str_datetime()