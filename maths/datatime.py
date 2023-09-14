from datetime import timedelta
from datetime import datetime
from dateutil.relativedelta import relativedelta

def date_time():
    # using time1 ( 2days 6hours ) - time2 ( 4h 30mn )
    # change times use timedelta functions
    a = timedelta(days=2, hours=6)
    b = timedelta(hours=4.5)
    c = a - b
    print(c.days)
    print(c.seconds)
    print(c.seconds / 3600)
    print(c.total_seconds() / 3600)
    
    # time = day2 - day1
    a = datetime( 2023, 7, 1 )
    b = datetime( 2023, 12, 1 )
    c = b - a
    print ( c.days)


if __name__ == '__main__':
    date_time()