num = int(input('введите число'))
if num > 0 and num <= 20:
    print('Это число подходит')
elif num % 3 == 0 and num % 5 == 0:
    print('Ладно, берём')
else:
    print('Не, не берём')

