import keyboard as kbd
import time

def num1():
    kbd.write("Python Programming is always fun!", delay=0.1)

    kbd.press_and_release('shift + r, shift + k, \n')

    kbd.press_and_release('R, K')

    # блокируется до нажатия Ctrl

    kbd.wait('Ctrl')

#num1()

def num2():
    # Клавиатурный модуль для ввода горячих клавиш.
    # нажмите, чтобы напечатать rk

    kbd.add_hotkey("ctrl+alt+p", lambda: print("CTRL+ALT+P Pressed!"))

    kbd.add_hotkey('a', lambda: kbd.write('Geek'))

    kbd.add_hotkey('ctrl + shift + a', print, args=('you entered', 'hotkey'))

    kbd.wait('esc')

#num2()

def num3():
    # Пример № 3: Модуль клавиатуры также используется для записи всех действий
    # клавиатуры и воспроизведения их с использованием метода воспроизведения.

    # Записывает все клавиши до нажатия клавиши Escape

    rk = kbd.record(until='Esc')

    # Воспроизвести все ключи

    kbd.play(rk, speed_factor=1)

    kbd.wait('ctrl')

#num3()

def num4():
    # Этот модуль предоставляет нам функцию add_abbreviation()
    # это позволяет нам зарегистрировать горячую клавишу, которая заменяет
    # один набранный текст другим. Например,
    # давайте заменим текст "@email" на адрес электронной почты
    # GEEKS FOR GEEKS: "test@example.com":
    kbd.add_abbreviation('@email', 'valyaev2002@bk.ru')

#num4()

def num5():
    c = 0
    while (kbd.is_pressed('ctrl') == False):
        print(kbd.is_pressed('ctrl'))
        c += 1
    print(kbd.is_pressed('ctrl'))
    print(c)

#num5()

def num6():
    kbd.send("ctrl+A")
    kbd.send('ctrl+X')
    time.sleep(10)
    kbd.send('ctrl+V')

#num6()

def num7():
    kbd.press("ctrl")
    kbd.press('A')
    # release the CTRL button
    kbd.release("ctrl")
    kbd.release('A')

#num7()

def num8():
    events = kbd.record('esc')
    print(kbd.get_typed_strings(events))

#num8()

def num9():
    kbd.on_release(lambda e: print(e.name))
    # Это будет печатать все, что вы нажимаете на клавиатуре

num9()