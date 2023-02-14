import pyautogui
import time
a = input('введите число: ')
for step in 1,2,3,4,5,6,7:
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.5)