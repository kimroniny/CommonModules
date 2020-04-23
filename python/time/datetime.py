import datetime, time

# 从 时间戳 转换为 日期 格式
# type: datetime.datetime
date_fromtimestamp = datetime.datetime.fromtimestamp(time.time())
# 将 datetime.datetime 类型的日期转换为 指定格式 的日期
date_fromtimestamp.strftime("%Y%m%d %H%M%S")
# 下面这个和 time.strptime() 的功能类似
datetime.datetime.strptime('20200423 172400', '%Y%m%d %H%M%S')

# 获取当前的时间
# type: datetime.datetime
date_now = datetime.datetime.now()
# 获取当前时间的各个字段
date = datetime.datetime.now().date() # 只有日期，没有时间
year = datetime.datetime.now().year
weekday = datetime.datetime.now().weekday() # 星期几，weekday是几就是星期几

# 日期加减法
qiantian = datetime.datetime.now() - datetime.timedelta(days=2)

