'''
datetime
'''

from datetime import datetime, date

def now(format='%Y-%m-%d %H:%M:%S'):
    '''
    获取当前的时间字符串。
    '''
    
    n = datetime.now()
    return n.strftime(format)

def today(format='%Y-%m-%d'):
    '''
    获取今天的时间字符串。
    '''

    t = date.today()
    return t.strftime(format)
