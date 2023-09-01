"""
时间处理模块
用于处理正计时和倒计时
"""



import time
from error import DatetimeError
#获取指定日期和时间的时间戳
def get_timestamp(date_str, format_str="%Y-%m-%d %H:%M:%S"):
    """
    获取指定日期和时间的时间戳
    :param date_str: 日期时间字符串
    :param format_str: 格式字符串
    :return: 指定时间和日期的时间戳
    """
    return int(time.mktime(time.strptime(date_str, format_str)))

#计算倒计时
def get_countdown(start_timestamp,end_timestamp):
    """
    计算倒计时
    :param start_timestamp: 开始时间戳
    :param end_timestamp: 结束时间戳
    :return: 倒计时

    """
    if start_timestamp < 0:
        raise DatetimeError("start_timestamp must be greater than 0")
    if end_timestamp < 0:
        raise DatetimeError("end_timestamp must be greater than 0")
    if start_timestamp > end_timestamp:
        raise DatetimeError("start_timestamp must be less than end_timestamp")
    return end_timestamp - start_timestamp

def countdown(start_time,end_time):
    """
    计算倒计时天数小时分钟秒
    :param start_time: 开始时间
    :param end_time: 结束时间
    :return: 倒计时

    """
    c=get_countdown(start_time,end_time)
    countdown_dict={
        "day":int(c//(24*60*60)),
        "hour":int(c//(60*60)%24),
        "minute":int(c//60%60),
        "second":int(c%60)
    }
    return countdown_dict

#正计时
def Pcountdown(start_time):
    """
    正计时
    :param start_time: 开始时间
    :return: 倒计时
    """
    return countdown(get_timestamp(start_time),time.time())
#倒计时
def Icountdown(end_tiem):
    """
    倒计时
    :param end_tiem: 结束时间
    :return: 倒计时
    """
    return countdown(time.time(),get_timestamp(end_tiem))