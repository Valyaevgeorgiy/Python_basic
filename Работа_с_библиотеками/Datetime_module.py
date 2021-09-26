# Классы tzinfo и timezone применяются для работы с информацией, которая содержит сведения о часовых поясах.
# Создать объект, принадлежащий типу tzinfo невозможно, поскольку этот класс является абстрактным.
# Однако можно воспользоваться наследованием, создав собственный класс на основе tzinfo.
# При этом следует помнить, что для работы с такими объектами придется реализовать несколько абстрактных методов,
# к числу которых относятся utcoffset (смещение по местному времени с UTC), dst (настройка перехода на летнее время),
# а также функция tzname (имя часового пояса в виде строки).
# В приведенной программе демонстрируется создание пользовательского класса UTC0530, в котором описаны методы utcoffset,
# dst и tzname, а также применение нового типа с двумя объектами a и b.
# Таким образом, получается отображение времени со смещением +5:30.

import datetime as dt
from datetime import tzinfo, timedelta, datetime, timezone
class UTC_Moscow_centre(tzinfo):
    def __init__(self, offset=10800, name=None):
        self.offset = timedelta(seconds=offset)
        self.name = name or self.__class__.__name__
    def utcoffset(self, dt):
        return self.offset
    def tzname(self, dt):
        return self.name
    def dst(self, dt):
        return timedelta(0)
a = datetime.now(timezone.utc)
print(a)
b = datetime.now(UTC_Moscow_centre())
print(b)
print(b.utcoffset())
print()
print(b.tzname())
print()
print(b.dst())

# Далее уже идут наиболее популярные функции класса datetime
x = dt.datetime.utcnow()
a = dt.datetime.today().strftime("%d.%m.%Y")
b = dt.datetime.today().strftime("%p %I:%M:%S")
print(a)
print(b)
print()
a = dt.datetime(2020, 3, 19)
b = dt.time(2, 10, 43)
c = dt.datetime.combine(a, b)
print(c)
y = x - a
print()
print(y)
print(y.days, y.microseconds, y.seconds, sep='\n')