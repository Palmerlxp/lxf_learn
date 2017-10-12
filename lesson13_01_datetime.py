# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：

import re
from datetime import datetime,timezone,timedelta

def to_timestamp(dt_str,tz_str):
    dt=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    tz_match=re.match(r'^UTC([\+|\-])(\d{1,2}):(\d{2})$',tz_str)
    if tz_match.group(1)=='+':
        utc_dt = dt.replace(tzinfo=timezone(timedelta(hours=int(tz_match.group(2)),minutes=int(tz_match.group(3)))))
    else:
        utc_dt = dt.replace(tzinfo=timezone(timedelta(hours=-int(tz_match.group(2)), minutes=-int(tz_match.group(3)))))
    return utc_dt.timestamp()


t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')

#另一种方法
import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    cday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    r = re.compile(r'^UTC(\+|\-)(\d{1,2}):(\d{2})$')
    utc = r.match(tz_str)
    # print(utc.group(1))
    if utc.group(1) == '+':
        print(cday.timestamp()+(8-int(utc.group(2)))*3600)
    elif  utc.group(1) == '-':
        print(cday.timestamp()+(int(utc.group(2))-8)*3600)

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')#t2运行出结果不对