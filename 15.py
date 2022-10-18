import pyautogui
a = input('Введите ваше имя: ')
pyautogui.alert(text='Привет, ' + a + '!', title='Привет!', button='OK') 