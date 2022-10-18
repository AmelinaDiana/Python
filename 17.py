import pyautogui
import pyperclip
import time
a = input('Введите текст: ')
pyperclip.copy(str(a))
pyautogui.hotkey('alt', 'tab')
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'n')
time.sleep(0.5)
print(pyperclip.paste())
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')