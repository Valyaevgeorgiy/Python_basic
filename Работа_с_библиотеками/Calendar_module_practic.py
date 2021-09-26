# Подключаем стандартные библиотеки Tkinter, datetime и calendar с помощью import.
# Инициализируем класс root, с помощью которого будет отрисовываться графический интерфейс.
# Задаем заголовок окна «Calendar». Объявляем пустой список days.
# В дальнейшем в нем будут храниться поля таблицы. Каждое такое поле соответствует определенному дню.
# В переменную now будем хранить текущую дату. В переменных year и month будут храниться год и месяц,
# календарь которых в данный момент отображается.

from tkinter import *
import calendar
import datetime as dt
root = Tk()
root.title('Calendar')
days = []
now = dt.datetime.now()
year = now.year
month = now.month

# Меняем текущий месяц
# Функции prew и next будут вызываться при нажатии на одну из клавиш смены месяца.
# Если текущее значение месяца «январь» и пользователь нажмет на кнопку перехода на предыдущий месяц,
# то тогда уменьшится год и месяц поменяет значение на «декабрь».
# Обратите внимание на то, что переменные month и year глобальные. Поэтому перед изменением их значения в функции
# необходимо использовать ключевое слово global.
# Функция fill перерисовывает календарь.

def prew():
    global month, year
    month -= 1
    if month == 0:
        month = 12
        year -= 1
    fill()

def next():
    global month, year
    month += 1
    if month == 13:
        month = 1
        year += 1
    fill()

# Перерисовка календаря
# В функции fill будет перерисовываться отображение всех элементов. Она будет вызываться в начале работы
# программы и каждый раз после изменения месяца, для которого нужно вывести календарь.
# В начале выводим наименование месяца и год. Вычисляем количество дней в предыдущем месяце и записываем
# в переменную prew_month_days. В переменноу week_day запишем номер дня недели первого числа
# месяца (от 0 – если первое число выпадет на понедельник, до 6 – на воскресенье).
# После этого в трех циклах выводим числа и их корректируем их цвета:
# В первом цикле заполняем номера дней выбранного месяца. Отображать будем их черным цветом.
# Если это текущий день, то его фон делаем зелёным.
# Во втором цикле заполняем числа предыдущего месяца. Они отображаться будут серым цветом.
# В третьем цикле добавляем числа следующего месяца. Их также выводим серым цветом.

def fill():
    info_label['text'] = calendar.month_name[month] + ', ' + str(year)
    month_days = calendar.monthrange(year, month)[1]
    if month == 1:
        prew_month_days = calendar.monthrange(year-1, 12)[1]
    else:
        prew_month_days = calendar.monthrange(year, month - 1)[1]
    week_day = calendar.monthrange(year, month)[0]
    for n in range(month_days):
        days[n + week_day]['text'] = n+1
        days[n + week_day]['fg'] = 'black'
        if year == now.year and month == now.month and n == now.day:
            days[n + week_day - 1]['background'] = 'yellow'
            days[n + week_day]['background'] = 'lightgray'
        else:
            days[n + week_day]['background'] = 'lightgray'
    for n in range(week_day):
        days[week_day - n - 1]['text'] = prew_month_days - n
        days[week_day - n - 1]['fg'] = 'gray'
        days[week_day - n - 1]['background'] = '#f3f3f3'
    for n in range(6*7 - month_days - week_day):
        days[week_day + month_days + n]['text'] = n+1
        days[week_day + month_days + n]['fg'] = 'gray'
        days[week_day + month_days + n]['background'] = '#f3f3f3'

# Отображение элементов
# Для отображения календаря в Python 3 мы используем библиотеку Tkinter.
# Воспользуемся её упаковщиком grid. Он представит все создаваемые нами элементы в виде таблицы.
# В первой строке в крайней левой и крайней правой ячейках (с номерами столбцов 0 и 6) отобразим кнопки смены месяцев.
# По центру выведем текстовое поле, в котором будет отображаться текущий год и месяц.
# Это поле будет занимать 5 ячеек таблицы, поэтому выставим параметр columnspan в 5.

prew_button = Button(root, text='<', command=prew)
prew_button.grid(row=0, column=0, sticky='nsew')
next_button = Button(root, text='>', command=next)
next_button.grid(row=0, column=6, sticky='nsew')
info_label = Label(root, text='0', width=1, height=1,
            font=('Verdana', 16, 'bold'), fg='darkorange')
info_label.grid(row=0, column=1, columnspan=5, sticky='nsew')

# Во второй строке выведем сокращенные названия месяцев.
# Дальше отображаем 6 строк по 7 столбцов, которые будем заполнять числами, обозначающими номера дней.
# В завершении используем функцию fill, которая заполнит наш календарь начальными данными – календарем текущего месяца.
# После этого запустим цикл обработки событий mainloop.

for n in range(7):
    lbl = Label(root, text=calendar.day_abbr[n], width=1, height=1,
                font=('Verdana', 10, 'normal'), fg='blue')
    lbl.grid(row=1, column=n, sticky='nsew')
for row in range(6):
    for col in range(7):
        lbl = Label(root, text='0', width=4, height=2,
                    font=('Verdana', 16, 'bold'))
        lbl.grid(row=row+2, column=col, sticky='nsew')
        days.append(lbl)
fill()
root.mainloop()