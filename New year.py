n=''
while n!='конец':
    print('Введите название страны:')
    n=input()
    r='Вас поздравляет'
    if n=='Россия':
        print(r, 'Дед Мороз из Росии: "С Новым Годом!"')
    elif n=='Италия':
        print(r, 'Бабо Натале из Италии: "Feliceannonuovo"')
    elif n=='Финляндия':
        print(r, 'Йоулупукки из Финляндии: "OnnellistaUuttaVuotta!"')
    elif n=='Норвегия':
        print(r, 'Юлебукк из Норвегии: "GodtNyttаr!"')
    elif n=='Великобритания':
        print(r, 'ФазерКристмас из Великобритании: "HappyNewYear!"')
    elif n=='Албания':
        print(r, 'Бабадимпи из Албании: "GezuarVitin e Ri!"')
    elif n=='Греция':
        print(r, 'Агиос Василис из Греции: "KenouriosChronos!"')
    elif n=='Татарстан':
        print(r, 'Кышбабай из Татарстана: "Яна ел белэн!"')
    elif n=='Франция':
        print(r, 'Пер Ноэль из Франции: "BonneAnnee!"')
    elif n=='Япония':
        print(r, 'Сегацу-сан из Японии: "AkimashiteOmedettoGozaimasu!"')
    elif n=='конец':
        break
    else:
        print('Нет данных по этой стране')
        print('Спасибо за внимание!')	