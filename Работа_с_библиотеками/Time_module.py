import time as t

print(t.localtime())
print()

print(t.ctime())
print(t.strftime("Today is %B %d, %Y.", t.localtime()))
print()

pause = 0.1
print("Program started...")
t.sleep(pause)
print(str(pause) + " seconds passed.")

# Таким образом, чтобы сделать задержку в 100 миллисекунд, надо написать
# t.sleep(0.1)

# Классический метод, чтобы узнать время выполнения программы

start = t.time()
t.sleep(5)
finish = t.time()
result = finish - start
print("Program time: " + str(result) + " seconds.")

# Метод вычисления времени выполнения программы,
# который не зависит от работы ОС и текущей платформы

start = t.monotonic()
t.sleep(15)
result = t.monotonic() - start
print("Program time: {:>.3f}".format(result) + " seconds.")