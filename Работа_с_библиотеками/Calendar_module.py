import calendar as cln
import time, locale

for i in cln.Calendar(firstweekday=5).iterweekdays():
    print(i)
a = cln.setfirstweekday(cln.TUESDAY)
print()
print(cln.firstweekday())
print()
print(cln.weekday(2002, 10, 8))
print()
print(cln.monthrange(2021, 2))
print()
x = cln.monthcalendar(2021, 10)
for i in x:
    print(i)
print()
struct = time.gmtime()
print(struct)
# time.struct_time(tm_year=2020, tm_mon=5,
# tm_mday=4, tm_hour=10, tm_min=28, tm_sec=54,
# tm_wday=0, tm_yday=125, tm_isdst=0)
print()
print()
sec = cln.timegm(struct)
print(sec)
# 1588588134

time.gmtime(sec)
print()
print()
print(tuple(cln.day_name))
# ('Monday', 'Tuesday', 'Wednesday',
# 'Thursday', 'Friday', 'Saturday', 'Sunday')
print()
print(list(cln.day_abbr))
# ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
print()
print(*list(cln.month_name))
# ['', 'January', 'February', 'March', 'April',
# 'May', 'June', 'July', 'August', 'September',
# 'October', 'November', 'December']
print()
print(*list(cln.month_abbr))
# ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
# 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

print()
print()
print(tuple((cln.day_name)))
# ('Понедельник', 'Вторник', 'Среда',
# 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
print(list(cln.day_abbr))
print()
# ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
print(*list(cln.month_name))
print()
# ['', 'января', 'февраля', 'марта', 'апреля',
# 'мая', 'июня', 'июля', 'августа', 'сентября',
# 'октября', 'ноября', 'декабря']
print(*list(cln.month_abbr))
# ['', 'янв', 'фев', 'мар', 'апр', 'мая', 'июн',
# 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']