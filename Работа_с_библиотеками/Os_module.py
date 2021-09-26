import os
import time

def num1():
    print()
    print(os.name)
    print()
    print(os.environ)

#num1()

def num2():
    print()
    print(os.getenv("TMP"))
    print()
    print(os.getcwd())
    print()
    os.chdir(r"C:\Users")

#num2()

def num3():
    os.makedirs(r"D:\folder\first\second\third")
    time.sleep(10)
    # os.rmdir(r"C:\folder") - это удаление 1 папки
    os.removedirs(r"D:\folder\first\second\third")

#num3()

def num4():
    os.startfile(r"C:\Users\Asus\PycharmProjects\Cases_Python\russia_words.txt")

#num4()
