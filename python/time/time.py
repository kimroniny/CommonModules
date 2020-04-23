import time

#    %y 两位数的年份表示（00-99）
# 　　%Y 四位数的年份表示（000-9999）
# 　　%m 月份（01-12）
# 　　%d 月内中的一天（0-31）
# 　　%H 24小时制小时数（0-23）
# 　　%I 12小时制小时数（01-12）
# 　　%M 分钟数（00=59）
# 　　%S 秒（00-59）
#
# 　　%a 本地简化星期名称
# 　　%A 本地完整星期名称
# 　　%b 本地简化的月份名称
# 　　%B 本地完整的月份名称
# 　　%c 本地相应的日期表示和时间表示
# 　　%j 年内的一天（001-366）
# 　　%p 本地A.M.或P.M.的等价符
# 　　%U 一年中的星期数（00-53）星期天为星期的开始
# 　　%w 星期（0-6），星期天为星期的开始
# 　　%W 一年中的星期数（00-53）星期一为星期的开始
# 　　%x 本地相应的日期表示
# 　　%X 本地相应的时间表示
# 　　%Z 当前时区的名称
# 　　%% %号本身

# 时间戳
# 1587631530.6981719
timestamp = time.time()

# 时间结构体
# time.struct_time(tm_year=2020, tm_mon=4, tm_mday=23, tm_hour=16, tm_min=46, tm_sec=2, tm_wday=3, tm_yday=114, tm_isdst=0)
time_strcut = time.localtime(time.time())

# 从time_struct或者time_tuple转换为 指定格式 的时间
pretty_struct = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
pretty_tuple = time.strftime('%Y-%m-%d %H:%M:%S', (2019, 2, 24, 12, 3, 6, 12, 3, 0)) # 元组的后面三项都可以为0了

# 从time_struct或者time_tuple转换为 时间戳
timestamp_struct = time.mktime(time.localtime())
timestamp_tuple = time.mktime((2019, 2, 24, 12, 3, 6, 12, 3, 0))

# 从指定格式时间转换为 time_struct
_time_struct = time.strptime("20191212000000", "%Y%m%d%H%M%S")

# 两个测试程序时间的函数
head_to_now = time.perf_counter()
last_to_now = time.process_time()