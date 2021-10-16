import time
import pyautogui
import webbrowser

def write_comment():
    pyautogui.moveTo(1209, 1010, duration=0.5)
    pyautogui.click()
    time.sleep(0.25)
    pyautogui.typewrite('good!')
    pyautogui.press('enter')


def maint():
    webbrowser.open('https://www.google.com/')

    time.sleep(1)
    pyautogui.moveTo(611, 339, duration=0.25)
    pyautogui.click()

    pyautogui.typewrite('python hello world', 0.05)
    pyautogui.press('enter')

    time.sleep(1)
    pyautogui.moveTo(330, 209, duration=0.25)
    pyautogui.click()

    write_comment()

maint()