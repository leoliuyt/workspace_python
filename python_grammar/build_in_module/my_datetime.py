from datetime import datetime,timedelta,timezone

#获取当前时间
now = datetime.now()
print('type:',type(now),'value:',now)

#获取指定日期和时间
dt = datetime(2018,8,18,12,12,12)
print('type:',type(dt),'value:',dt)

#dattime->timestamp
timestamp = dt.timestamp()
print(timestamp)

#timestamp->datetime
print(datetime.fromtimestamp(timestamp)) # 本地时间2018-08-18 12:12:12 UTC+8:00
print(datetime.utcfromtimestamp(timestamp)) #UTC时间2018-08-18 04:12:12 UTC+0:00

#str->datetime
cday = datetime.strptime('2018-8-18 12:12:02','%Y-%m-%d %H:%M:%S')#没有时区信息
print(cday)
#datetime->str
print(now.strftime('%a, %b %d %H:%M'))

#datetime +-
newDate = now + timedelta(hours=10)
print(newDate)
newDate = now - timedelta(days=1)
print(newDate)
newDate = now - timedelta(days=1,hours=12)
print(newDate)

#本地时间->UTC
# 本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间
tz_utc_8 = timezone(timedelta(hours=8))#创建时区UTC+8:00
now = datetime.now()
print('UTC8-now:',now)
dt = now.replace(tzinfo=tz_utc_8)
print(dt)

#时区转换
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

#转换为北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)
