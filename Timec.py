import time
from error import DatetimeError
#获取指定日期和时间的时间戳
def get_timestamp(date_str, format_str="%Y-%m-%d %H:%M:%S"):
    return int(time.mktime(time.strptime(date_str, format_str)))

#计算倒计时
def get_countdown(start_timestamp,end_timestamp):
    if start_timestamp < 0:
        raise DatetimeError("start_timestamp must be greater than 0")
    if end_timestamp < 0:
        raise DatetimeError("end_timestamp must be greater than 0")
    if start_timestamp > end_timestamp:
        raise DatetimeError("start_timestamp must be less than end_timestamp")
    return end_timestamp - start_timestamp

def countdown(start_time,end_time):
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
    return countdown(get_timestamp(start_time),time.time())
#倒计时
def Icountdown(end_tiem):
    return countdown(time.time(),get_timestamp(end_tiem))