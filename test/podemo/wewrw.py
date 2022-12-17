# coding=utf-8
import re


def date2timestamp(strdate):
    """
    年月日转时间戳
    :param strdate: 2022-02-01
    :type strdate:
    :return:
    :rtype:
    """
    import datetime
    curr = datetime.datetime.strptime(strdate, '%Y-%m-%d')
    flag = datetime.datetime.strptime('1970-01-01', '%Y-%m-%d')
    return int(((curr - flag).total_seconds() - 60 * 60 * 8) * 1000)


def timestamp2datetime(timestamp):
    '''
    时分秒时间戳转日期时间戳
    :param timestamp:
    :type timestamp:
    :return:
    :rtype:
    '''
    import datetime
    strftime = datetime.datetime.fromtimestamp(int(timestamp / 1000)).strftime('%Y-%m-%d')
    date_timestamp = date2timestamp(strftime)
    return date_timestamp


def str2timestamp(strdate):
    '''
    字符串转日期时间戳
    2022-04-25   2021年06月22日    2021/4/5    2021.4.5    2021-03-21. -2.2091616e+12
    '''
    if re.match('^\d{4}-\d{1,2}-\d{1,2}$', strdate):
        fmt = '%Y-%m-%d'
    elif re.match('^\d{4}-\d{1,2}-\d{1,2}\.$', strdate):
        strdate = strdate.strip('.')
        fmt = '%Y-%m-%d'
    elif re.match('^\d{4}年\d{1,2}月\d{1,2}日$', strdate):
        fmt = '%Y年%m月%d日'
    elif re.match('^\d{4}年\d{1,2}月\d{1,2}$', strdate):
        strdate = strdate + "日"
        fmt = '%Y年%m月%d日'
    elif re.match('^\d{4}/\d{1,2}/\d{1,2}$', strdate):
        fmt = '%Y/%m/%d'
    elif re.match('^\d{4}\.\d{1,2}\.\d{1,2}$', strdate):
        fmt = '%Y.%m.%d'
    elif re.match('^-?\d*\.\d*[E|e]\+\d*$', strdate):
        # 科学计数法
        return int(float(strdate))
    else:
        return int(strdate)
    import time
    return int(time.mktime(time.strptime(strdate, fmt))) * 1000



if __name__ == '__main__':
