import csv
import os

def wr_csv1():
    with open("classmates.csv", mode="w+") as w_file:
        names = ["Имя", "Возраст"]
        file_writer = csv.DictWriter(w_file, delimiter=";", lineterminator="\r", fieldnames=names)
        file_writer.writeheader()
        file_writer.writerow({"Имя": "Саша", "Возраст": "6"})
        file_writer.writerow({"Имя": "Маша", "Возраст": "15"})
        file_writer.writerow({"Имя": "Вова", "Возраст": "14"})

#wr_csv1()

def wr_csv11():
    csv.register_dialect('my_dialect', delimiter=';', lineterminator="\r")
    with open("classmates.csv", mode="w") as w_file:
        file_writer = csv.writer(w_file, 'my_dialect')
        file_writer.writerow(["Имя", "Класс", "Возраст"])
        file_writer.writerow(["Женя", "3", "10"])
        file_writer.writerow(["Саша", "5", "12"])
        file_writer.writerow(["Маша", "11", "18"])

#wr_csv11()

def wr_csv2():
    with open('new_csvfile.csv', mode='w', newline='') as fitr:
        file_writer = csv.writer(fitr, delimiter=';', lineterminator='\r\n')
        file_writer.writerow(['Fio', 'sum_balls', 'grades'])
        file_writer.writerow(['Valyaev G.A.', '273', '5+'])
        file_writer.writerow(['Veselovskiy V.V.', '262', '5+'])
        file_writer.writerow(['Berkman Aidyn', '263', '4'])

#wr_csv2()

with open('new_csvfile.csv', 'r', encoding='utf-8') as fit:
    reader = csv.DictReader(fit, delimiter=';')
    count = 0
    for row in reader:
        if count == 0:
            print()
            print(f'Таблица содержит столбцы с такими названиями: {" | ".join(row)}:')
            print()
        print(f'    {row["Fio"]} сдал ЕГЭ на {row["sum_balls"]} баллов(а) и получил за предмет {row["grades"]} :)')
        count += 1
    print()
    print(f'А всего в этой таблице {count + 1} строк.')

os.startfile(r'C:\Users\Asus\PycharmProjects\Cases_Python\classmates.csv')
os.startfile(r'C:\Users\Asus\PycharmProjects\Cases_Python\new_csvfile.csv')